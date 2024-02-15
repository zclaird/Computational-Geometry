import math

def bruteForce(points):
    min_dist = float("inf")  # marks that no points have been compared yet
    p1 = None  # No points set initially as closest pair
    p2 = None

    for i in range(len(points)):  # start on point 1
        for j in range(i + 1, len(points)):  # compare to all other points
            d = math.dist(points[i], points[j])  # get distance at each set
            if d < min_dist:  # compare distance
                min_dist = d  # update min
                p1 = points[i]  # update points
                p2 = points[j]
    return p1, p2

def closest_points(points):
    if not points:  # Handle empty list case
        return None, None

    x = sorted(points, key=lambda point: point[0])  # sorts tuples by x
    y = sorted(points, key=lambda point: point[1])  # sorts tuples by y
    return recursion(x, y)  # here we jump into the algorithm

def recursion(x, y):
    n = len(x)
    if n <= 3:  # covers base cases, if n is 3 or less it's trivial to find
        return bruteForce(x)
    else:
        midpoint = x[n // 2]  # define midpoint based on x coords
        xl = x[:n // 2]  # get all points up to (not including) midpoint
        xr = x[n // 2:]  # get all points from midpoint to end
        yl = []  # lists to store sorted y values for each side
        yr = []
        for point in y:
            if point[0] <= midpoint[0]:  # if x is less than midpoint x,
                yl.append(point)  # append to left subarray
            else:
                yr.append(point)  # if not, append right
        (p1l, p2l) = recursion(xl, yl)  # run function recursively for
        (p1r, p2r) = recursion(xr, yr)  # left and right sides to get
        # Choose minimum between the two pairs based on delta left or right
        # being smaller
        (p1, p2) = (p1l, p2l) if math.dist(p1l, p2l) < math.dist(p1r, p2r) else (p1r, p2r)
        # Define the center "band," for each point in y if the x coordinate is
        # within midpoint val +/- delta, then those values are considered in the
        # band.  Since we checked all other points, this band guarantees that our
        # points are on opposite sides of the midpoint.
        band = [point for point in y if midpoint[0] - math.dist(p1, p2) < point[0] < midpoint[0] + math.dist(p1, p2)]
        for i in range(len(band)):  # iterate loop for each point in the band
            for j in range(i + 1, min(i + 7, len(band))):  # traverse the next 6 points
                d_prime = math.dist(band[i], band[j])  # check distance between new pairs
                if d_prime < math.dist(p1, p2):  # check pair
                    p1, p2 = band[i], band[j]  # update if smaller
        return p1, p2

# Testing the function
points = [(1, 3), (-4, 5), (6, 2), (7, 4), (-2, -4)]
print(closest_points(points))

# Test with empty list
empty_points = []
print(closest_points(empty_points))

bruteForce([(1, 3), (2, 4)])
