import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'


def GetPost():
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    SQL = """
            SELECT
                membership.name,membership.gender,editoral.post_title,editoral.post_content
            FROM
                editoral
                LEFT JOIN 
                    post
                ON 
                    editoral.post_id=post.post_id
                LEFT JOIN
                    membership
                ON 
                    post.member_id=membership.member_id
            ORDER BY editoral.post_id DESC 
         """
    cursor.execute(SQL)
    rows = cursor.fetchall()
    d = []
    for row in rows:
        d.append({'Name':row.name, 'Gender':row.gender, 'Title':row.post_title,'Content':row.post_content})
    Json={
        'Datas':d
    }
    print(Json)
    d = json.dumps(Json)
    with open("./Datas/Post.json", "w") as outfile:
        outfile.write(d)
    outfile.close()


# if __name__ == '__main__':
#     GetPost()
