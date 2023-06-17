
import csv
from statistics import mean
with open('grades.csv') as f :
    reader= csv.reader(f)
    for row in reader:
        print(row)
        name=row[0]
        these_grades=list()
        for grade in row[1:] :
            these_grades.append(int(grade))
        print("average of %9s is %.2f" %(name ,mean(these_grades)))