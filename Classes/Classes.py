import pandas as pd
import xlsxwriter
import openpyxl


class ImportFileCreator():

    def __init__(self, path: str, acc_document_nr: int, period:int):
        self.path = path
        self.acc_document_nr = acc_document_nr
        self.period = period


    def excel_new_worksheet(self):
        with xlsxwriter.Workbook(self.path) as workbook:
            worksheet = workbook.add_worksheet()
            # Create first few indexses needed for import (accounting program neeeds those as configuration)

            worksheet.write(0, 0, "Rodzaj dowodu")
            worksheet.write(0, 1, "PK")
            worksheet.write(1, 0, "Numer dowodu")
            worksheet.write(1, 1, self.acc_document_nr)
            worksheet.write(2, 0, "Numer okresu")
            worksheet.write(2, 1, self.period)
            worksheet.write(3, 0, "znak końca pliku")
            worksheet.write(3, 1, "***")

class DataframefromExcel():

    def __init__(self, path:str):
        self.path = path
        self.path = path

    def import_dataframe(self):
        df = pd.read_excel(self.path, engine="openpyxl", header=1)
        return df

    def df_for_concat(self, df = None):
        self.df = df
        #change the sign of Zobowiazania column
        df["Zobowiązania"] = df["Zobowiązania"] * -1
        #remove not doubling Kod kontr.
        filt = df["Kod kontr."].value_counts()
        to_remove = filt[filt % 2 != 0].index
        df = df[~self.df["Kod kontr."].isin(to_remove)]
        #remove not doubling NR Urzadzenia
        df['NR Urzadzenia'] = df['Symbol rozrachunku'].str[:15]
        filt2 = df['NR Urzadzenia'].value_counts()
        to_remove2 = filt2[filt2 %2 !=0].index
        df = df[~df['NR Urzadzenia'].isin(to_remove2)]
        #drop last row
        df.drop(df.tail(1).index,inplace=True)
        return df

