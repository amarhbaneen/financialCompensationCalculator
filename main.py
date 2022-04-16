import math
import pandas as pd
from datetime import datetime


class employee:
    def __init__(self, firstName, lastName, gender, birthDate, worBegin, salary,
                 law14Date, propertyValue, deposits, workLeave, propertyPayment, checkComplet, leaveReason, law14per):
        self.compensation = 0

        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.age = 2020 - datetime.strptime(birthDate, '%Y-%m-%d').year
        self.seniority = (datetime.strptime('2021-12-31', '%Y-%m-%d').year - datetime.strptime(worBegin,
                                                                                               '%Y-%m-%d').year) / 365.25
        self.salary = float(salary)
        if type(law14Date) != float:
            self.law14date = datetime.strptime(law14Date, '%Y-%m-%d')
        else:
            self.law14date = None

        if type(workLeave) != float:
            if workLeave == '-':
                self.workleave = None
            else:
                self.workleave = datetime.strptime(workLeave, '%Y-%m-%d %H:%M:%S')
        else:
            self.workleave = None

        try:
            self.propertyValue = float(propertyValue)
            if pd.isna(self.propertyValue):
                self.propertyValue = 0
        except:
            self.propertyValue = 0
        try:
            self.deposits = float(deposits)
            if pd.isna(self.deposits):
                self.deposits = 0
        except:
            self.deposits = 0
        try:
            self.checkComplet = float(checkComplet)
            if pd.isna(self.checkComplet):
                self.checkComplet = 0
        except:
            self.checkComplet = 0
        try:
            self.propertyPayment = float(propertyPayment)
            if pd.isna(self.propertyPayment):
                self.propertyPayment = 0
        except:
            self.propertyPayment = 0
        self.propertyNetWorth = self.propertyPayment + self.checkComplet

        try:
            self.law14per = float(law14per) / 100
            if pd.isna(self.law14per):
                self.law14per = 0
        except:
            self.law14per = 0

        self.leaveReason = leaveReason

##### fucntions to calc the probility of get fired by age #####
def probability(num):
    proarray = []
    if num >= 19 or num <= 29:
        proarray.append(0.07)
        proarray.append(0.2)
    if num >= 30 or num <= 39:
        proarray.append(0.05)
        proarray.append(0.13)
    if num >= 40 or num <= 49:
        proarray.append(0.04)
        proarray.append(0.10)
    if num >= 50 or num <= 59:
        proarray.append(0.03)
        proarray.append(0.07)
    if num >= 60 or num <= 67:
        proarray.append(0.02)
        proarray.append(0.03)

    return proarray
#########################

######### importing Data from ExcelFile to CSV file #################
df = pd.read_excel(r'data4.xlsx', header=1)
df.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfile.csv', encoding='utf-8')
df = df.reset_index()
############################################################

########### creating death log dictionary #################
dl = pd.read_excel(r'deathlog.xlsx', header=1)
dl.to_csv('death.csv', encoding='utf-8')
dl = pd.read_csv('death.csv', encoding='utf-8')
dl = dl.reset_index()
deathdict = {}
for i in dl.iloc:
    deathdict[i['age']] = i['q(x)']
############################################################

########### creating DiscountRate dictionary #############
discountRate = pd.read_excel(r'data4.xlsx', header=2, sheet_name=1, usecols="A,B")
discountRate.to_csv('discountRate.csv', encoding='utf-8')
discountRate = pd.read_csv('discountRate.csv', encoding='utf-8')
discountRate = discountRate.reset_index()

discountRateDict = {}
for i in discountRate.iloc:
    discountRateDict[i['שנה ']] = i['שיעור היוון']
###################################################################
employeeArray = []
for i in df.iloc:
    e = employee(i['שם '], i['שם משפחה'], i['מין'], i['תאריך לידה'], i['תאריך תחילת עבודה '], i['שכר '],
                 i['תאריך  קבלת סעיף 14'], i['שווי נכס'], i['הפקדות'],
                 i['תאריך עזיבה '], i['תשלום מהנכס'], i["השלמה בצ'ק"], i['סיבת עזיבה'], i['אחוז סעיף 14'])
    employeeArray.append(e)

