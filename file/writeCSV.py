import  csv

def writeCsv(path,data):
    with open(path,"w") as f:
        writer = csv.writer(f)
        for rowdata in data:
            writer.writerow(rowdata)


path = r"c\tex.csv"
writeCsv(path,[1,2,3],[4,5,6],[7,8,9])

#with open(path,"w",newline="") 解决空行问题