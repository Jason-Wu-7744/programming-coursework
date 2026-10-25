# Student coursework archive. Public maintainer: Jason.
# Prescribed course exercises; numerical algorithms retained from the source archive.
for carpentry_wage in range(60, 81):
    for electrician_wage in range(60, 81):
        for painter_wage in range(60, 81):
            # print(carpentry_wage, electrician_wage, painter_wage)
            if 8*carpentry_wage == 1*electrician_wage + 6*painter_wage and 5*electrician_wage == 4*carpentry_wage + 1*painter_wage and 7*painter_wage == 4*carpentry_wage + 4*electrician_wage:
                print("木工工资"+str(carpentry_wage)+"元，电工工资"+str(electrician_wage)+"元，油漆工工资"+str(painter_wage)+"元")