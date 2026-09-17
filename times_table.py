# times_table.py

# Prompt the user for a number
number = int(input("Enter a number to generate its times table: "))

print(f"\n--- Times Table for {number} ---")
# range(1, 11) runs from 1 to 10 inclusive
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")