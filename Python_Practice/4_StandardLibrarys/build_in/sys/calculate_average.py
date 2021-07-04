import sys


len_ = len(sys.argv)

if len_ <= 1:
    print('No arguments given')
else:
    print(f'Average: {sum(map(int, sys.argv[1:])) / (len(sys.argv) - 1):.4f}')
    