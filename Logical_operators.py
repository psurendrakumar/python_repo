has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")


has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")



has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")


has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Customer Eligible for Loan")
else:
    print("Customer Not Eligible for Loan")