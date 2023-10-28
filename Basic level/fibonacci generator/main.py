import sys

def main():
    # Initialize the Fibonacci sequence with the first two terms
    fibo_seq = [0, 1]

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python/python3 main.py <n>")
        sys.exit(1)

    try:
        # Convert the command-line argument to an integer
        n = int(sys.argv[1])

        # Check if n is a positive integer
        if n <= 0:
            raise ValueError()

    except ValueError:
        # Handle the case where the provided value for n is not a valid positive integer
        print("Error: Please provide a valid positive integer for n.")
        sys.exit(1)

    # Generate the Fibonacci sequence up to the required number of terms
    while len(fibo_seq) < n:
        next_term = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_term)

    # Print the generated Fibonacci sequence
    print(' '.join(str(item) for item in fibo_seq[:n]))

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
