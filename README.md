# Week 6 Assignment: Times Tables, Skip Counting & Loop Hospital

## Files Included
- `times_table.py`: Takes a user input and displays its multiplication table from 1 to 10 using `range(1, 11)`.
- `skip_counter.py`: Demonstrates step values in `range()` by generating even numbers from 0 to 20 and counting down from 10 to 0.
- `loop_hospital.py`: Debugs three broken loops involving off-by-one errors, infinite loops, and misplaced accumulators.
- `screenshots/`: Folder containing screenshots of each program output.

## Reflection
An **off-by-one error** occurs when an iterative loop executes one time too many or one time too few, typically caused by misunderstanding whether boundary indices are inclusive or exclusive. In Python, a reliable habit to avoid off-by-one errors with `range(start, stop)` is remembering that `stop` is **exclusive**—if you want to include a specific target end number `N`, always pass `N + 1` as the `stop` argument.