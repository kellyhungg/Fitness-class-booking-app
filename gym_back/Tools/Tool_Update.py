import pyodbc


class UpdateDatas:
    def __init__(self, args, Server='000.000', Port='0000', DataBase='Test', UserName='aa',
                 PassWord='000000', Table='None'):
        self.cnxn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
        self.cursor = self.cnxn.cursor()
        self.args = args

        if (Table == 'membership'):
            self.Updatemembership()
            self.commit()

    def Updatemembership(self):
        sql = """
                UPDATE 
                    membership
                SET
                    name=?,
                    phone_number=?,
                    password=?,
                    email=?
                WHERE
                    member_id=?
            """
        for i in self.args:
            print(i)
            self.cursor.execute(sql, i)


    def commit(self):
        self.cnxn.commit()
        print('Data have set in MS SQL SERVER!')