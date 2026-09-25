# Task 4: Exception Handling and Input Validation

def calculate_percentage(obtained, total):
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative.")
    if obtained > total:
        raise ValueError("Obtained marks cannot exceed total marks.")
    
    return (obtained / total) * 100.0


def run_percentage_calculator(obtained_raw, total_raw):
    print(f"\nTesting Input: obtained={obtained_raw}, total={total_raw}")
    try:
        obtained = float(obtained_raw)
        total = float(total_raw)
        percentage = calculate_percentage(obtained, total)
    except ValueError as error:
        print(f"Validation Error: {error}")
    else:
        print(f"Calculated Percentage: {percentage:.2f}%")
    finally:
        print("Calculation attempt finished.")


if __name__ == "__main__":
    # Standard required test cases
    test_cases = [
        (80, 100),    # Valid
        (-5, 100),    # Negative obtained
        (120, 100),   # Obtained > total
        (80, 0),      # Total = 0
        ("abc", 100)  # Non-numeric
    ]
    
    for obt, tot in test_cases:
        run_percentage_calculator(obt, tot)