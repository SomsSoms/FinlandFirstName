#FileManager.py
#Opens the required file and returns needed values

import xlrd

class NameData:
    Full = {}
    Men = {}
    Women = {}
    def __init__(self,Full,Men,Women):
        self.Full = Full
        self.Men = Men
        self.Women = Women

def OpenFile():
    file = "etunimitilasto-2018-09-03-vrk.xlsx"
    with xlrd.open_workbook(file) as f:
        FullDic = {}
        FullDic = ReadData(f, 1)

        Dic1 = ReadData(f, 1) #Men data
        Dic2 = ReadData(f, 4) #Women data

        FullDic.update(Dic2)

        data = NameData(FullDic,Dic1,Dic2)

    return data

def ReadData(file, sheetN):
    NameNumberDic = {}
    sheet = file.sheet_by_index(sheetN)

    for line in range(1, sheet.nrows):
        name = sheet.cell(line, 0).value
        number = int(sheet.cell(line, 1).value)
        NameNumberDic[name] = number

    return NameNumberDic
