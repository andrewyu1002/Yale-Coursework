import numpy as np
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import random

def lat_lon_to_cartesian(lat, lon):
    """Convert latitude and longitude to Cartesian coordinates."""
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = np.cos(lat_rad) * np.cos(lon_rad)
    y = np.cos(lat_rad) * np.sin(lon_rad)
    z = np.sin(lat_rad)
    return np.array([x, y, z])


def cartesian_to_lat_lon(cartesian_coords):
    """Convert Cartesian coordinates to latitude and longitude."""
    x, y, z = cartesian_coords
    lon = np.arctan2(y, x)
    hyp = np.sqrt(x**2 + y**2)
    lat = np.arctan2(z, hyp)
    return np.degrees(lat), np.degrees(lon)

def cosine_similarity(vec1, vec2):
    """Calculate cosine similarity between two vectors."""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

df = pd.read_csv("problem_set_3/worldcities.csv")
city_data = df[['lat','lng']].copy()
city_data['cartesian'] = city_data.apply(lambda row: lat_lon_to_cartesian(row['lat'], row['lng']), axis = 1)
pts = city_data['cartesian'].tolist()

def k_means(k):
    centers = random.sample(pts, k)
    old_cluster_ids, cluster_ids = None, []
    while cluster_ids != old_cluster_ids:
        old_cluster_ids = list(cluster_ids)
        cluster_ids = []
        for pt in pts:
            closest_cluster = -1
            max_similarity = -1
            for i, center in enumerate(centers):
                similarity = cosine_similarity(pt, center)
                if similarity > max_similarity:
                    closest_cluster = i
                    max_similarity = similarity
            cluster_ids.append(closest_cluster)
        city_data['cluster'] = cluster_ids
        cluster_pts = [[pt for pt, cluster in zip(pts, cluster_ids) if cluster == match] for match in range(k)]
        centers = [np.mean(pts, axis = 0)/np.linalg.norm(np.mean(pts, axis = 0)) for pts in cluster_pts]
    return centers

def plot(city_data, k, run):
    fig, ax = plt.subplots(subplot_kw={"projection": ccrs.Robinson()})
    ax.set_global()
    ax.coastlines()

    # Plot each cluster in a different color
    for i in range(k):
        cluster_points = city_data[city_data['cluster'] == i]
        lons = cluster_points['lng']
        lats = cluster_points['lat']
        ax.scatter(
            lons, lats, s=0.2, transform=ccrs.PlateCarree(), label=f"Cluster {i+1}"
        )
    plt.title(f"K-Means Clustering with k = {k}, Run {run}")
    plt.show()

k_means(5)
plot(city_data, 5, 1)
k_means(5)
plot(city_data, 5, 2)
k_means(5)
plot(city_data, 5, 3)
k_means(7)
plot(city_data, 7, 1)
k_means(7)
plot(city_data, 7, 2)
k_means(7)
plot(city_data, 7, 3)
k_means(15)
plot(city_data, 15, 1)
k_means(15)
plot(city_data, 15, 2)
k_means(15)
plot(city_data, 15, 3)