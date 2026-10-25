
# Model-Based Agent for Smart Traffic Signal Control

previous_density = 0

current_density = int(input("Enter current traffic density (0-100): "))

print("Previous Traffic Density:", previous_density)
print("Current Traffic Density:", current_density)

if current_density < 0 or current_density > 100:
    print("Invalid traffic density!")
else:
    if current_density > previous_density:
        print("Traffic is increasing.")
    elif current_density < previous_density:
        print("Traffic is decreasing.")
    else:
        print("Traffic is stable.")

    if current_density >= 70:
        print("Signal Status: GREEN - High traffic priority")
    elif current_density >= 40:
        print("Signal Status: GREEN - Medium traffic priority")
    else:
        print("Signal Status: RED - Low traffic priority")

    previous_density = current_density
    print("Updated Previous Density:", previous_density)
