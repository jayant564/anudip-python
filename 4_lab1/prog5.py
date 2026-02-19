# Loan Approval System 
# Loan approval depends on: 
# • Credit score 
# • Monthly income 
# • Existing loan amount 
# Rules: 
# • Credit score < 600 → Reject 
# • 600–750 → Further check income 
# • 750 → Approve 
# If income < ₹30,000 and existing loans > ₹5,00,000 → Reject. 
credit_score = int(input("Enter credit score: "))
income = float(input("Enter monthly income: "))
existing_loan = float(input("Enter existing loan amount: "))

if credit_score < 600:
    print("Loan Rejected: Low credit score")
elif credit_score >= 750:
    print("Loan Approved")
else:
    # credit score between 600 and 749
    if income < 30000 and existing_loan > 500000:
        print("Loan Rejected: Low income and high existing loan")
    else:
        print("Loan Approved")
