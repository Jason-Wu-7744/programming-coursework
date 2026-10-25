# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
def tax(income):
    pension = 0.08*income
    medical = 0.02*income
    unemployment = 0.01*income
    house = 0.07*income
    insurance_fund = pension + medical + unemployment + house
    bottomline = 5000
    taxbase = income - insurance_fund - bottomline
    if income <= 36000/12:
        rate = 0.03
        back = 0/12
    elif income <= 144000/12:
        rate = 0.1
        back = 2520/12
    elif income <= 300000/12:
        rate = 0.2
        back = 16920/12
    elif income <= 420000/12:
        rate = 0.25
        back = 31920/12
    elif income <= 660000/12:
        rate = 0.3
        back = 52920/12
    elif income <= 960000/12:
        rate = 0.35
        back = 89520/12
    else:
        rate = 0.45
        back = 181920/12
    tax_initial = taxbase*rate - back
    if tax_initial < 0:
        tax_initial = 0
    return tax_initial

print("月薪为7800时，每月缴税"+str(tax(7800))+"元，每月到手工资"+str(7800-tax(7800))+"元")
#起初算得的个税为负，可能是对于个税扣除机制理解不到位，需要再加一个if语句以确保个税为正或0
print("月薪为9800时，每月缴税"+str(tax(9800))+"元，每月到手工资"+str(9800-tax(9800))+"元")
print("月薪为32000时，每月缴税"+str(tax(32000))+"元，每月到手工资"+str(32000-tax(32000))+"元")
print("月薪为56000时，每月缴税"+str(tax(56000))+"元，每月到手工资"+str(56000-tax(56000))+"元")
