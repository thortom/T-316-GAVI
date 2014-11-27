import csv

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

years = []
months = []
dataForYear = []
data = []
with open('Gistingar.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if '2014' in row:
            for year in row:
                if year != '' and year != ' ':
                    years.append(year)
        elif 'Janúar' in row:
            for idx, month in enumerate(row):
                if idx >= 12:
                    break
                if month != '' and month != ' ':
                    months.append(month)
        else:
            for idx, number in enumerate(row):
                if isNumber(number):
                    dataForYear.append(number)
                elif number == '..':
                    dataForYear.append('nan')
                else:
                    continue
                if idx%12 == 0:
                      data.append(dataForYear)
                      dataForYear = []

# print('years = ', years)
# print('months = ', months)
# print('data = ', data)

dataArray = []
for idx, year in enumerate(years):
    temp = data[idx]
    temp.insert(0, year)
    dataArray.append(temp)

for data in dataArray:
    print(data[0])
    print(data[1:len(data)])
    print()
