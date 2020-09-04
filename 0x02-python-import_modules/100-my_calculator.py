#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

        a = int(argv[1])
        oper = argv[2]
        b = int(argv[3])
        result = 0

        if oper == '+':
            result = add(a, b)
        elif oper == '-':
            result = sub(a, b)
        elif oper == '*':
            result = mul(a, b)
        elif oper == '/':
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

            print("{:d} {} {:d} = {:d}".format(a, oper, b, result))
