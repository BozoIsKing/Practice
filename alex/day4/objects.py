cat_x = 0
cat_speed = 2

cat1 = [8, 4, 5]
cat2 = [4, 2, 1]
cats = [cat1, cat2]

for i in range(50):
    cat_x = cat_x + cat_speed
    cat_speed = cat_x // 2
    print(f"The cat's position is {cat_x} and its speed is {cat_speed}")