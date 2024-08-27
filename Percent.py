number = 90
total = 100

# Calculate the percentage
percentage = (number / total) * 100

# Use elif to check the percentage
if percentage >= 90:
    print("Excellent")
elif percentage >= 70:
    print("Good")
elif percentage >= 50:
    print("Average")
else:
    print("Needs Improvement")
