import requests
from tqdm import tqdm

def get_error(a, b):
    return float(requests.get(f"http://ramcdougal.com/cgi-bin/error_function.py?a={a}&b={b}", headers={"User-Agent": "MyScript"}).text)

def gradient_estimate(a, b, delta):
    error = get_error(a, b)

    error_delta_a = get_error(a + delta, b)
    gradient_a = (error_delta_a - error)/delta

    error_delta_b = get_error(a, b + delta)
    gradient_b = (error_delta_b - error)/delta

    return gradient_a, gradient_b

def gradient_descent(start_a, start_b, alpha, tolerance, iterations):
    a = start_a
    b = start_b
    current_error = 1
    new_error = 0
    for i in tqdm(range(iterations), desc = "Gradient Descent"):
        current_error = get_error(a, b)
        gradient_a, gradient_b = gradient_estimate(a, b, 0.00001)
        new_a = a - alpha*gradient_a
        new_a = min(max(new_a, 0), 1)
        new_b = b - alpha*gradient_b
        new_b = min(max(new_b, 0), 1)

        new_error = get_error(new_a, new_b)
        if abs(current_error - new_error) < tolerance:
            print("Error converged within tolerance")
            return new_a, new_b, new_error
        
        a = new_a
        b = new_b
    print("Reached max number of iterations")
    return a, b, new_error

start_points = [(0.1, 0.1), (0.5, 0.5), (0.9, 0.9), (0.1, 0.9), (0.9, 0.1), (0.2, 0.6), (0.7, 0.2)]
results = []
for start_a, start_b in tqdm(start_points, desc = "Start Points"):
    final_a, final_b, error = gradient_descent(start_a, start_b, 0.1, 0.0001, 20)
    results.append((final_a, final_b, error))

for result in results:
    print(result)