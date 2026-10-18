"""Numeric invariant test, independent of a renderer. Run with Python 3."""

def polygon_area(points):
    return abs(sum(x * points[(i + 1) % len(points)][1] - y * points[(i + 1) % len(points)][0]
                   for i, (x, y) in enumerate(points))) / 2

for k in [-2, -0.65, 0, 0.65, 2]:
    base = [(-2, -1), (1, -1), (1, 1), (-2, 1)]
    mapped = [(x + k * (y + 1), y) for x, y in base]
    assert abs(polygon_area(mapped) - 6) < 1e-12
    for y in [-1, -0.5, 0, 0.5, 1]:
        left, right = -2 + k * (y + 1), 1 + k * (y + 1)
        assert abs((right - left) - 3) < 1e-12
print('PASS: area 6 and width 3 at 5 shears x 5 slice heights')
