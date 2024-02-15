import math as m

def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    d = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    if d > 0:
        return 1 
    elif d < 0:
        return -1 
    else:
        return 0
    
def gift_wrapping(points):
    on_hull = min(points)
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = orientation(on_hull, next_point, point)
            if next_point == on_hull or o == 1 or (o == 0 and m.dist(on_hull, point) > m.dist(on_hull, next_point)):
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break
    return hull

points1 = [(0, 0), (1, 1), (1, 2), (2, 2), (3, 0)]
points2 = [(0, 3), (3, 3), (2, 1), (1, 3), (2, 0)]

gift_wrapping(points1)
gift_wrapping(points2)
