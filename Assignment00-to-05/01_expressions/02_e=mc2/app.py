# Function to calculate energy using E = m * c^2
def calculate_energy(mass: float) -> float:
    SPEED_OF_LIGHT = 299_792_458  # Speed of light in meters per second
    return mass * (SPEED_OF_LIGHT ** 2)

# Main function that runs the program
def main() -> None:
    print("🔢 Mass to Energy Calculator (E = mc²)\n")
    
    try:
        # Get mass input from user
        user_input = input("Enter mass in kilograms (kg): ")
        mass = float(user_input)

        # Calculate energy
        energy = calculate_energy(mass)

        # Show results
        print("\n📄 Result:")
        print(f"Mass (m): {mass} kg")
        print(f"Speed of Light (c): 299,792,458 m/s")
        print(f"Energy (E): {energy:.2f} joules")
        
    except ValueError:
        print("\n⚠️ Please enter a valid number (like 12.5 or 50).")

# Run the program
if __name__ == "__main__":
    main()
