#--My Fisrt FinTech App

account_balance = 2400.50
withdrawal_request = 1500.50

print("Processing Transaction...!")
if withdrawal_request > account_balance:
    print("Withdrawal denied: Insurficient fund.")
else:
    print("Withdrawal Approved: Please take your cash.")


