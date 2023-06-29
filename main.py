# Abdullah Mutaz Alshawa
import argparse
import numpy as np
print("Please note that to use * and ** single quotes must surround the operator.")
print("For example, python main.py '**' 2.0 2.0 will return 4.0 which is 2^2.")
parser = argparse.ArgumentParser()
parser.add_argument("operation", help="Operation to perform (+, -, *, /, %, **)")
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
elif args.operation == '**':
    result = np.power(args.num1, args.num2)
elif args.operation == '//':
    result = args.num1 // args.num2
else:
    raise ValueError("Invalid operation")

print(result)
print("Thanks, goodbye")
