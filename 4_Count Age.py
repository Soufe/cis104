from datetime import datetime

def calculate_age(dob, calc_date):
    dob_date = datetime.strptime(dob, '%d/%m/%Y')
    calc_date = datetime.strptime(calc_date, '%d/%m/%Y')
    delta = calc_date - dob_date
    years = delta.days // 365
    remaining_days = delta.days % 365
    months = remaining_days // 30

    return f"{years} years {months} months"

#input
dob = input().strip()
calc_date = input().strip()

#output
age_result = calculate_age(dob, calc_date)
print(age_result)