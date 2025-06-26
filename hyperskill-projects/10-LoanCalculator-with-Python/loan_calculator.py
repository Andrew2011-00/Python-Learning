import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--interest", type=float)
parser.add_argument("--periods", type=float)
parser.add_argument("--type", type=str)

args = parser.parse_args()

parameters = [args.principal, args.payment, args.interest, args.periods]
if args.type not in ["annuity", "diff"]:
    print("Incorrect parameters")
    exit()

if args.interest is None or args.interest <= 0:
    print("Incorrect parameters")
    exit()

if any(x is not None and x < 0 for x in parameters):
    print("Incorrect parameters")
    exit()

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    exit()

interest = args.interest / 1200

if args.type == "annuity":
    if args.payment is None:
        payments = args.principal * interest * ((1 + interest) ** args.periods) / ((1 + interest) ** args.periods - 1)
        print(f"Your monthly payment = {math.ceil(payments)}!")
        print(f"Overpayment = {math.ceil(payments) * args.periods - math.floor(args.principal)}")
    elif args.principal is None:
        loan = args.payment / (interest * ((1 + interest) ** args.periods) / ((1 + interest) ** args.periods - 1) )
        print(f"Your loan principal = {math.floor(loan)}!")
        print(f"Overpayment = {int(args.payment * args.periods - math.floor(loan))}")

    elif args.periods is None:
        period = math.log(args.payment / (args.payment - (interest * args.principal)), 1 + interest)
        years = int(period / 12)
        months = int(math.ceil(period % 12))
        if months == 12:
            print(f"It will take {years + 1} years to repay this loan!")
        elif period < 12:
            print(f"It will take {math.ceil(period)} months to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")

        print(f"Overpayment = {int(math.ceil(period) * args.payment - args.principal)}")
    else:
        print("Incorrect parameters")
elif args.type == "diff":
    if args.principal is None or args.periods is None:
        print("Incorrect parameters")
    else:
        total_payment = 0
        for month in range(1, int(args.periods)+1):
            diff_payment = (args.principal / args.periods) + (interest * (args.principal - (args.principal * (month - 1) / args.periods)))
            diff_payment = math.ceil(diff_payment)
            total_payment += diff_payment
            print(f"Month {month}: payment is {diff_payment}")
        print(f"Overpayment = {int(total_payment - args.principal)}")


else:
    print("Incorrect parameters")