import csv

with open('resources/kjv-john.csv', newline='') as csvfile:
    text = csv.reader(csvfile)
    for row in text:
        print(row)