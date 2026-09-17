# loop_hospital.py

print("--- Patient 1 ---")
# FIXED: range(1, 10) stops at 9 because the stop bound is exclusive. Changed to range(1, 11) to include 10.
for i in range(1, 11):
    print(i)


print("\n--- Patient 2 ---")
n = 3
# FIXED: 'n' was never decremented, causing an infinite loop. Added 'n -= 1' inside the loop body.
while n > 0:
    print(n)
    n -= 1


print("\n--- Patient 3 ---")
# FIXED: 'total' was re-initialized to 0 inside the loop on every iteration. Moved 'total = 0' outside the loop.
total = 0
for i in range(1, 6):
    total = total + i
print(f"Total: {total}")