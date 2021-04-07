f = open("C:/Users/User/fyers/interview/airlines.csv", "r");
readList = f.readlines();

readList.__delitem__(0); #delete column headings

# print(readList[0].split(",")[1]);
# print(readList[1].split(",")[2]);

# airportName = readList[0].split(",")[1] + readList[0].split(",")[2];

airportDict = {};

for i in readList:
    temp_list = i.split(",");
    airportName = temp_list[1].strip() + temp_list[2].strip();
    # print(airportName in airportDict.keys());

    if airportName in airportDict.keys():
        count = airportDict[airportName];
        count += 1;
        airportDict[airportName] = count;
    else:
        airportDict[airportName] = 1;

# print(airportDict);

#Output1 : printing number of occurences of each airport
for name in airportDict:
    print(name+":"+" "+str(airportDict[name]));

#printing the most mentioned and least mentioned airport
sortedDict = sorted(airportDict.items(), key=lambda item: item[1]);
leastOccuredName = sortedDict[0][0];
leastOccuredCount = str(sortedDict[0][1]);
mostOccuredName = sortedDict[len(sortedDict) - 1][0];
mostOccuredCount = str(sortedDict[len(sortedDict) - 1][1]);
print("\nMost occurred airport is "+mostOccuredName+" : "+mostOccuredCount+" times");
print("Least airport is "+leastOccuredName+" : "+leastOccuredCount+" times");


