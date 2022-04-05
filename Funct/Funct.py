import os
import os.path
import pandas as pd

def folders_create(folder_path:str):
    try:
        os.startfile(folder_path)
    except FileNotFoundError:
        os.mkdir(folder_path)
        os.startfile(folder_path)
    #There is folder needed for exporting files:
    if not os.path.isdir(f"{folder_path}\\Exports"):
        os.mkdir(f"{folder_path}\\Exports")
    print("Przegraj pliki importu do otwartego folderu")

def user_input():
    try:
        period = int(input("Jakiego miesiąca dotyczy plik "))
        acc_document_nr = int(input("Pod jakim numerem DW, pozostanie zaimportowany pierwszy plik "))
    except ValueError:
        print("To nie była liczba [1,2 ...] Podaj jeszcze raz")
        user_input()
    return [period, acc_document_nr]

def df_final_fun(df = None):
    columns_final = ["Numer pozycji", "Konto", "Kwota WN", "Kwota MA", "Kwota WN w walucie", "Kwota MA w walucie",
                     "Kod waluty", "Kurs waluty", "Stanowisko kosztów", "Stan. kosztów przeciwstawne",
                     "Pozycja kalkulacji kosztów","Zlecenie", "Transakcja", "Jednostka organizacyjna",
                     "Kod kontrahenta", "Należność", "Zobowiazanie","Numer pracownika",
                     "Symbol rozrachunku z pracownikiem", "Indeks", "Magazyn", "Opis dodatkowy"]
    df_final = pd.DataFrame(columns = columns_final)
    df_final[["Kwota MA","Zobowiazanie", "Kod kontrahenta"] ] = df[["Zobowiązania", "Symbol rozrachunku",
                                                                    "Kod kontr."]]
    df_final["Numer pozycji"].fillna(1, inplace = True)
    df_final["Konto"].fillna("251-02", inplace = True)
    df_final.reset_index(drop=True, inplace = True)
    df_final = df_final.append({"Numer pozycji": "***"}, ignore_index = True)
    return df_final