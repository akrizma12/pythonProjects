# The Python program trace_me.py is posted next to this handout on Canvas.
# Download it and add to your project for this assignment. Set breakpoints on the two print("set...") statements in this program.
# Run your program in the PyCharm debugger and enter 5 for the first input, then the values 1.0, -2.0, 3.0, -4.0, 5.0 for the five subsequent inputs.
# When your program stops at each breakpoint, write down the values of a, b, c, d, and e.
# Then resume until the next breakpoint is encountered.  Finally, add comments (lines starting with #)
# at the end of the program which lists the five sets of such breakpoint values,
# followed by the values for the final breakpoint.  Your program should thus end with a comment
# that lists six total sets of the values for a, b, c, d, and e.  Submit your code with these comments as your delivery for this problem.
# Figure out what this program does, then rename the variables to better reflect its meaning.
# You are refactoring the program: changing its structure to improve readability, but not changing its behavior.
# Resubmit this version of the code to Canvas.
# Unfortunately, the given code doesn't always compute the correct values for all input data. Why? Discuss in class how to fix this.

#
# H3-5: run the following in the PyCharm debugger and print
#       the following requested info...

num = int(input("enter number of floats: "))

a = 0.0
b = 0.0
c = 0.0

for d in range(num):
    e = float(input("enter next float: "))
    a = max(a, e)
    b = min(b, e)
    c = c + e
    print("set breakpoint here...")
    # LOCATION 1:
    # list values of a, b, c, d, e at this point, each time through loop

print(a)
print(b)
print(c / num)

print("set another breakpoint here...")
# LOCATION 2:
# list final values of a, b, c, d, e
