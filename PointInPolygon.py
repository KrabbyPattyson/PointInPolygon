# Bryce Patterson
# The purpose of this program is to find out whether a particular point is in a group of edges, namely a polygon

# *********************************
# **** Define helper functions ****

# Returns whether two numbers are appoximately equal
# This will be helpful when detecting intersecting edges below
def approx(n1, n2) -> bool:
    threshold = 0.001
    return abs(n1 - n2) < threshold

# This function returns whether the line drawn from a point intersects an edge:
# 0: No intersections
# 1: One intersection
# 2: Point is on the edge
# There are five cases:
# Case 1: The edge is to the left of the point
# Case 2: The edge is horizontal to the point
# Case 3: The point is on the edge/intersection
# Case 4: The point is on one of the endpoints
# Case 5: The point is to the left of the edge
def intersect_edge(edge, point) -> int:
    # For convenience, define these local variables:
    xp = point[0]
    yp = point[1]
    x1 = edge[0][0]
    x2 = edge[1][0]
    y1 = edge[0][1]
    y2 = edge[1][1]

    # Case 1: Edge is on the left of p
    if x1 < xp and x2 < xp:
        return 0
    # Case 2: Edge is horizontal to p
    elif approx(y1, y2):
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        if xmin <= xp and xp <= xmax and approx(yp, y1):
            return 2
        else:
            return 0
    else:
        x = ((yp - y1) / (y2 - y1)) * (x2 - x1) + x1
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        # Case 3: The point is on the intersection (as opposed to in front of it, case 5)
        if approx(x, xp) and ymin <= yp <= ymax:
            return 2
        # Case 4: The point is one of the endpoints of the edge
        elif xp < x1 and approx(yp, y1):
            if y1 < y2:
                return 1
            else:
                return 0
        elif xp < x2 and approx(yp, y2):
            if y2 < y1:
                return 1
            else:
                return 0
        # Case 5: Intersection point is inside the edge
        elif x > xp and ymin < yp < ymax:
            return 1
        else:
            return 0
            


# This function returns whether a point intersects any edge of a polygon
def point_in_polygon(point) -> int:
    k = 0
    for edge in polygon_points:
        m = intersect_edge(edge, point)
        if file_info_output:
            print("Edge ", edge, ", intersection: ", m)
        if m == 2:
            return 2
        else:
            k += m
    return k % 2


# *************************
# **** Begin main code ****

# Ask for the file location, then pick apart the points inside
# and sort them into their respective groups.

# TODO: When finished debugging, undo comments below

file_info_output = False

file_loc = input("Enter the file location: ")
file = open(file_loc, "r")

polygon_points_size = int(file.readline())

# Polygon_points are formatted as below:
# = [edge, edge, edge]
# edge = [p1, p2]
# p1, p2 = [x, y]
polygon_points = []

# Query_points are as below:
# = [point, point, point]
# point = [x, y]
query_points = []

# Populate polygon_points with points from file
polygon_str = "Polygon PL ["
for inc in range(polygon_points_size):
    line = file.readline().replace("\n","")
    line = line.split(" ")
    polygon_str += ("(" + line[0] + ", " + line[1] + "), ")
    line[0] = float(line[0])
    line[1] = float(line[1])
    if inc == 0:
        polygon_points.append([line, line])
    else:
        polygon_points.append([polygon_points[inc-1][1], line])
# Attach final point to the beginning
if polygon_points_size > 1:
    polygon_points[0][0] = polygon_points[polygon_points_size-1][1]
polygon_str += "]"

# Populate query_points with final points from file
for line in file:
    line = line.replace("\n","").split(" ")
    line[0] = float(line[0])
    line[1] = float(line[1])
    query_points.append(line)

if file_info_output:
    print("Polygon PL: ", polygon_str)
for point in query_points:
    print("Point P", point)
    print("Is P inside PL?")
    
    result = point_in_polygon(point)
    if result == 1:
        print("RESULT: P is INSIDE PL")
    elif result == 2:
        print("RESULT: P IS ON THE EDGE OF PL")
    else:
        print("RESULT: P is OUTSIDE PL")
