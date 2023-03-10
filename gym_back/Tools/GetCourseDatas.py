import json
import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'


def GetCourseDatas():
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()
    SQL = """
            SELECT
                *
            FROM
                course 
         """
    cursor.execute(SQL)
    rows = cursor.fetchall()
    d = {}
    for row in rows:
        TimeResult=[]
        tmp=[row.Monday,row.Tuesday,row.Wednesday,row.Thursday,row.Friday,row.Saturday,row.Sunday]
        for i in tmp:
            i=i.split(',')
            t=[]
            for j in i:
                t.append(j=='True')
            TimeResult.append(t)
        d[row.course_title]={
            'Time':TimeResult,
            'description':row.description,
            'price':row.price,
            'period':row.period,
            'number_of_lessons':row.number_of_lessons,
            'course_level':row.course_level
        }
    Json={
        'Datas':d
    }
    print(d)
    d = json.dumps(Json)
    with open("./Datas/Course.json", "w") as outfile:
        outfile.write(d)
    outfile.close()


if __name__ == '__main__':
    GetCourseDatas()
