import datetime
import pandas as pd


class employee:
    def __init__(self, firstName, lastName, gender, birthDate, worBegin, salary,
                 law14Date, propertyValue, deposits, workLeave, propertyPayment, checkComplet, leaveReason):
        self.gender = gender
        self.firstName = firstName
        self.lastName = lastName
        self.age = datetime.today().year - datetime.strptime(birthDate, '%d/%m/%Y').year
        self.seniority = datetime.strptime(workLeave, '%d/%m/%Y').year - datetime.strptime(worBegin, '%d/%m/%Y').year
        self.salary = salary
        self.law14date = datetime.strptime(law14Date, '%d/%m/%Y')
        self.propertyValue = propertyValue
        self.deposits = deposits
        self.propertyNetWorth = propertyPayment + checkComplet
        self.leaveReason = leaveReason


df = pd.read_excel(r'data.xlsx', header=1)
df.to_csv('csvfile.csv', encoding='utf-8')
df = pd.read_csv('csvfile.csv', encoding='utf-8')
df = df.reset_index()
employeeArray = []
for i in df.iterrows():
    print(i)
