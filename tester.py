# This file just compares user's output files with 
# the given outputs. No terminal output means you did 
# great.

import os

my_commands = ["Make transaction", "Make account", "Make bank"]


for i in my_commands:
    if i == "Make transaction":
        os.system(i)
        os.system("Make run > out_for_trs.txt")
        os.system("diff out_for_trs.txt example_transaction.txt")

    if i == "Make account":
        os.system(i)
        os.system("Make run > out_for_acc.txt")
        os.system("diff out_for_acc.txt example_account.txt")

    if i == "Make bank":
        os.system(i)
        os.system("Make run > out_for_bank.txt") 
        os.system("diff out_for_bank.txt example_bank.txt")\

