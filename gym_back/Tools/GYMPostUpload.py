import datetime
import json

import pyodbc
from gym.Tools import Tool_Insert,PostGet

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

def GetPost_id(cursor):
    SQL = """
                SELECT
                    post_id
                FROM
                    post
                ORDER BY post_id DESC
             """
    cursor.execute(SQL)
    rows = cursor.fetchone()
    Post_id = rows[0] + 1
    return Post_id


def UploadPost(post_title,post_content,member_id):
    time=str(datetime.date.today())
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    try:
        Post_id=GetPost_id(cursor)
        Datas=[[Post_id,member_id,time]]
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='post')
        Datas=[[Post_id,post_title,post_content]]
        InsertTool= Tool_Insert.InsertDatas(Datas, Table='editoral')
        Json={
            'Status':True
        }
        Json=json.dumps(Json)
        PostGet.GetPost()
        return Json
    except:
        Json = {
            'Status': False
        }
        Json = json.dumps(Json)
        return Json

# if __name__=='__main__':
#     UploadPost(post_title='haha',post_content='gsgsgs',member_id=41533816)