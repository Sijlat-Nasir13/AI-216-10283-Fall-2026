# Problem: Classify electricity consumption data into usage tiers and compute total distribution.
# Inputs: daily_usage_kwh list containing float readings in kWh.
# Rules: Low < 5.0, Normal 5.0 <= usage <= 10.0, High > 10.0.
# Repetition: Iterate over every reading using a for-loop, incrementing category counters.
# Outputs: Formatted summary counts and percentages with 2 decimal places.

daily_usage_kwh = [3.2, 5.0, 7.5, 10.0, 12.4, 4.9, 10.1]

low_count = 0
normal_count = 0
high_count = 0
total_readings = len(daily_usage_kwh)

for usage in daily_usage_kwh:
    if usage < 5.0:
        low_count += 1
    elif 5.0 <= usage <= 10.0:
        normal_count += 1
    else:
        high_count += 1

low_pct = (low_count / total_readings) * 100
normal_pct = (normal_count / total_readings) * 100
high_pct = (high_count / total_readings) * 100

print(f"Low: {low_count} ({low_pct:.2f}%)")
print(f"Normal: {normal_count} ({normal_pct:.2f}%)")
print(f"High: {high_count} ({high_pct:.2f}%)")