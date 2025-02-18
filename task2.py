def fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    return fib_sequence

# Input: Number of terms in the Fibonacci sequence
num_terms = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    print(fibonacci(num_terms))