# skip_counter.py

# Even numbers from 0 to 20 (stop index must be 21 to include 20)
print("Even numbers:")
for number in range(0, 21, 2):
    print(number)

print("\nCountdown:")
# Countdown from 10 to 0 (stop index must be -1 to include 0)
for count in range(10, -1, -1):
    print(count)