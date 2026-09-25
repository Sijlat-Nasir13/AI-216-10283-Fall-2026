def calculate_percentage(obtained, total):
    if total == 0:
        return 0.0
    return (obtained / total) * 100.0


def is_passing(score, passing_score):
    return score >= passing_score


choice = ""
while choice != "3":
    print("\nMenu")
    print("1. Check pass/fail")
    print("2. Calculate percentage")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        s = float(input("Enter student score: "))
        p = float(input("Enter passing score: "))
        if is_passing(s, p):
            print("Result: PASS")
        else:
            print("Result: FAIL")
    elif choice == "2":
        obt = float(input("Enter obtained marks: "))
        tot = float(input("Enter total marks: "))
        pct = calculate_percentage(obt, tot)
        print(f"Calculated Percentage: {pct:.2f}%")
    elif choice == "3":
        print("Exiting program. Goodbye!")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")