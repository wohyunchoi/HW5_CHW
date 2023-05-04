import csv

if __name__ == "__main__":

    f= open('202303_Seoul_Subway.csv',encoding='UTF8')
    data = csv.reader(f)
    header = next(data)

    maxStation = ["","","",""]
    minStation = ["","","",""]
    maxPass = [0,0,0,0]
    minPass = [999999999,999999999,999999999,999999999]
    totalPass = [0,0,0,0]
    for row in data:
        for i in range(4,6):
            if row[i] == "":
                row[i] = 0
            row[i] = int(row[i])

        if row[1] == "1호선":
            totalPass[0] = row[4] + row[5]
            if totalPass[0] > maxPass[0]:
                maxPass[0] = totalPass[0]
                maxStation[0] = row[3]
            if totalPass[0] < minPass[0]:
                minPass[0] = totalPass[0]
                minStation[0] = row[3]
        if row[1] == "2호선":
            totalPass[1] = row[4] + row[5]
            if totalPass[1] > maxPass[1]:
                maxPass[1] = totalPass[1]
                maxStation[1] = row[3]
            if totalPass[1] < minPass[1]:
                minPass[1] = totalPass[1]
                minStation[1] = row[3]
        if row[1] == "3호선":
            totalPass[2] = row[4] + row[5]
            if totalPass[2] > maxPass[2]:
                maxPass[2] = totalPass[2]
                maxStation[2] = row[3]
            if totalPass[2] < minPass[2]:
                minPass[2] = totalPass[2]
                minStation[2] = row[3]
        if row[1] == "4호선":
            totalPass[3] = row[4] + row[5]
            if totalPass[3] > maxPass[3]:
                maxPass[3] = totalPass[3]
                maxStation[3] = row[3]
            if totalPass[3] < minPass[3]:
                minPass[3] = totalPass[3]
                minStation[3] = row[3]

    print("*** Subway Report for Seoul on March 2023 ***\n")
    for i in range (1,5):
        print("Line {0:d}".format(i))
        print("Busiest Station: {0:s}(the number of total passengers: {1:d})".format(maxStation[i-1],maxPass[i-1]))
        print("Least used Station: {0:s}(the number of total passengers: {1:d})\n".format(minStation[i-1],minPass[i-1]))

    f.close()
