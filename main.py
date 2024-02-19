#

import csv
import os
import matplotlib.pyplot as p


time = []

if os.path.exists("data.csv"):
    with (open("data.csv", encoding="utf-8-sig")as f):
        csvREAD = csv.reader(f)
        for row in csvREAD:
            time.append(row[0])
        print("Please input data into", time[0])
        while True:
            data1 = input("Time:")
            if data1 == "":
                break

        f = open("data.csv", "w")
        f.write((data1 + "\n"))
        f.close()

else:
    print("Please name the file.")
    name1 = input("")
    f = open("data.csv", "w")
    f.write(name1+"\n")
    f.close()

voltage = []

if os.path.exists("data2.csv"):
    with open("data2.csv", encoding="utf-8-sig")as g:
        csvREAD = csv.reader(g)
        for row in csvREAD:
            voltage.append(row[0])
        print("Please input data into", voltage[0])
        while True:
            data2 = input("Time:")
            if data2 == "":
                break

        g = open("data2.csv", "w")
        g.write((data2 + "\n"))
        g.close()

else:
    print("Please name the file.")
    name2 = input("")
    g = open("data2.csv", "w")
    g.write(name2+"\n")
    g.close()


quit()
