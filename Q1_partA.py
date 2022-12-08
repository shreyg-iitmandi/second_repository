import pandas as pd
# Use pandas to read the CSV
csvData = pd.read_csv('Data.csv',sep=',')
# Convert dataframe into a numpy array
csvDataNum = csvData[['State','A','B','C','D','E','F','G','H','I','J','K']].to_numpy()
# Convert numpy array into a list (of lists)
data = csvDataNum.tolist()
# Access values as usual from data # For eg. data[0][3] is 25 print(data[0][3])

#Functions
def Highest(column):
    x = 0
    max = data[0][column]
    for i in range (12):
        if data[i][column] > max:
            max = data[i][column]
            x = i
    return data[x][0]

def Lowest(column):
    x = 0
    min = data[0][column]
    for i in range (12):
        if data[i][column] < min:
            min = data[i][column]
            x = i
    return data[x][0]

def Median(column):
    someonesList = []
    for i in range (12):
        someonesList.append(data[i][column])
    someonesList.sort()
    return someonesList[6]

def Average(column):
    sum = 0
    for i in range (12):
        sum = sum + data[i][column]
    return sum/12

def Mode(column):
    someonesList = []
    mode = 0
    max = 0
    for i in range (12):
        someonesList.append(data[i][column])
    for i in range (12):
        temp = someonesList[i]
        count = 0
        for j in range (12):
            if (temp == someonesList[j]): 
                count += 1
        if count > max:
            max = count
            mode = someonesList[i]
    return mode

#Part A
print("State with Highest Population Density:", Highest(6))
print("State with Lowest Population Density:", Lowest(6))
print("Median Population Density:", Median(6))
print("Average Population Density:", Average(6))
print("Mode of Population Density:", Mode(6))
print()

print("State with Highest Percentage of Marginal Farmers:", Highest(7))
print("State with Lowest Percentage of Marginal Farmers:", Lowest(7))
print("Median Percentage of Marginal Farmers:", Median(7))
print("Average Percentage of Marginal Farmers:", Average(7))
print("Mode of Percentage of Marginal Farmers:", Mode(7))
print()

print("State with Highest Percentage of Women in the Overall Workforce:", Highest(11))
print("State with Lowest Percentage of Women in the Overall Workforce:", Lowest(11))
print("Median Percentage of Women in the Overall Workforce:", Median(11))
print("Average Percentage of Women in the Overall Workforce:", Average(11))
print("Mode of Percentage of Women in the Overall Workforce:", Mode(11))