import json
import pyodbc
from gym.Tools import Tool_Update

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

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


def EditInfo(member_id,name,phone_number,password,email):

    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    RepeatState=GetRepeatState(cursor,email,password)
    if(RepeatState):
        UpdateTools= Tool_Update.UpdateDatas([[name, phone_number, password, email, member_id]], Table='membership')
    Json={
        'Status':RepeatState
    }
    Json=json.dumps(Json)
    print(Json)
    return Json

# if __name__=='__main__':
#     EditInfo(49999971,'2sas','女','S1212','ls@gmail.com')
