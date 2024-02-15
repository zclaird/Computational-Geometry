import math
from closest_pair import closest_points

points = [(1, 3), (-4, 5), (6, 2), (7, 4), (-2, -4)]

def test_closest_pair(points):
    result = closest_points(points)
    assert result == ((6, 2), (7, 4), math.dist((6, 2), (7, 4)))