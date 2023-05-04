import csv

if __name__ == "__main__":
    
    f= open('2022_Seoul_Temp.csv')
    data = csv.reader(f)
    header = next(data)
    larTempvar = ""
    maxTemDiff = 0
    smaTempvar = ""
    minTemDiff = 999
    temDiff = 0

    for row in data:
        for i in range(3,5):
            if row[i] == "":
                row[i] = "999"
            row[i] = float(row[i])
        if row[3] == 999 or row[4] == 999:
            continue
        temDiff = row[4] - row[3]
        if temDiff > maxTemDiff:
            maxTemDiff = temDiff
            larTempvar = row[0]
        if temDiff < minTemDiff:
            minTemDiff = temDiff
            smaTempvar = row[0]            
    f.close()
    
    print("*** Annual Temperature Report for Seoul in 2022***")
    print("Day with the Largest Temperature Variation: {0:s}".format(larTempvar))
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(maxTemDiff))
    print("Day with the Smallest Temperature Variation: {0:s}".format(smaTempvar))
    print("Minimum Temperature Difference: {0:.1f} Celsius".format(minTemDiff))

