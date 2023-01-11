# Let's write some code for multinomial theorem, a topic heavily talked about in MATH 3012: Applied Combinatorics at Georgia Tech >_>

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def multinomial(n, k):
    result = factorial(n)
    for i in range(len(k)):
        result /= factorial(k[i])
    return int(result)

# This function takes two inputs, n and k where n is the exponent of the sum, and k is a list of exponents of the terms.
# It first defines a helper function factorial that calculates the factorial of an input number n.
# Then it defines the main function multinomial that calculates the multinomial coefficient.
# It starts by finding the factorial of n and assigns the result to result.
# Then, it iterates over the exponents in the list k, and for each exponent, it divides result by the factorial of the exponent. The division will yield the result of the multinomial coefficient.
# Finally, it returns the result which is the multinomial coefficient for the input.
