
# Monkey Banana Problem

monkey_position = "door"
box_position = "window"
banana_position = "center"
monkey_on_box = False
has_banana = False

print("Initial Monkey Position:", monkey_position)
print("Box Position:", box_position)
print("Banana Position:", banana_position)

# Step 1: Monkey moves to the box
monkey_position = box_position
print("\nMonkey moves to the box.")

# Step 2: Monkey pushes the box under the banana
box_position = banana_position
monkey_position = banana_position
print("Monkey pushes the box under the banana.")

# Step 3: Monkey climbs onto the box
monkey_on_box = True
print("Monkey climbs onto the box.")

# Step 4: Monkey grabs the banana
if monkey_position == banana_position and monkey_on_box:
    has_banana = True
    print("Monkey grabs the banana!")

# Check goal state
if has_banana:
    print("Goal State Achieved: Monkey has the banana.")
else:
    print("Goal State Not Achieved.")
