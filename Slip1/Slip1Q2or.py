
class ModelBasedAgent:
    def __init__(self):
        self.memory = {}

    def perceive(self, room, status):
        print("\nCurrent Room:", room)
        print("Current Perception:", status)

        # Update internal state (memory)
        self.memory[room] = status

        # Decide action using current perception and memory
        if self.memory[room] == "Dirty":
            action = "Clean the room"
        else:
            action = "Move to next room"

        print("Action:", action)
        print("Internal State:", self.memory)


agent = ModelBasedAgent()

agent.perceive("Room A", "Dirty")
agent.perceive("Room B", "Clean")
agent.perceive("Room A", "Clean")
