import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'


def GetMyPlan(member_id):
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    SQL = """
            SELECT
                course.course_title,course.price,coach.name
            FROM
                membership
                LEFT JOIN 
                    transact
                ON 
                    membership.member_id=transact.member_id
                LEFT JOIN 
                    course
                ON 
                    transact.course=course.course_title
                LEFT JOIN
                    coach
                ON 
                    transact.coach_id=coach.coach_id
            WHERE membership.member_id=?
            ORDER BY transact.time DESC 
         """
    cursor.execute(SQL,member_id)
    rows = cursor.fetchall()
    d = []
    for row in rows:
        d.append({'Course':row.course_title,'Price':row.price,'Teacher':row.name})

    SQL = """
                SELECT
                    membership.balance
                FROM
                    membership
                WHERE membership.member_id=?
             """
    cursor.execute(SQL, member_id)
    rows = cursor.fetchone()

    Json = {
        'Balance':rows[0],
        'Datas': d
    }
    print(Json)
    d = json.dumps(Json)
    return d

# if __name__ == '__main__':
#     GetMyPlan(40072501)
