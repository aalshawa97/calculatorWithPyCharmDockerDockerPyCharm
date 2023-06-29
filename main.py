#Abdullah Mutaz Alshawa
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="Operation to perform (+,-,*,/, %)")
parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
args = parser.parse_args()

if args.operation == '+':
    result = np.add(args.num1, args.num2)
elif args.operation == '-':
    result = np.subtract(args.num1, args.num2)
elif args.operation == '*':
    result = np.multiply(args.num1, args.num2)
elif args.operation == '/':
    result = np.divide(args.num1, args.num2)
elif args.operation == '%':
    result = args.num1 % args.num2
else:
    raise ValueError("Invalid operation")

print(result)
