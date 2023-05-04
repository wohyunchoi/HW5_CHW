import csv

if __name__ == "__main__":

    f= open('q1.csv')
    data = csv.reader(f)
    header = next(data)
    averTemp = 0
    averMaxTemp = 0
    averMinTemp = 0
    totalDate = 0
    for row in data:
        for i in range(2,5):
            if row[i] == "":
                row[i] = 999
            row[i] = float(row[i])
        if row[2] == 999 or row[3] == 999 or row[4] == 999:
            continue
        averTemp += row[2]
        averMinTemp += row[3]
        averMaxTemp += row[4]
        totalDate += 1
        
    averTemp /= totalDate
    averMinTemp /= totalDate
    averMaxTemp /= totalDate
    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(averTemp))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(averMinTemp))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(averMaxTemp))
    f.close()
