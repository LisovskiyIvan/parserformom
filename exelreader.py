import pandas as pd

book = pd.read_excel("parserformom/test2.xlsx", index_col=[0], skiprows=None)

data = book.values
arr = []
for z in data:
    print(str(z)[0])
    for i in z:
        i = i
        # print(i)
print(book.values)
