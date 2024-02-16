from tkinter import *
from filtrate import filtrate
import json, time, pyttsx3

with open(r"D:\projects\python projects\Xbot\data.txt", "r") as file:
        dataset = file.read()
        file.close()

data = json.loads(dataset)
datakeys = list(data.keys())

message_history = []
compResponse = ""
userAns = ""

def history():
    userValue = message_history[len(message_history)-2]
    compValue = message_history[len(message_history)-1]
    listbox.insert(END, f"{userValue[0]}: {userValue[1]}")
    listbox.insert(END, f"{compValue[0]}: {compValue[1]}")
    root.update()

def logic(userInput):
    global compResponse, userAns
    userAns = userInput
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
    message_history.append(("You", userInput))
    message_history.append(("Comp", outputValue))
    history()
    textArea.delete("1.0", END)
    compResponse = outputValue
    return outputValue

def speak():
        sidebarImage.config(image=smileImage1)
        root.update()
        engine = pyttsx3.init()
        engine.setProperty('volume', int(volVar.get())/100)
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id) if(voiceValue.get()=="female") else (engine.setProperty('voice', voices[0].id))
        engine.setProperty('rate', rateVar.get())
        engine.say(compResponse) if(personValue.get()=="comp") else(engine.say(userAns))
        engine.runAndWait()
        sidebarImage.config(image=smileImage2)

        
root = Tk()
root.minsize(700, 600)
root.title("Xbot")
root.iconbitmap(r"D:\projects\python projects\Xbot\fresh.ico")
bottomFrame = Frame(root, bg='red')
bottomFrame.pack(fill=X, side=BOTTOM)

rightFrame = Frame(root, bg='blue')
rightFrame.pack(fill=Y, side=RIGHT)

leftFrame = Frame(root, bg='grey')
leftFrame.pack(fill=BOTH, expand=True)

sendIcon = PhotoImage(file=r"D:\projects\python projects\Xbot\send.png")
smileImage1 = PhotoImage(file=r"D:\projects\python projects\Xbot\smileImage.png")
smileImage2 = PhotoImage(file=r"D:\projects\python projects\Xbot\smileImage2.png")

sendButton = Button(bottomFrame, image=sendIcon, height=1, font="COPPER 10 bold")
sendButton.pack(side=RIGHT, fill=Y)

textArea = Text(bottomFrame, height=2)
textArea.pack(fill=X)

sendButton.config(command=lambda : logic(textArea.get("1.0", END)))

listbox = Listbox(leftFrame, bg="yellow")
listbox.pack(fill=BOTH, expand=True)

sidebarImage = Label(rightFrame, image=smileImage2)
sidebarImage.pack(side=TOP)

speakButton = Button(rightFrame, text="Speak", command=speak)
speakButton.pack(side=TOP, fill=X)

personValue = StringVar()
personValue.set("comp")

personFrame = Frame(rightFrame, bg='red')
personFrame.pack()

compRadio = Radiobutton(personFrame, text="Computer", variable=personValue, value="comp", bg='blue', anchor="w")
userRadio = Radiobutton(personFrame, text="You", variable=personValue, value="user", bg='blue', anchor="w")
compRadio.pack(side=LEFT)
userRadio.pack(side=LEFT)

volVar = IntVar()
volume = Scale(rightFrame, bg="blue", orient=HORIZONTAL, from_=0, to=100, label="Volume", showvalue=False, length=130, sliderlength=30, variable=volVar)
volume.pack(pady=20)

rateVar = IntVar()
rateVar.set(140)
rate = Scale(rightFrame, bg="blue", orient=HORIZONTAL, from_=30, to=400, label="Rate", showvalue=True, length=130, sliderlength=30, variable=rateVar)
rate.pack(pady=20)

voiceFrame = Frame(rightFrame, bg='red')
voiceFrame.pack()

voiceValue=StringVar()
voiceValue.set("male")

maleRadio = Radiobutton(voiceFrame, text="Male", variable=voiceValue, value="male", bg='blue', anchor="w")
femaleRadio = Radiobutton(voiceFrame, text="Female", variable=voiceValue, value="female", bg='blue', anchor="w")
maleRadio.pack(side=LEFT)
femaleRadio.pack(side=LEFT)


root.mainloop()
