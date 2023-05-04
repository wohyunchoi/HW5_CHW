import csv

if __name__ == "__main__":
    
    f= open('202303_Seoul_Subway.csv',encoding='UTF8')
    data = csv.reader(f)
    header = next(data)
    a = [0,0,0,0,0,0,0,0,0]
    for row in data:
        for i in range(4,6):
            if row[i] == "":
                row[i] = 0
            row[i] = int(row[i])
    
        if row[1] == "1호선":
            a[0] += row[4]
            a[0] += row[5]
        if row[1] == "2호선":
            a[1] += row[4]
            a[1] += row[5]
        if row[1] == "3호선":
            a[2] += row[4]
            a[2] += row[5]
        if row[1] == "4호선":
            a[3] += row[4]
            a[3] += row[5]
        if row[1] == "5호선":
            a[4] += row[4]
            a[4] += row[5]
        if row[1] == "6호선":
            a[5] += row[4]
            a[5] += row[5]
        if row[1] == "7호선":
            a[6] += row[4]
            a[6] += row[5]
        if row[1] == "8호선":
            a[7] += row[4]
            a[7] += row[5]
        if row[1] == "9호선":
            a[8] += row[4]
            a[8] += row[5]
    b = a.copy()
    a.sort()
    print("*** Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line {0:d} (the number of total passengers: {1:d})".format(b.index(a[8])+1,a[8]))
    print("2st Busiest Line: Line {0:d} (the number of total passengers: {1:d})".format(b.index(a[7])+1,a[7]))
    print("1st Least used Line: Line {0:d} (the number of total passengers: {1:d})".format(b.index(a[0])+1,a[0]))
    print("2st Lesat used Line: Line {0:d} (the number of total passengers: {1:d})".format(b.index(a[1])+1,a[1]))
    f.close()
