import datetime
import json

import pyodbc
from gym.Tools import Tool_Insert

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

def SignUp(name,phone_number,email,gender,birthday,password):

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    Member_id=GetMember_id(cursor)
    Member_type=3
    start_date=str(datetime.date.today())
    Delta_Time= datetime.timedelta(days=300)
    expiry_date=str(datetime.date.today()+Delta_Time)
    balance=str(1000)
    RepeatState=GetRepeatState(cursor,email,password)

    if(RepeatState):
        Datas=[[Member_id,Member_type,start_date,expiry_date,balance,name,gender,phone_number,birthday,password,email]]
        print(Datas)
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='membership')

    JSON={
        'Status':RepeatState
    }
    print(JSON)
    Json=json.dumps(JSON)
    return Json

def GetRepeatState(cursor,email,password):
    SQL = """
                SELECT
                    member_id
                FROM
                    membership
                WHERE email=? AND password=?
             """
    cursor.execute(SQL,email,password)
    rows = cursor.fetchone()
    try:
        tmp=rows[0]
        return False
    except:
        return True
def GetMember_id(cursor):
    SQL = """
            SELECT
                member_id
            FROM
                membership
            ORDER BY member_id DESC
         """
    cursor.execute(SQL)
    rows = cursor.fetchone()
    Member_id = (int(rows[0]) + 1)
    return Member_id

# SignUp('wei','0988769461','open891013@gmail.com','男','10/13/2000','W891013')