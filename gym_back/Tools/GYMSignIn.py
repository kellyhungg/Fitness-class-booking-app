import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

def GetMember_id(cursor,email,password):
    SQL = """
            SELECT
                member_id,name,gender,member_type
            FROM
                membership
            WHERE
                email=? AND password=?
         """
    cursor.execute(SQL,email,password)
    rows = cursor.fetchone()
    if(rows==None):
        return ['','','','']
    else:
        return rows

def SignIn(email,password):
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    Member_id,Name,Gender,Member_type=GetMember_id(cursor,email,password)
    Json = {
        'Status': False if (len(Member_id) == 0) else True,
        'Member_id': Member_id,
        'Name':Name,
        'Gender':Gender,
        'Member_type':Member_type
    }
    print(Json)
    Json = json.dumps(Json)
    return Json

# SignIn('open891013@gmail.com','1013')