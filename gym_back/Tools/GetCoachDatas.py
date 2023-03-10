import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'


def GetCoachDatas():
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    SQL = """
            SELECT
                coach.name,coach.coach_id,coach.gender,coach.coach_level,coach.gym_name,course.course_title
            FROM
                coach
                LEFT JOIN 
                    teach
                ON 
                    coach.coach_id=teach.coach_id
                LEFT JOIN
                    course
                ON 
                    teach.course_id=course.course_id
         """
    cursor.execute(SQL)
    rows = cursor.fetchall()
    d = dict()
    for row in rows:
        try:
            tmp=d[row.gym_name + ',' + row.course_title]
            d[row.gym_name + ',' + row.course_title].append({'Name':row.name, 'Gender':row.gender, 'Level':row.coach_level,'ID':row.coach_id})
        except:
            d[row.gym_name + ',' + row.course_title] = [{'Name':row.name, 'Gender':row.gender, 'Level':row.coach_level,'ID':row.coach_id}]
    print(d)
    Json={
        'Datas':d
    }
    Json=json.dumps(Json)
    with open("./Datas/Coach.json", "w") as outfile:
        outfile.write(Json)
    outfile.close()


# if __name__ == '__main__':
#     GetCoachDatas()
