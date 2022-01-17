import csv
from tkinter import N
import matplotlib.pyplot as plt
import pandas as pd

def mymetrics(file_path):
    dict = {}
    with open(file_path) as f:
        r = csv.reader(f)
        #Skip header
        next(r)
        for row in r:
            user_id = int(row[1])
            if user_id not in dict:
                dict[user_id] = {"total": 0, "number": 0}
            dict[user_id]["total"] += int(row[3])
            dict[user_id]["number"] += int(row[4])
    data = []
    for id, pair in dict.items():
        shop_avg = pair["total"]/pair["number"]
        data.append({"id": id, "avg": shop_avg})
    df = pd.DataFrame(data, columns= ["id", "avg"] )
    # Apply 1.5 IQR
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

    print("\nStats of Trimmed Average Shop Item Value Dataset:")
    print(df["avg"].describe())
    print("\nTrimmed Average Shop Item Value(TASIV):")
    TASIV = df["avg"].mean()
    print(TASIV)
    return TASIV

def gainKnowledge(file_path):
    columns =  ["item_amount"]
    data = []
    with open(file_path) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            temp = {columns[0]:int(row[3])/int(row[4])}
            for _ in range(int(row[4])):
                data.append(temp)
    mydf = pd.DataFrame(data, columns =columns)
    print(mydf.describe())
    print(mydf['item_amount'].value_counts())

if __name__ == "__main__":
    rows = 0
    numOfItems = 0
    total = 0
    file_path = "./2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv"
    dict = {}
    with open(file_path) as f:
        r = csv.reader(f)
        # SKIP header
        next(r)
        for row in r:
            total += int(row[3])
            numOfItems += int(row[4])
            rows +=1
    AOV = total/rows # Average Order Value
    AIV = total/numOfItems# Average Item Value

    print("AOV:" + str(AOV))
    print("Average Item Price:" + str(AIV))
    # gainKnowledge(file_path)
    mymetrics(file_path)
