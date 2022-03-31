from Classes.Classes import ImportFileCreator, DataframefromExcel
from Funct.Funct import folders_create, user_input, df_final_fun
from os import listdir
import os.path
import pandas as pd
import xlsxwriter
import openpyxl


def main():
    document_nr_and_period = user_input()
    path = "C:\Przemek\\import"
    folders_create(path)
    # creating multiple "export later" files:
    for export_file in range(len(listdir(path))-1):
        export_file_name = f"export_file_{export_file}.xlsx"
        export_file = ImportFileCreator(f"{path}\\Exports\\{export_file_name}",document_nr_and_period[1],
                    document_nr_and_period[0])
        export_file.excel_new_worksheet()
        document_nr_and_period[1] += 1
    # preparing df data from existing excel files
    export_path = "C:\Przemek\\import\\Exports"
    file_list = [file for file in listdir(path) if os.path.isfile(f"{path}\\{file}")]
    print(file_list)
    for file, export_file in zip(file_list,listdir(export_path)):
        instance= DataframefromExcel(f"{path}\\{file}")
        df = instance.df_for_concat(instance.import_dataframe())
        df_final = df_final_fun(df)
 # appending df_final to previously created excel export files
        #Uwaga tutaj błąd dać do  góry file,export file
        with pd.ExcelWriter(f"{export_path}\\{export_file}",mode='a',engine='openpyxl',
        if_sheet_exists = 'overlay') as writer:
                df_final.to_excel(writer, sheet_name='Sheet1', startrow = 4, index = False)

if __name__ == "__main__":
    main()