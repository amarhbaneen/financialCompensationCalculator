
import pandas as pd
from datetime import datetime



class employee:
    def __init__(self, firstName, lastName, gender, birthDate, worBegin, salary,
                 law14Date, propertyValue, deposits, workLeave, propertyPayment, checkComplet, leaveReason,law14per):
        self.compensation = 0

        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.age =  2020 - datetime.strptime(birthDate, '%Y-%m-%d').year
        self.seniority = (datetime.strptime('2021-12-31', '%Y-%m-%d').year - datetime.strptime(worBegin,'%Y-%m-%d').year)/365.25
        self.salary = float(salary)
        if type(law14Date) != float:
            self.law14date = datetime.strptime(law14Date, '%Y-%m-%d')
        else:
            self.law14date = None

        if type(workLeave) != float:
            if workLeave == '-':
                self.workleave = None
            else:
                self.workleave = datetime.strptime(workLeave,'%Y-%m-%d %H:%M:%S')
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
            self.law14per = float(law14per)/100
            if pd.isna(self.law14per):
                self.law14per = 0
        except:
            self.law14per = 0

        self.leaveReason = leaveReason

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



df = pd.read_excel(r'C:\Users\amara\Desktop\data.xlsx', header=1)
df.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfile.csv', encoding='utf-8')
df = df.reset_index()

employeeArray = []
for i in df.iloc:
    e = employee(i['שם'], i['שם משפחה'], i['מין'], i['תאריך לידה'], i['תאריך תחילת עבודה '], i['שכר '],
                 i['תאריך  קבלת סעיף 14'], i['שווי נכס'], i['הפקדות'],
                 i['תאריך עזיבה '], i['תשלום מהנכס'], i["השלמה בצ'ק"], i['סיבת עזיבה'],i['אחוז סעיף 14'])
    employeeArray.append(e)

count = 0
for i in employeeArray:
   if  i.workleave != None :
       if i.workleave.year == 2021:
           if i.leaveReason == 'התפטרות':
                i.compensation = 0
       else:
            for x in range(20,22):
                if x+2000 - i.law14date.year > 0:
                    i.compensation = (i.salary * i.seniority * (1-i.law14per)) * pow((1+(i.deposits - i.propertyValue),count+0.5) #TODO to finish the forumal !


