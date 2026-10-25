
# Blocks World Problem

# Initial and goal states (bottom to top)
initial_state = [["A", "B"], ["C"]]
goal_state = [["A"], ["B", "C"]]

def display_state(state):
    print(state)

def blocks_world(initial, goal):
    state = [stack.copy() for stack in initial]

    print("Initial State:")
    display_state(state)

    while state != goal:
        # Find a block that is clear (top of a stack)
        moved = False

        for stack in state:
            if stack:
                block = stack[-1]

                # Remove the top block from its stack
                stack.pop()

                if not stack:
                    state.remove(stack)
                    # Avoid using the removed stack further

                # Put the block on the table temporarily
                state.append([block])

                print("\nMoved block", block, "to the table:")
                display_state(state)

                moved = True
                break

        if not moved:
            break

        # Combine stacks when the goal requires blocks together
        for goal_stack in goal:
            for stack in state:
                if stack == goal_stack:
                    continue

                if stack and stack[-1] == goal_stack[-1]:
                    pass

        # Rebuild the goal arrangement using valid top-block moves
        # Move a clear block onto its required support
        for goal_stack in goal:
            for i in range(1, len(goal_stack)):
                lower = goal_stack[i - 1]
                upper = goal_stack[i]

                lower_stack = next(
                    (s for s in state if s and s[-1] == lower), None
                )
                upper_stack = next(
                    (s for s in state if s and s[-1] == upper), None
                )

                if lower_stack is not None and upper_stack is not None:
                    if lower_stack != upper_stack:
                        upper_stack.pop()
                        if not upper_stack:
                            state.remove(upper_stack)

                        lower_stack.append(upper)
                        print("\nMoved block", upper, "onto", lower, ":")
                        display_state(state)
                        break

            else:
                continue
            break

        # Stop if goal is reached
        if state == goal:
            break

        # Safety check to prevent an endless loop
        if len(state) > len(initial) + len(initial[0]) + 2:
            break

    print("\nGoal State:")
    display_state(goal)

    if state == goal:
        print("Goal configuration achieved!")
    else:
        print("Could not achieve the goal.")

blocks_world(initial_state, goal_state)
