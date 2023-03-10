import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'


def GetBranch():
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    SQL = """
            SELECT
                *
            FROM
                gym 
         """
    cursor.execute(SQL)
    rows = cursor.fetchall()
    d = []
    for row in rows:
        d.append({'Name':row.gym_name,'Address':row.gym_address,'PhoneNumber':row.phone_number})
    Json={
        'Datas':d
    }
    print(d)
    d = json.dumps(Json)
    with open("./Datas/Branch.json", "w+") as outfile:
        outfile.write(d)
        outfile.close()
        print('Data saved')

if __name__ == '__main__':
    GetBranch()
