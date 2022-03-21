import math

import pandas as pd
from datetime import datetime

class employee:
    def __init__(self, firstName, lastName, gender, birthDate, worBegin, salary,
                 law14Date, propertyValue, deposits, workLeave, propertyPayment, checkComplet, leaveReason):

        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.age = datetime.today().year - datetime.strptime(birthDate, '%Y-%m-%d').year
        self.seniority = (datetime.strptime('2021-12-31', '%Y-%m-%d').year - datetime.strptime(worBegin, '%Y-%m-%d').year)/365.25
        self.salary = salary
        if type(law14Date) != float:
            self.law14date = datetime.strptime(law14Date, '%Y-%m-%d')
        else:
            self.law14date = None
        self.propertyValue = propertyValue
        self.deposits = deposits
        self.pp = propertyPayment
        self.cc = checkComplet
        if self.cc == 'nan':
            self.cc = 0
        else:
            self.cc = float(self.cc)
        if self.pp == 'nan':
            self.pp = 0
        else:
            try:
                self.pp = float(self.pp)
            except:
                self.pp = 0
        self.propertyNetWorth = self.pp + self.cc
        self.leaveReason = leaveReason


df = pd.read_excel(r'C:\Users\amara\Desktop\data.xlsx', header=1)
df.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfile.csv', encoding='utf-8')
df = df.reset_index()

employeeArray = []
for i in df.iloc:
    e = employee(i['שם'],i['שם משפחה'],i['מין'],i['תאריך לידה'],i['תאריך תחילת עבודה '],i['שכר '],
                        i['תאריך  קבלת סעיף 14'],i['שווי נכס'],i['הפקדות'],
                        i['תאריך עזיבה '],i['תשלום מהנכס'],i["השלמה בצ'ק"],i['סיבת עזיבה'])
    employeeArray.append(e)

