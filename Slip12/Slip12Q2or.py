
location = input("Enter current location (A/B): ").upper()
status = input("Enter room status (Clean/Dirty): ").capitalize()

if location not in ["A", "B"]:
    print("Invalid location!")
elif status not in ["Clean", "Dirty"]:
    print("Invalid room status!")
elif status == "Dirty":
    print("Action: Clean the room")
elif location == "A":
    print("Action: Move to location B")
else:
    print("Action: Move to location A")
