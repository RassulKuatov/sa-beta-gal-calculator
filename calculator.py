def calculate_senescence():
    print("=== SA-beta-gal Senescence Index Calculator ===")
    
    try:
        fov_count = int(input("How many fields of view (FOV) did you count?: "))
        if fov_count <= 0:
            print("Error: Number of FOVs must be greater than 0.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    total_blue = 0
    total_cells = 0

    for i in range(1, fov_count + 1):
        print(f"\nData for FOV #{i}:")
        try:
            blue = int(input("  SA-beta-gal positive (blue) cells: "))
            normal = int(input("  Healthy (unstained) cells: "))
            
            if blue < 0 or normal < 0:
                print("  Warning: Cell counts cannot be negative. Skipping this FOV.")
                continue
                
            total_blue += blue
            total_cells += (blue + normal)
        except ValueError:
            print("  Warning: Invalid entry. Skipping this FOV.")
            continue

    if total_cells > 0:
        percentage = (total_blue / total_cells) * 100
        print("\n" + "="*40)
        print(f"Total cells counted: {total_cells}")
        print(f"Senescent (blue) cells: {total_blue}")
        print(f"Average senescence index: {round(percentage, 2)}%")

        # Biological Interpretation Thresholds
        if percentage >= 60:
            print("Result: Culture shows pronounced senescence/SASP.")
        elif percentage >= 20:
            print("Result: Early/moderate senescence stage.")
        else:
            print("Result: Culture is young/proliferating.")
        print("="*40)
    else:
        print("\nError: No valid data entered.")

if __name__ == "__main__":
    calculate_senescence()
