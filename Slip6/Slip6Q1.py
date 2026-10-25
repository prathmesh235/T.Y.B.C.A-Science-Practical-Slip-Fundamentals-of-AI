
# Hill Climbing Algorithm

def hill_climbing(start):
    current = start

    while True:
        current_value = -(current - 3) ** 2 + 9

        left = current - 1
        right = current + 1

        left_value = -(left - 3) ** 2 + 9
        right_value = -(right - 3) ** 2 + 9

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, -(current - 3) ** 2 + 9


start = 0
best_position, best_value = hill_climbing(start)

print("Starting Position:", start)
print("Best Position:", best_position)
print("Maximum Value:", best_value)
