# 💸 Loan Calculator

This is a simple command-line Loan Calculator built as part of my Python learning journey on [Hyperskill](https://hyperskill.org). The program calculates different aspects of a loan based on user input, using arguments passed through the terminal.

## 🧠 What It Does

The calculator can compute:

- Annuity monthly payments
- Loan principal
- Number of periods needed to repay a loan
- Differentiated payments

## ⚙️ How to Use

You run the program using `argparse` to specify the required parameters. Example usage:

```bash
python loan_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```
Supported arguments:

- --type: "annuity" or "diff" (for differentiated)

- --payment: Monthly payment amount (used with "annuity")

- --principal: Loan principal

- --periods: Number of months

- --interest: Interest rate (required for all types)
  
⚠️ Interest is required for all calculations.
⚠️ You can’t mix diff with --payment.

## 🧪 Example Output
```bash
It will take 10 years to repay this loan!
Overpayment = 146640
```
## 📌 What I Learned

- How to use the argparse module for parsing command-line arguments.

- Logical structure for financial calculations.

- Error handling and input validation for user-friendly programs.

## 💬 Notes
I found the logic relatively straightforward, but setting up and handling argparse took some getting used to. Once I understood how to structure the conditions and parse the arguments correctly, the rest came together smoothly.

















