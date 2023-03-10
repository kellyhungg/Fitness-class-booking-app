import datetime
import json

import pyodbc
from gym.Tools import Tool_Insert

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

def GetRecord_id(cursor):
    SQL = """
                SELECT
                    record_id
                FROM
                    transact
                ORDER BY record_id DESC
             """
    cursor.execute(SQL)
    rows = cursor.fetchone()
    Record_id = rows[0] + 1
    return Record_id

def GetCourseIDAndAmount(cursor,course):
    SQL = """
                SELECT
                    course_id,price
                FROM
                    course
                WHERE
                    course_title=?
             """
    cursor.execute(SQL, course)
    rows = cursor.fetchone()

    return rows[0],rows[1]


def JoinUs(gym_name,coach_id,course,member_id):
    time=str(datetime.date.today())
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    try:
        Record_id=GetRecord_id(cursor)

        Course_id,Amount=GetCourseIDAndAmount(cursor,course)

        Datas=[[Record_id,Course_id,gym_name,coach_id,time,Amount,course,member_id]]
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='transact')
        Datas=[[Record_id,gym_name]]
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='host')
        Datas=[[Record_id,member_id]]
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='client')
        Json={
            'Status':True
        }
        Json=json.dumps(Json)
        return Json
    except:
        Json = {
            'Status': False
        }
        Json = json.dumps(Json)
        return Json

# if __name__=='__main__':
#     JoinUs('台中','C8974','Boxing',40072501)