import pandas as pd
from sklearn import decomposition, preprocessing
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

data = pd.read_excel('Computation Methods for Informatics/problem_set_4/Rice_Cammeo_Osmancik.xlsx')

scaler = preprocessing.StandardScaler()
my_cols = ['Area', 'Perimeter', 'Major_Axis_Length', 'Minor_Axis_Length', 'Eccentricity', 'Convex_Area', 'Extent']
data_scaled = scaler.fit_transform(data[my_cols])

pca = decomposition.PCA(n_components=2)
data_reduced = pca.fit_transform(data_scaled)
pc0 = data_reduced[:, 0]
pc1 = data_reduced[:, 1]

color_mapping = {'Cammeo': 'red', 'Osmancik': 'blue'}
data['Class_Color'] = data['Class'].map(color_mapping)
plt.scatter(pc0, pc1, c = data['Class_Color'], s = 3)
plt.xlabel('pc0')
plt.ylabel('pc1')
plt.title('PCA of Rice Data')
for label, color in color_mapping.items():
    plt.scatter([], [], c=color, label=label)
plt.legend(title='Class')
plt.show()

class QuadTree:
    def __init__(self, xlo, ylo, xhi, yhi, points, max_points = 4):
        self.bounds = (xlo, ylo, xhi, yhi)
        self.points = points
        self.children = []
        self.max_points = max_points

        if len(points) > max_points:
            self.subdivide()

    def subdivide(self):
        xlo, ylo, xhi, yhi = self.bounds
        xmid = (xlo + xhi) / 2
        ymid = (ylo + yhi) / 2
        quadrants = [[],[],[],[]]
        for px, py, label in self.points:
            if px <= xmid and py <= ymid:
                quadrants[0].append((px, py, label))
            elif px > xmid and py <= ymid:
                quadrants[1].append((px, py, label))
            elif px <= xmid and py > ymid:
                quadrants[2].append((px, py, label))
            else:
                quadrants[3].append((px, py, label))

        self.children = [
            QuadTree(xlo, ylo, xmid, ymid, quadrants[0], self.max_points),
            QuadTree(xmid, ylo, xhi, ymid, quadrants[1], self.max_points),
            QuadTree(xlo, ymid, xmid, yhi, quadrants[2], self.max_points),
            QuadTree(xmid, ymid, xhi, yhi, quadrants[3], self.max_points)
        ]

        self.points = None
    
    def contains(self, x, y):
        xlo, ylo, xhi, yhi = self.bounds
        return (xlo <= x <= xhi and ylo <= y <= yhi)
    
    def small_containing_quadtree(self, x, y):
        if not self.contains(x,y) or not self.children:
            return self
        for child in self.children:
            if child.contains(x,y):
                return child.small_containing_quadtree(x,y)
            
    def _within_distance(self, x, y, d):
        xlo, ylo, xhi, yhi = self.bounds
        closest_x_in_bounds = min(max(x, xlo), xhi)
        closest_y_in_bounds = min(max(y, ylo), yhi)
        return (closest_x_in_bounds - x)**2 + (closest_y_in_bounds - y)**2 <= d**2
    
    def leaves_within_distance(self, x, y, d):
        if not self._within_distance(x, y, d):
            return []
        if self.children:
            neighbor_quadtrees = []
            for child in self.children:
                neighbor_quadtrees.extend(child.leaves_within_distance(x, y, d))
            return neighbor_quadtrees
        else:
            return [(px, py, label) for px, py, label in self.points if (px - x)**2 + (py - y)**2 <= d**2]
        
    def query(self, x, y, k):
        init_tree = self.small_containing_quadtree(x, y)
        neighbors = init_tree.points
        radius = 0.1
        while len(neighbors) < k:
            neighbors = self.leaves_within_distance(x, y, radius)
            radius *= 2
        neighbors = sorted(neighbors, key = lambda p: ((p[0] - x)**2 + (p[1] - y) **2))[:k]
        return neighbors

def knn(quad_tree, x, y, k):
    neighbors = quad_tree.query(x, y, k)
    labels = [label for _, _, label in neighbors]
    label_counts = Counter(labels)
    most_common_label = label_counts.most_common(1)[0][0]
    return most_common_label

train_data, test_data = train_test_split(data, test_size = 0.2, random_state = 1)
train_data_scaled = scaler.fit_transform(train_data[my_cols])
test_data_scaled = scaler.transform(test_data[my_cols])
train_data_reduced = pca.fit_transform(train_data_scaled)
test_data_reduced = pca.transform(test_data_scaled)
train_data['pc0'] = train_data_reduced[:,0]
train_data['pc1'] = train_data_reduced[:,1]
test_data['pc0'] = test_data_reduced[:,0]
test_data['pc1'] = test_data_reduced[:,1]

train_points = list(zip(train_data['pc0'], train_data['pc1'], train_data['Class']))
xlo, ylo = train_data[['pc0', 'pc1']].min()
xhi, yhi = train_data[['pc0', 'pc1']].max()
quad_tree = QuadTree(xlo, ylo, xhi, yhi, train_points)

def knn_test(test_data, quad_tree, k):
    predictions = []
    for _, row in test_data.iterrows():
        prediction = knn(quad_tree, row['pc0'], row['pc1'], k)
        predictions.append(prediction)
    correct_labels = test_data['Class']
    cm = confusion_matrix(correct_labels,predictions, labels = ['Cammeo', 'Osmancik'])
    df_cm = pd.DataFrame(
        cm,
        index = ['True Cammeo', 'True Osmancik'],
        columns = ['Pred Cammeo', 'Pred Osmancik']
    )
    return df_cm

cm_k1 = knn_test(test_data, quad_tree, k=1)
print("k = 1 Confusion Matrix:\n", cm_k1)

cm_k5 = knn_test(test_data, quad_tree, k=5)
print("k = 5 Confusion Matrix:\n", cm_k5)