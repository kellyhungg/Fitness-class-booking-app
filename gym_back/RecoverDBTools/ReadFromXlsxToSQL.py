from gym.Tools import Tool_Insert
import pandas as pd

ExcelFile = '../DataBase(Excel)/database.xlsx'
SpecificTable = 'client'


def ReadSpecific(Table):
    df = pd.read_excel(ExcelFile, sheet_name=Table, dtype=str)
    args = list(df.values)
    for index, val in enumerate(args):
        args[index] = list(val)
    InsertTools = Tool_Insert.InsertDatas(args, Table=Table)


def ReadALL():
    xls = pd.ExcelFile(ExcelFile)
    Df = dict()

    for Table in xls.sheet_names:
        Df[Table] = pd.read_excel(ExcelFile, Table, dtype=str)

    for Table in Df:
        args = list((Df[Table]).values)
        for index, val in enumerate(args):
            args[index] = list(val)
        InsertTools = Tool_Insert.InsertDatas(args, Table=Table)


def main():
    if SpecificTable == '':
        ReadALL()
    else:
        ReadSpecific(SpecificTable)


if __name__ == '__main__':
    main()
