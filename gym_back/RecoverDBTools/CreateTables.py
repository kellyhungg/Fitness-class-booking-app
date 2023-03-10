import pyodbc

Server = '000.000'
DataBase = 'Test'
Port = '0000'
UserName = 'aa'
PassWord = '000000'

def main():
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
    cursor = cnxn.cursor()

    try:
        sql = """
                DROP TABLE membership
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE membership
            (
                 member_id nchar(8) PRIMARY KEY ,
                 member_type tinyint,
                 start_date date,
                 expiry_date date,
                 balance smallint,
                 name nvarchar(30),
                 gender nchar(1),
                 phone_number nchar(10),
                 birthday date,
                 password varchar(max),
                 email varchar(max)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE gym
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE gym
            (
                 gym_name nchar(2) PRIMARY KEY ,
                 gym_address nvarchar(max),
                 phone_number nvarchar(20)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE course
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE course
            (
                 course_id int PRIMARY KEY,
                 course_title nvarchar(max),
                 price int,
                 period float,
                 number_of_lessons tinyint,
                 course_level tinyint,
                 Sunday	nvarchar(20),
                 Monday	nvarchar(20),
                 Tuesday nvarchar(20),
                 Wednesday nvarchar(20),
                 Thursday nvarchar(20),
                 Friday	nvarchar(20),
                 Saturday nvarchar(20),
                 description nvarchar(max)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE transact
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE transact
            (
                 record_id int PRIMARY KEY ,
                 course_id int REFERENCES course(course_id),
                 gym_name nchar(2),
                 coach_id nchar(5),
                 time date,
                 amount int,
                 course nvarchar(50),
                 member_id nchar(8) REFERENCES membership(member_id)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
            DROP TABLE client
        """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE client
            (
                 record_id int REFERENCES transact(record_id),
                 member_id nchar(8) REFERENCES membership(member_id)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE post
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE post
            (
                post_id int PRIMARY KEY,
                member_id nchar(8) REFERENCES membership(member_id),
                time date
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE editoral
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE editoral
            (
                 post_id int REFERENCES post(post_id),
                 post_title nvarchar(max),
                 post_content nvarchar(max)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE host
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE host
            (
                 record_id int,
                 gym_name nchar(2)
        
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE coach
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE coach
            (
                 coach_id nchar(5) PRIMARY KEY ,
                 name nvarchar(max),
                 gym_name nchar(2) REFERENCES gym(gym_name),
                 gender nchar(1),
                 coach_level tinyint,
                 salary int,
                 phone_number nchar(10)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE teach
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE teach
            (
                 coach_id nchar(5) REFERENCES coach(coach_id),
                 course_id int REFERENCES  course(course_id)
            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE equipment
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE equipment
            (
                equipment_id nchar(9) PRIMARY KEY ,
                equipment_name nvarchar(max),
                equipment_type nvarchar(10),
                equipment_quantity tinyint

            );
        """
    cursor.execute(sql)

    try:
        sql = """
                DROP TABLE useCourse
            """
        cursor.execute(sql)
    except:
        pass
    sql = """
            CREATE TABLE useCourse
            (
                 equipment_id nchar(9),
                 course_id int REFERENCES course(course_id),
                 use_date date
            );
        """
    cursor.execute(sql)

    cnxn.commit()


if __name__ == '__main__':
    main()
