# Task 3: Temperature Monitoring

temperatures = [21.5, 29.0, 32.5, 18.0, 35.2, 27.8, 14.0]

below_normal_count = 0
normal_count = 0
high_count = 0

for temp in temperatures:
    if temp < 15.0:
        category = "Below Normal"
        below_normal_count += 1
    elif 15.0 <= temp <= 30.0:
        category = "Normal"
        normal_count += 1
    else:
        category = "High"
        high_count += 1
    print(f"Temperature: {temp}°C -> Category: {category}")

print("\nSummary")
print(f"Below Normal: {below_normal_count}")
print(f"Normal: {normal_count}")
print(f"High: {high_count}")