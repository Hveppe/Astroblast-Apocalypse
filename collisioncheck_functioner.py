import math


def collisionchecker(firstobject, seconobject):
    if (firstobject.x + firstobject.width > seconobject.x and
            firstobject.x < seconobject.x + seconobject.width and
            firstobject.y + firstobject.height > seconobject.y and
            firstobject.y < seconobject.y + seconobject.height):
        return True
    return False


def collisionchecker_circle_square(circle, square):
    # Finder afstanden mellem det tæteste punkt mellem square og circle
    closest_x = max(square.x, min(circle.x, square.x + square.width))
    closest_y = max(square.y, min(circle.y, square.y + square.height))

    distance = math.sqrt((circle.x - closest_x) ** 2 + (circle.y - closest_y) ** 2)

    # Checker om distancen er mindre eller det samme som radius
    if distance <= circle.radius:
        return True
    return False


def collisionchecker_circle(circle1, circle2):
    distance = ((circle2.x - circle1.x) ** 2 + (circle2.y - circle1.y) ** 2) ** 0.5

    if distance <= (circle1.radius + circle2.radius):
        return True
    else:
        return False