################## functions for first Sigma ###################################
def firstSigma(employee):
    if i.gender == 'M':
        for j in range(0, 67 - i.age - 1):
            i.compensation = i.compensation + (
                    i.salary * i.seniority * (1 - i.law14per) * helpFuncFirstSigma(employee.age, j))
    if i.gender == 'F':
        for j in range(0, 64 - i.age - 1):
            i.compensation = i.compensation + (
                    i.salary * i.seniority * (1 - i.law14per) * helpFuncFirstSigma(employee.age, j))


def helpFuncFirstSigma(age, time):

    return ((pow(1 + 0.03, time + 0.5) * probability(age + time + 1)[0] * pX(age, time + 1)) / pow(1 + discountRateDict[time+1],
                                                                                           time + 0.5))


def pX(age, time):
    x = 1
    for i in range(0, time):
        x = x * (1 - probability(age + i)[1] - probability(age + i)[0] - deathdict[age + i])
    return x

######################################################################################################################
################# functions for Second Sigma #################################################################

def secondSigma(employee):
    if i.gender == 'M':
        for j in range(0, 67 - i.age - 1):
            i.compensation = i.compensation + (
                    i.salary * i.seniority * (1 - i.law14per) * helpFuncFirstSigma(employee.age, j))
    if i.gender == 'F':
        for j in range(0, 64 - i.age - 1):
            i.compensation = i.compensation + (
                    i.salary * i.seniority * (1 - i.law14per) * helpFuncSeconSigma(employee.age, j))


def helpFuncSeconSigma(age,time):
     return ((pow(1 + 0.03, time + 0.5) * deathdict[age+time+1] * pX(age, time + 1)) / pow(1 + discountRateDict[time+1],
                                                                                           time + 0.5))

#######################################################################################################################
################################ Functions Third Sigma ################################################################
def thirdSigma(employee):
    if i.gender == 'M':
        for j in range(0, 67 - i.age - 1):
            i.compensation = i.compensation + employee.propertyValue * pX(employee.age,j)*probability(employee.age+j+1)[1]

    if i.gender == 'F':
        for j in range(0, 64 - i.age - 1):
            i.compensation = i.compensation + employee.propertyValue * pX(employee.age, j) * probability(
                employee.age + j + 1)[1]


#######################################################################################################################

count = 0
for i in employeeArray:
    if i.workleave != None:
        if i.workleave.year == 2021:
            if i.leaveReason == 'התפטרות':
                i.compensation = 0
    else:
            firstSigma(i)
            secondSigma(i)
            thirdSigma(i)
            if i.gender == 'M':
                w = 67
            else:
                w = 64
            i.compensation = i.compensation + (i.salary * i.seniority * (1 - i.law14per) *
             (pow(1 + 0.03, w - i.age + 0.5) * probability(w- 1)[0] * pX(i.age, w-i.age-1)) / pow(
                        1 + discountRateDict[round(i.seniority* 365.25)],
                        w-i.age+0.5)
             )+(
                    i.salary * i.seniority * (1 - i.law14per) *  (pow(1 + 0.03, w- i.age -1 + 0.5) * deathdict[w-1] * pX(i.age, w- i.age-1)) / pow(1 + discountRateDict[round(i.seniority* 365.25)],
                                                                                            w-i.age-1 + 0.5)

            )+(i.propertyValue*pX(i.age,w-i.age-1)*probability(w-1)[1])+(i.salary * i.seniority * (1 - i.law14per) *(
                    pow(1 + 0.03, w- i.age -1 + 0.5)  * pX(i.age, w- i.age-1) * (1-probability(w-1)[0]*probability(w-1)[1]*deathdict[w-1]))/pow(1 + discountRateDict[round(i.seniority* 365.25)],w-i.age) )




newarr =[]
for i in employeeArray:
    arr = [i.firstName,i.lastName,i.compensation]
    newarr.append(arr)

df = pd.DataFrame(newarr)
df.to_excel(excel_writer = "test.xlsx")