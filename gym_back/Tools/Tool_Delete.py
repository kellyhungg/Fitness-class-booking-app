import pyodbc


class DeleteDatas:
    def __init__(self, args, Server='000.000', Port='0000', DataBase='Test', UserName='aa',
                 PassWord='000000', Table='None'):
        self.cnxn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + Server + ',' + Port + ';DATABASE=' + DataBase + ';UID=' + UserName + ';PWD=' + PassWord)
        self.cursor = self.cnxn.cursor()
        self.args = args

        if (Table == 'client'):
            self.Deleteclient()
            self.commit()
        elif (Table == 'membership'):
            self.Deletemembership()
            self.commit()
        elif (Table == 'post'):
            self.Deletepost()
            self.commit()
        elif (Table == 'editoral'):
            self.Deleteeditoral()
            self.commit()
        elif (Table == 'transact'):
            self.Deletetransact()
            self.commit()
        elif (Table == 'host'):
            self.Deletehost()
            self.commit()
        elif (Table == 'gym'):
            self.Deletegym()
            self.commit()
        elif (Table == 'coach'):
            self.Deletecoach()
            self.commit()
        elif (Table == 'teach'):
            self.Deleteteach()
            self.commit()
        elif (Table == 'course'):
            self.Deletecourse()
            self.commit()
        elif (Table == 'useCourse'):
            self.DeleteuseCourse()
            self.commit()
        elif (Table == 'equipment'):
            self.Deleteequipment()
            self.commit()

    def Deletemembership(self):
        sql = """
                DELETE FROM 
                    membership
                WHERE 
                    membership_id=?
            """
        for i in self.args:
            print(i)
            self.cursor.execute(sql, i)

    def commit(self):
        self.cnxn.commit()
        print('Data have set in MS SQL SERVER!')