
# Monkey Banana Problem

monkey = "door"
banana = "center"
box = "window"
has_banana = False

print("Initial monkey position:", monkey)
print("Banana position:", banana)
print("Box position:", box)

# Move monkey to the box
print("\nMonkey moves from", monkey, "to", box)
monkey = box

# Push the box to the banana
if monkey == box:
    print("Monkey pushes the box to", banana)
    box = banana
    monkey = banana

# Climb onto the box
if monkey == banana and box == banana:
    print("Monkey climbs onto the box")

    # Grab the banana
    has_banana = True
    print("Monkey grabs the banana")

# Check goal state
if has_banana:
    print("\nGoal achieved! Monkey got the banana.")
else:
    print("\nGoal not achieved.")
