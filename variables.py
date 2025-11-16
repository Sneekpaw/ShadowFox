# Day 1: Variables tasks

# Task 1: pi variable
pi = 22 / 7
print("Task 1 - value of pi:", pi)
print("Task 1 - type of pi:", type(pi))

print("\n" + "="*40 + "\n")

# Task 2: reserved keyword demonstration
print("Task 2 - reserved word example:")
try:
    # we cannot use 'for' as a variable name; so demonstrate via eval to show error
    code_try = "for = 4"
    eval(code_try)
except Exception as e:
    print("Using 'for' as a variable name causes a SyntaxError or similar:")
    print(type(e).__name__, ":", e)

print("\n" + "="*40 + "\n")

# Task 3: Simple Interest calculation
P = 10000   # principal (change to test)
R = 5       # rate percent per year
T = 3       # time in years

SI = (P * R * T) / 100
total_amount = P + SI

print("Task 3 - Simple Interest =", SI)
print("Task 3 - Total Amount (P + SI) =", total_amount)