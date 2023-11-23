import sys

input_value = int(sys.stdin.readline())

for _ in range(input_value):
    A, B = map(int, sys.stdin.readline().split())

    print(A+B)