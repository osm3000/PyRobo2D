# AXB test

from walls import *
import math
from sympy import *
import numpy as np
from robot import *

def line(line_coordinates):
    X1, Y1, X2, Y2 = line_coordinates
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

def line_line_intersection(L1_coord, L2_coord):
    A1, b1 = line(L1_coord)
    A2, b2 = line(L2_coord)

    X1, Y1, X2, Y2 = L1_coord
    X3, Y3, X4, Y4 = L2_coord

    if A1 == A2: # The two line are parallel
        return False, -1
    else:
        Xa = (b2 - b1) / (A1 - A2)

        if (Xa < max(X1, X2)) and (Xa > min(X1, X2)) and \
        (Xa < max(X3, X4)) and (Xa > min(X3, X4)):
            distance = estimate_range((A1, b1), L1_coord, Xa)
            return True, distance
        else:
            return False, -1

def circle_circle_intersection(circle_center0, circle_radius0, circle_center1, circle_radius1):
    c_x0, c_y0 = circle_center0
    c_x1, c_y1 = circle_center1
    distance_between_centers = np.sqrt((c_x0 - c_x1)**2 + (c_y0 - c_y1)**2)
    if distance_between_centers <= (circle_radius0 + circle_radius1):
        return True, distance_between_centers
    else:
        return False, -1

def line_circle_intersection(circle_center, circle_radius, line_data):
    A, b = line(line_data)
    c_x, c_y = circle_center
    r = circle_radius

    # TODO: Solving the equations using this sympy is super slow
    # x, y = symbols('x y', real = True) # 'real' is to show only the real solutions
    # possible_solutions = solve([(x-c_x)**2 + (y-c_y)**2 - r**2, A*x + b - y], (x, y))

    # This is a direct solution, which is much faster
    possible_solutions = [] # At maximum, there are two possible solutions
    try: # Add the 1st solution
        solution = ((-A*b + A*c_y + c_x - np.sqrt(-A**2*c_x**2 + A**2*r**2 - 2*A*b*c_x + 2*A*c_x*c_y - b**2 + 2*b*c_y - c_y**2 + r**2))/(A**2 + 1), (A**2*c_y + A*c_x - A*np.sqrt(-A**2*c_x**2 + A**2*r**2 - 2*A*b*c_x + 2*A*c_x*c_y - b**2 + 2*b*c_y - c_y**2 + r**2) + b)/(A**2 + 1))
        possible_solutions.append(solution)
    except:
        pass
    try: # Add the 2nd solution
        solution = ((-A*b + A*c_y + c_x + sqrt(-A**2*c_x**2 + A**2*r**2 - 2*A*b*c_x + 2*A*c_x*c_y - b**2 + 2*b*c_y - c_y**2 + r**2))/(A**2 + 1), (A**2*c_y + A*c_x + A*sqrt(-A**2*c_x**2 + A**2*r**2 - 2*A*b*c_x + 2*A*c_x*c_y - b**2 + 2*b*c_y - c_y**2 + r**2) + b)/(A**2 + 1))
        possible_solutions.append(solution)
    except:
        pass

    if len(possible_solutions) == 0: # No solution is found
        return False, -1
    else:
        # No we need to check which of these solutions lies on the line segment, then,
        # we will check which is closest
        X1, Y1, X2, Y2 = line_data
        distance = float("inf")
        for solution in possible_solutions:
            Xa, Ya = float(solution[0]), float(solution[1])
            if (Xa <= max(X1, X2)) and (Xa >= min(X1, X2)):
                solution_distance = np.sqrt((X1 - Xa)**2 + (Y1 - Ya)**2)
                if solution_distance < distance:
                    distance = solution_distance
        if distance == float("inf"):
            return False, -1
        else:
            return True, distance

def sensor_range_detection(robot, objects_list):
    global_distances = []
    for sensor_id, sensor in enumerate(robot.sensors):
        distances = [-1 for i in range(len(sensor.current_sensor_rays))]
        for object_id, object_item in enumerate(objects_list):
            if (sensor.color ==  object_item.color) and (object_item.properties["detectable_enabled"]):
                for sensor_ray in range(len(sensor.current_sensor_rays)):
                    if isinstance(object_item, Wall):
                        interstection_detection, detection_range = line_line_intersection(sensor.current_sensor_rays[sensor_ray], \
                        object_item.wall_coordinates)

                    elif isinstance(object_item, Robot) or isinstance(object_item, Ball):
                        interstection_detection, detection_range = line_circle_intersection(circle_center=object_item.circle_position, \
                        circle_radius=object_item.circle_radius, line_data=sensor.current_sensor_rays[sensor_ray])

                    if interstection_detection:
                        if distances[sensor_ray] == -1:
                            distances[sensor_ray] = detection_range
                        elif distances[sensor_ray] > detection_range: # Report only the near object_line
                            distances[sensor_ray] = detection_range
        global_distances += distances
    return global_distances

def collision_detection(source_object, object_list):
    """
    The goal here is to detect all possible
    """
    intersection_dic    = {}
    for object_index, object_item in enumerate(object_list):
        if object_item.properties["collision_enabled"]:
            if isinstance(source_object, Robot) and isinstance(object_item, Ball):
                interstection_detection, detection_range = circle_circle_intersection(circle_center0=object_item.circle_position, \
                circle_radius0=object_item.circle_radius, \
                circle_center1=source_object.circle_position_temp, \
                circle_radius1=source_object.circle_radius)
                intersection_dic[(source_object.properties["name"], object_item.properties["name"])] = interstection_detection

            elif isinstance(source_object, Robot) and isinstance(object_item, Wall):
                interstection_detection, detection_range = line_circle_intersection(\
                circle_center=source_object.circle_position_temp, \
                circle_radius=source_object.circle_radius, \
                line_data=object_item.wall_coordinates)
                intersection_dic[(source_object.properties["name"], object_item.properties["name"])] = interstection_detection

            else:
                raise("Undefined collision!")
    return intersection_dic
