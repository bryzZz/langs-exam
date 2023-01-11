class Point:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y


class DistanceMeter:
  def __init__(self) -> None:
    self.points = []

  def distance_between(self, p1: Point, p2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

  def add(self, point: Point):
    self.points.append(point)

    return self

  def measure(self):
    res = 0
    for i in range(1, len(self.points)):
      res += self.distance_between(self.points[i], self.points[i - 1])

    return res


meter = DistanceMeter()
print(meter.add(Point(0, 0)).add(Point(2, 0)).add(Point(2, 3)).measure())
