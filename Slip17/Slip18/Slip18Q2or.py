
# Intelligent Agent: Perception -> Decision -> Action

environment = input("Enter environment status (Clean/Dirty): ").lower()

# 1. Perception
print("\n1. PERCEPTION")
print("Agent perceives the environment:", environment)

# 2. Decision
print("\n2. DECISION")
if environment == "dirty":
    action = "Clean the environment"
elif environment == "clean":
    action = "Do nothing"
else:
    action = "Invalid environment status"

print("Agent decides to:", action)

# 3. Action
print("\n3. ACTION")
if environment == "dirty":
    print("Agent is cleaning the environment.")
    print("Environment is now clean.")
elif environment == "clean":
    print("Environment is already clean.")
else:
    print("Please enter Clean or Dirty.")
