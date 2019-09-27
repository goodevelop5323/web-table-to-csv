from selenium import webdriver
import sys
import tkinter as tk
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# Tkクラス生成
root = tk.Tk()
root.geometry('350x200')
root.title('Table to csv')

urlLabel = tk.Label(text="URL")
urlLabel.place(x=30, y=20)
urlTextField = tk.Entry(width=20)
urlTextField.place(x=150, y=20)

fileNameLabel = tk.Label(text="ファイル名")
fileNameLabel.place(x=30, y=50)
fileNameTextField = tk.Entry(width=20)
fileNameTextField.place(x=150, y=50)

classNameLabel = tk.Label(text="テーブルクラス名")
classNameLabel.place(x=30, y=80)
classNameTextField = tk.Entry(width=20)
classNameTextField.place(x=150, y=80)

classCountLabel = tk.Label(text="クラス番号")
classCountLabel.place(x=30, y=110)
classCountTextField = tk.Entry(width=20)
classCountTextField.place(x=150, y=110)
classCountTextField.insert(tk.END, "0")


def tableToCSV():
    html = urlopen(urlTextField.get())
    beautifulSoup = BeautifulSoup(html, 'html.parser')
    table = beautifulSoup.findAll("table", {"class": classNameTextField.get()})[int(classCountTextField.get())]
    innerTable = table.findAll('table')
    rows = innerTable.findAll('tr')


    with open(fileNameTextField.get(), "w", encoding='UTF-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text())
            writer.writerow(csvRow)


button = tk.Button(root, text="実行", command=tableToCSV)
button.place(x=200, y=150)

root.mainloop()

