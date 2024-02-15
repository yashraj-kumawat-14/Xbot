from filtrate import filtrate
import json

with open(r"D:\projects\python projects\Xbot\data.txt", "r") as file:
        dataset = file.read()
        file.close()

data = json.loads(dataset)
datakeys = list(data.keys())
print(datakeys)
userInput = "start"
while(userInput.lower()!="quiet"):
    userInput = input("you : ")
    filterInputlist = filtrate(userInput)
    matchValue = []
    for i in range(len(data)):
        count=0
        for j in range(len(filterInputlist)):
            if(filterInputlist[j] in datakeys[i]):
                count+=1
        matchPercentage = (count/len(datakeys[i].split(" ")))*100
        matchValue.append(matchPercentage)
    maxMatch = max(matchValue)
    maxMatchIndex = matchValue.index(maxMatch)
    outputValue = data[datakeys[maxMatchIndex]]
    print(outputValue)
    


