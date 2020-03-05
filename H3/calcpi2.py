# Here's another way of approximating Pi, using the Madhava-Leibniz formula:
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
#
# Notice how the signs alternate between + and - for each term of this series.
# Write a program which reads num_terms as an int, then computes the above approximation of Pi/4 by summing the first num_terms of this series.
# Then multiply by 4 and print out the resulting approximate calculated value of Pi as well the error: the absolute value of its difference with math.pi.
#
# Hint: use a loop for count in range(num_terms): initialize sign=-1.0 followed by a loop body that calculates
# sign=-sign and then term = sign / (2*count + 1) for count=0,1,2... Accumulate the sum of these terms,
# using the accumulator pattern with a variable pi_estimate, then calculate and print 4*pi_estimate and its error.

num_terms = input('Enter num_terms')

sign = -1.0
temp = 0
for count in range(int(num_terms)):
    print(int(num_terms))
    sign = -sign
    term = temp + (sign / (2*count + 1))
    print(term)
    temp = term
pi_estimate = 4*temp
print(pi_estimate)

'''
/Users/a6003261/Documents/class/pythonProjects/venv/bin/python /Users/a6003261/Documents/class/pythonProjects/H3/calcpi2.py
Enter num_terms3
3
1.0
3
0.6666666666666667
3
0.8666666666666667
3.466666666666667

Process finished with exit code 0
'''
