import pyodbc

class InsertDatas:
    def __init__(self,args,Mode='Default',Server='000.000',Port='0000',DataBase='Test',UserName='aa',PassWord='000000',Table='None',Tables=['membership','post','editoral','transact','client','host','gym','coach','teach','course','useCourse','equipment'],columns=[]):
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+Server+','+Port+';DATABASE='+DataBase+';UID='+UserName+';PWD='+ PassWord)
        self.cursor = self.cnxn.cursor()
        self.args=args
        self.Table=Table
        self.Columns=columns

        if(self.Table in Tables):
            if(Mode=="Default"):
                self.default_Insert()
                self.commit()
            elif(Mode=='Specific'):
                self.specific_Insert()
                self.commit()

    def default_Insert(self):
        sql ='INSERT INTO {} VALUES ({})'
        for i in self.args:
            print('Table:',self.Table)
            print('Data:',i)
            self.cursor.execute(sql.format(self.Table,('?,'*len(i))[:-1]), i)

    def specific_Insert(self):
        sql = 'INSERT INTO {} ({}) VALUES ({})'
        for i in self.args:
            print('Table:', self.Table)
            print('Data:', i)
            self.cursor.execute(sql.format(self.Table,str(self.Columns)[1:-1].replace('\'','').replace(' ',''),('?,'*len(i))[:-1]), i)

    def commit(self):
        self.cnxn.commit()
        print('Data have set in MS SQL SERVER!')