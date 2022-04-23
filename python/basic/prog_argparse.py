import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
#parser.add_argument("echo", help="echo the string you use here")
#parser.add_argument("square", help="display a square of a given number", type=int)
#parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
#parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int)
#parser.add_argument("-v", "--verbose", help="increase output verbosity", type=int, choices=[0,1,2])
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("y", help="the exponent", type=int)
parser.add_argument("x", help="the base", type=int)
#parser.add_argument("-v", "--verbose", help="increase output verbosity", action="count", default=0)

args = parser.parse_args()

#answer = args.square**2
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))