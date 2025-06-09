class MouseOver:
    def __init__(self, rectangles):
        self.rectangles = rectangles

    def find_rectangle(self, x, y):
        result = None
        for x1, y1, dx, dy in self.rectangles:
            x2, y2 = x1 + dx, y1 + dy
            if x1<=x<=x2 and y1<=y<=y2:
                return x1, y1, dx, dy
        return result


rectangles = [(9, 8, 9, 3), (6, 4, 15, 3), (9, 16, 9, 3), (6, 20, 15, 3), (5, 9, 3, 9), (1, 6, 3, 15), (19, 9, 3, 9),
              (23, 6, 3, 15), (15, 15, 10, 10)]
mouse_over = MouseOver(rectangles)

print(mouse_over.find_rectangle(3, 18))
