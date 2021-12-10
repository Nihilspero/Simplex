from pulp import *
def simplexup(vr,rs,nums,integer=1):
    f=[0]*5
    r=[[0] * 5 for _ in range(5)]
    rzap=nums[vr:-rs]
    for i in range(vr): #Считываем коэфициенты для функции
        f[i]=nums[i]
    u=0 #Считываем коэфициенты для системы ограничений
    for i in range(rs):
        for j in range(vr):
            r[i][j]=rzap[u]
            u+=1
    ra=nums[-rs:]
    while len(ra) <5:
        ra.append(0)
    if integer:
        x1 = pulp.LpVariable("x1", lowBound=0,cat='Integer') #Oбъявления with integer"
        x2 = pulp.LpVariable("x2", lowBound=0,cat='Integer')
        x3 = pulp.LpVariable("x3", lowBound=0,cat='Integer')
        x4 = pulp.LpVariable("x4", lowBound=0,cat='Integer')
        x5 = pulp.LpVariable("x5", lowBound=0,cat='Integer')
    else:
        x1 = pulp.LpVariable("x1", lowBound=0)  # Oбъявления without integer
        x2 = pulp.LpVariable("x2", lowBound=0)
        x3 = pulp.LpVariable("x3", lowBound=0)
        x4 = pulp.LpVariable("x4", lowBound=0)
        x5 = pulp.LpVariable("x5", lowBound=0)
    problem = pulp.LpProblem('0', LpMaximize)
    problem += f[0]*x1 + f[1]*x2 + f[2]*x3 + f[3]*x4 + f[4]*x5, "Функция цели"
    problem += r[0][0]*x1 + r[0][1]*x2 + r[0][2]*x3 +r[0][3]*x4 + r[0][4]*x5 <= ra[0], "1"
    problem += r[1][0]*x1 + r[1][1]*x2 + r[1][2]*x3 +r[1][3]*x4 + r[1][4]*x5 <= ra[1], "2"
    problem += r[2][0]*x1 + r[2][1]*x2 + r[2][2]*x3 +r[2][3]*x4 + r[2][4]*x5 <= ra[2], "3"
    problem += r[3][0]*x1 + r[3][1]*x2 + r[3][2]*x3 +r[3][3]*x4 + r[3][4]*x5 <= ra[3], "4"
    problem += r[4][0]*x1 + r[4][1]*x2 + r[4][2]*x3 +r[4][3]*x4 + r[4][4]*x5 <= ra[4], "5"#'Задаем ограничения'
    problem.solve()
    answers={}
    for variable in problem.variables():
        answers[variable.name] = round(variable.varValue, 2)
    answers['Profit:'] = round(value(problem.objective), 2)
    return answers
def simplexdown(vr,rs,nums,integer):
    f=[0]*5
    r=[[0] * 5 for _ in range(5)]
    rzap=nums[vr:-rs]
    for i in range(vr): #Считываем коэфициенты для функции
        f[i]=nums[i]
    u=0 #Считываем коэфициенты для системы ограничений
    for i in range(rs):
        for j in range(vr):
            r[i][j]=rzap[u]
            u+=1
    ra=nums[-rs:]
    while len(ra) <5:
        ra.append(0)
    if integer:
        x1 = pulp.LpVariable("x1", lowBound=0, cat='Integer')  # Oбъявления with integer"
        x2 = pulp.LpVariable("x2", lowBound=0, cat='Integer')
        x3 = pulp.LpVariable("x3", lowBound=0, cat='Integer')
        x4 = pulp.LpVariable("x4", lowBound=0, cat='Integer')
        x5 = pulp.LpVariable("x5", lowBound=0, cat='Integer')
    else:
        x1 = pulp.LpVariable("x1", lowBound=0)  # Oбъявления without integer
        x2 = pulp.LpVariable("x2", lowBound=0)
        x3 = pulp.LpVariable("x3", lowBound=0)
        x4 = pulp.LpVariable("x4", lowBound=0)
        x5 = pulp.LpVariable("x5", lowBound=0)
    problem = pulp.LpProblem('0', LpMinimize)
    problem += f[0]*x1 + f[1]*x2 + f[2]*x3 + f[3]*x4 + f[4]*x5, "Функция цели"
    problem += r[0][0]*x1 + r[0][1]*x2 + r[0][2]*x3 +r[0][3]*x4 + r[0][4]*x5 >= ra[0], "1"
    problem += r[1][0]*x1 + r[1][1]*x2 + r[1][2]*x3 +r[1][3]*x4 + r[1][4]*x5 >= ra[1], "2"
    problem += r[2][0]*x1 + r[2][1]*x2 + r[2][2]*x3 +r[2][3]*x4 + r[2][4]*x5 >= ra[2], "3"
    problem += r[3][0]*x1 + r[3][1]*x2 + r[3][2]*x3 +r[3][3]*x4 + r[3][4]*x5 >= ra[3], "4"
    problem += r[4][0]*x1 + r[4][1]*x2 + r[4][2]*x3 +r[4][3]*x4 + r[4][4]*x5 >= ra[4], "5"#'Задаем ограничения'
    problem.solve()
    answers={}
    for variable in problem.variables():
        answers[variable.name] = round(variable.varValue, 2)
    answers['Profit:'] = round(value(problem.objective), 2)
    return answers

