# Number of test cases
T = int(input())

for _ in range(T):
    # Reading X and Y for each test case
    X, Y = map(int, input().split())
    
    # Check if renting is beneficial
    if X >= Y:
        # If renting is not beneficial, output 0
        print(0)
    else:
        # Calculate the maximum number of months Chef can rent
        print((Y // X) - 1)
