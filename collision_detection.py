from walls import *
import math
from sympy import *
import numpy as np
def line(line_coordinates):
    X1, Y1, X2, Y2 = line_coordinates
    if X1 == X2:
        X1 += 0.0001
    if Y1 == Y2:
        Y1 += 0.0001
    try:
        A1 = (Y1-Y2)/(X1-X2) # Pay attention to not dividing by zero
    except:
        A1 = float("inf") # Just a large value, outside the window size

    b1 = Y1-A1*X1# = Y2-A1*X2
    return A1, b1

def estimate_range(L1, L1_coord, Xa):
    A1, b1 = L1
    X1, Y1, X2, Y2 = L1_coord

    Ya = (A1 * Xa) + b1
    distance = math.sqrt((X1 - Xa)**2 + (Y1 - Ya)**2)
    return distance

def line_line_intersection(L1, L2, L1_coord, L2_coord):
    A1, b1 = L1
    A2, b2 = L2

    X1, Y1, X2, Y2 = L1_coord
    X3, Y3, X4, Y4 = L2_coord

    if X1 == X2:
        X1 += 0.0001
    if X3 == X4:
        X3 += 0.0001

    if Y1 == Y2:
        Y1 += 0.0001
    if Y3 == Y4:
        Y3 += 0.0001

    if A1 == A2: # The two line are parallel
        print ("Parallel Lines")
        return False, -1
    else:
        Xa = (b2 - b1) / (A1 - A2)

        if (Xa < max(X1, X2)) and (Xa > min(X1, X2)) and \
        (Xa < max(X3, X4)) and (Xa > min(X3, X4)):
            distance = estimate_range(L1, L1_coord, Xa)
            return True, distance
        else:
            return False, -1

def line_circle_intersection(circle_center, circle_radius, line_data):
    A, b = line(line_data)
    c_x, c_y = circle_center
    r = circle_radius

    x, y = symbols('x y', real = True) # 'real' is to show only the real solutions
    possible_solutions = solve([(x-c_x)**2 + (y-c_y)**2 - r**2, A*x + b - y], (x, y))
    if len(possible_solutions) == 0: # No solution is found
        return False, -1
    else:
        # No we need to check which of these solutions lies on the line segment, then,
        # we will check which is closest
        X1, Y1, X2, Y2 = line_data
        distance = float("inf")
        for solution in possible_solutions:
            Xa, Ya = float(solution[0]), float(solution[1])
            if (Xa < max(X1, X2)) and (Xa > min(X1, X2)):
                solution_distance = np.sqrt((X1 - Xa)**2 + (Y1 - Ya)**2)
                if solution_distance < distance:
                    distance = solution_distance
        if distance == float("inf"):
            return False, -1
        else:
            return True, distance

def sensor_range_detection(sensor, objects_list):
    distances = [-1 for i in range(len(sensor.current_sensor_rays))]
    for objects in range(len(objects_list)):
        if sensor.color !=  objects_list[objects].color:
            continue
        for sensor_ray in range(len(sensor.current_sensor_rays)):
            sensor_line = line(sensor.current_sensor_rays[sensor_ray])
            if isinstance(objects_list[objects], Wall):
                object_line = line(objects_list[objects].wall_coordinates)
                interstection_detection, detection_range = line_line_intersection(sensor_line, object_line, sensor.current_sensor_rays[sensor_ray], objects_list[objects].wall_coordinates)
            elif isinstance(objects_list[objects], Robot) or isinstance(objects_list[objects], Ball):
                interstection_detection, detection_range = line_circle_intersection()
            if interstection_detection:
                if distances[sensor_ray] == -1:
                    distances[sensor_ray] = detection_range
                elif distances[sensor_ray] > detection_range: # Report only the near object_line
                    distances[sensor_ray] = detection_range
    print (distances)

# line_data = [10, 0, 0, -10]
# line_data = [4, 4, -4, -4]
# circle_center = [0, 0]
# circle_radius = 1
# print (line_circle_intersection(circle_center, circle_radius, line_data))