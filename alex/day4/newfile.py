class Cat:
    def __init__(self, x_value, speed, color):
        self.x = x_value
        self.speed = speed
        self.color = color

    def move(self):
        self.x = self.x + self.speed


cat1 = Cat(0, 2, "Orange")
cat2 = Cat(4, 5, "Black")

cat1.move()
cat2.move()

print(cat1.x, cat2.x)
