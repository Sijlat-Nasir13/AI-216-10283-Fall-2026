age = 19
programming_score = 72
prerequisite_completed = True

print(f"Applicant Details: Age={age}, Score={programming_score}, Prereq={prerequisite_completed}")

if age >= 18 and programming_score >= 60 and prerequisite_completed:
    print("Status: Eligible")
else:
    print("Status: Not eligible")
    if age < 18:
        print("- Age requirement not met")
    if programming_score < 60:
        print("- Programming score requirement not met")
    if not prerequisite_completed:
        print("- Prerequisite course not completed")