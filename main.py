import datetime
import pandas as pd

class employee:
    def __init__(self, firstName, lastName, gender, birthDate, worBegin, salary,
                 law14Date, propertyValue, deposits, workLeave, propertyPayment, checkComplet, leaveReason):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.age = datetime.today().year - datetime.strptime(birthDate, '%d/%m/%Y').year
        self.seniority = (datetime.strptime('31/12/2021', '%d/%m/%Y').year - datetime.strptime(worBegin, '%d/%m/%Y').year)/365.25
        self.salary = salary
        self.law14date = datetime.strptime(law14Date, '%d/%m/%Y')
        self.propertyValue = propertyValue
        self.deposits = deposits
        self.propertyNetWorth = propertyPayment + checkComplet
        self.leaveReason = leaveReason


df = pd.read_excel(r'C:\Users\amara\Desktop\data.xlsx', header=1)
df.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfile.csv', encoding='utf-8')
df = df.reset_index()

employeeArray = []
for i in df.iloc:
    employee = employee(i['שם'],i['שם משפחה'],i['מין'],i['תאריך לידה'],i['תאריך תחילת עבודה '],i['שכר '],
                        i['תאריך  קבלת סעיף 14'],i['אחוז סעיף 14'],i['שווי נכס'],i['הפקדות'],
                        i['תאריך עזיבה '],i['תשלום מהנכס'],i['השלמה בצ'ק])
