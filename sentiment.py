# read from the LIWC csv file

#
# import csv
#
# with open("liwc.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for lines in csv_reader:
#         print(lines[3])



# with open("test_fil.txt", "r") as f:
#     negText = f.read()
# negTokens = negText.split("\n") # This splits the text file into tokens on the new line character
# negTokens[-1:] = [] # This strips out the final empty item
# print(negTokens[-10:])

import pandas as pd
from numpy import nan

df = pd.read_csv("liwc.csv")
for index in range(df.shape[1]):
    columnSeriesObj = df.iloc[:, index]
    z = [x for x in columnSeriesObj.values if x is not nan]
    for i in range(len(z)):
        print(z[i])