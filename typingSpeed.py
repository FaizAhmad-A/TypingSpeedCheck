import random
from tkinter import *
from tkinter import ttk
import ttkthemes
import threading
from time import sleep


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('ubuntu')

root.geometry('940x765+300+10')
root.resizable(0,0)
# root.overrideredirect(True)

#----------Functionalities-----------
totalTime = 60
def startToType():
    startBtn.config(state=DISABLED)
    global time
    textArea.config(state=NORMAL)
    textArea.focus()

    for time in range(1,61):
        elapsedTimer.config(text=time)
        remaintime=totalTime-time
        remainingTimer.config(text=remaintime)
        sleep(1)
        root.update()

    textArea.config(state=DISABLED)
    resetBtn.config(state=NORMAL)

time = 0
wrongEnterWords = 0
elapsedTimePerMin = 0
def counts():
    while time!=totalTime:
        typedPara = textArea.get(1.0,END).split()
        totalEnterWords = len(typedPara)
    totalWords.config(text=totalEnterWords)

    global wrongEnterWords
    paraWords = paraLable['text'].split()
    for pairsOfWords in list(zip(paraWords,typedPara)):
        if pairsOfWords[0] != pairsOfWords[1]:
            wrongEnterWords += 1
    wrongWords.config(text=str(wrongEnterWords))

    elapsedTimePerMin = time/60
    wpm = round((totalEnterWords - wrongEnterWords) / elapsedTimePerMin)
    wpmCount.config(text=str(wpm))

    totalWmp = totalEnterWords/elapsedTimePerMin
    accuracyOfWords = round(wpm/totalWmp *100)
    accuracy.config(text=str(accuracyOfWords)+'%')

def resets():
    global time, elapsedTimePerMin
    startBtn.config(state=NORMAL)
    resetBtn.config(state=DISABLED)
    textArea.config(state=NORMAL)
    textArea.delete(1.0,END)
    textArea.config(state=DISABLED)

    elapsedTimer.config(text='0')
    remainingTimer.config(text='0')
    wpmCount.config(text='0')
    accuracy.config(text='0')
    totalWords.config(text='0')
    wrongWords.config(text='0')

def start():
    t1 = threading.Thread(target=startToType)
    t1.start()

    t2 = threading.Thread(target=counts)
    t2.start()


#---------- Graphical user interface ------------
mainFrame = Frame(root,bd=10)
mainFrame.grid(row=0,column=0)

# title
titleFrame = Frame(mainFrame,bd=5,bg='black')
titleFrame.grid(row=0,column=0)

titleLable = Label(titleFrame,text="Check Your Typing Speed",font=('algerian',24,'bold'),bg='green',width=47,fg='white',pady=8)
titleLable.grid(row=0,column=0)

#paragraph
paraFrame = Frame(mainFrame,pady=8)
paraFrame.grid(row=2,column=0)

paraList = ["Nature is the beautiful and complex world around us. It is made up of all the living things on Earth, as well as the non-living things that support them. Nature is constantly changing and evolving, and it is full of surprises One of the most amazing things about nature is its diversity. There are millions of different species of plants and animals, each with its own unique adaptations. Nature is also home to a wide variety of landscapes, from towering mountains to lush rainforests to vast deserts",
            "Islam is an Abrahamic monotheistic religion teaching that there is only one God (Allah), and that Muhammad is a messenger of God. It is the world's second-largest religion with 1.9 billion followers, or 24.9% of the world's population, known as Muslims. Muslims make up a majority of the population in 50 countries. Islam teaches that God is merciful, all-powerful, and unique, and has guided humanity through prophets, revealed scriptures and natural signs. The primary scriptures of Islam are the Quran.",
            "A laptop is a portable personal computer (PC) that can be used in a variety of locations. Laptops are designed to have the same functionality as a desktop computer, including the ability to run the same software and open the same types of files. However, laptops are usually more expensive than comparable desktop computers. Laptops have an all-in-one design with a built-in monitor, keyboard, touchpad, and speakers. This means that they are fully functional even when no peripherals are connected.",
            "A sea is a large body of saltwater that is partly surrounded by land. There are about 50 seas around the world. The largest sections of the sea are called oceans.The sea plays a very important role in supporting life. It moderates the Earth's climate and has important roles in the water, carbon, and nitrogen cycles. The sea is also home to a wide variety of plants and animals.The sea is a beautiful and mysterious place. It has been a source of inspiration for artists, poets, and writers for centuries."
            ]
random.shuffle(paraList)

paraLable = Label(paraFrame,text=paraList[0],wraplength=900,justify=LEFT,font=('arial',14,'bold'))
paraLable.grid()

#textbox
textFrame = Frame(mainFrame)
textFrame.grid(row=3,column=0)

textArea = Text(textFrame,width=100,height=10,font=('arial',13,'bold'),relief=GROOVE,wrap='word',state=DISABLED)
textArea.grid()

#outputs
outputsFrame = Frame(mainFrame)
outputsFrame.grid(row=4,column=0)

elapsedTime = Label(outputsFrame,text="Elapsed Time=",fg='red',font=('bold',14))
elapsedTime.grid(row=0,column=0)
elapsedTimer = Label(outputsFrame,text="0",font=('bold',14))
elapsedTimer.grid(row=0,column=1)

remainingTime = Label(outputsFrame,text=" Remaining Time=",fg='red',font=('bold',14))
remainingTime.grid(row=0,column=3)
remainingTimer = Label(outputsFrame,text="0",font=('bold',14))
remainingTimer.grid(row=0,column=4)

wpmLable = Label(outputsFrame,text=" WPM=",fg='red',font=('bold',14))
wpmLable.grid(row=0,column=5)
wpmCount = Label(outputsFrame,text="0",font=('bold',14))
wpmCount.grid(row=0,column=6)

accuracyLable = Label(outputsFrame,text=" Accuracy=",fg='red',font=('bold',14))
accuracyLable.grid(row=0,column=7)
accuracy= Label(outputsFrame,text="0",font=('bold',14))
accuracy.grid(row=0,column=8)

totalWordsLable = Label(outputsFrame,text=" Total Words=",fg='red',font=('bold',14))
totalWordsLable.grid(row=0,column=9)
totalWords = Label(outputsFrame,text="0",font=('bold',14))
totalWords.grid(row=0,column=10)

wrongWordsLable = Label(outputsFrame,text=" Wrong Words=",fg='red',font=('bold',14))
wrongWordsLable.grid(row=0,column=11)
wrongWords = Label(outputsFrame,text="0",font=('bold',14))
wrongWords.grid(row=0,column=12)

#Buttons
buttonFrame = Frame(mainFrame)
buttonFrame.grid(row=5,column=0)

startBtn = ttk.Button(buttonFrame,text="Start",command=start)
startBtn.grid(row=0,column=0,padx=10)

resetBtn = ttk.Button(buttonFrame,text="Reset",state=DISABLED,command=resets)
resetBtn.grid(row=0,column=1,padx=10)

exitBtn = ttk.Button(buttonFrame,text="Exit",command=root.destroy)
exitBtn.grid(row=0,column=2,padx=10)

#Keyboard
keyBoardFrame = Frame(mainFrame,pady=10)
keyBoardFrame.grid(row=6,column=0)

keyborad1to0 = Frame(keyBoardFrame,pady=2)
keyborad1to0.grid(row=0,column=0)

lable1 = Label(keyborad1to0,text='1',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable1.grid(row=0,column=0,padx=2)
lable2 = Label(keyborad1to0,text='2',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable2.grid(row=0,column=1,padx=2)
lable3 = Label(keyborad1to0, text='3', font=('arial', 10, 'bold'), fg='white', relief=GROOVE, bg='black', height=2,width=5, bd=5)
lable3.grid(row=0, column=2, padx=2)
lable4 = Label(keyborad1to0, text='4', font=('arial', 10, 'bold'), fg='white', relief=GROOVE, bg='black', height=2,width=5, bd=5)
lable4.grid(row=0, column=3, padx=2)
lable5 = Label(keyborad1to0,text='5',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable5.grid(row=0,column=4,padx=2)
lable6 = Label(keyborad1to0,text='6',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable6.grid(row=0,column=5,padx=2)
lable7 = Label(keyborad1to0,text='7',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable7.grid(row=0,column=6,padx=2)
lable8 = Label(keyborad1to0,text='8',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable8.grid(row=0,column=7,padx=2)
lable9 = Label(keyborad1to0,text='9',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable9.grid(row=0,column=8,padx=2)
lable0 = Label(keyborad1to0,text='0',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lable0.grid(row=0,column=9,padx=2)

keyboradQtoP = Frame(keyBoardFrame,pady=2)
keyboradQtoP.grid(row=1,column=0)

lableQ = Label(keyboradQtoP,text='Q',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableQ.grid(row=0,column=0,padx=2)
lableW = Label(keyboradQtoP,text='W',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableW.grid(row=0,column=1,padx=2)
lableE = Label(keyboradQtoP,text='E',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableE.grid(row=0,column=2,padx=2)
lableR = Label(keyboradQtoP,text='R',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableR.grid(row=0,column=3,padx=2)
lableT = Label(keyboradQtoP,text='T',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableT.grid(row=0,column=4,padx=2)
lableY = Label(keyboradQtoP,text='Y',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableY.grid(row=0,column=5,padx=2)
lableU = Label(keyboradQtoP,text='U',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableU.grid(row=0,column=6,padx=2)
lableI = Label(keyboradQtoP,text='I',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableI.grid(row=0,column=7,padx=2)
lableO = Label(keyboradQtoP,text='O',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableO.grid(row=0,column=8,padx=2)
lableP = Label(keyboradQtoP,text='P',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableP.grid(row=0,column=9,padx=2)

keyboradAtoL = Frame(keyBoardFrame,pady=2)
keyboradAtoL.grid(row=2,column=0)

lableA = Label(keyboradAtoL,text='A',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableA.grid(row=0,column=0,padx=2)
lableS = Label(keyboradAtoL,text='S',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableS.grid(row=0,column=1,padx=2)
lableD = Label(keyboradAtoL,text='D',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableD.grid(row=0,column=2,padx=2)
lableF = Label(keyboradAtoL,text='F',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableF.grid(row=0,column=3,padx=2)
lableG = Label(keyboradAtoL,text='G',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableG.grid(row=0,column=4,padx=2)
lableH = Label(keyboradAtoL,text='H',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableH.grid(row=0,column=5,padx=2)
lableJ = Label(keyboradAtoL,text='J',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableJ.grid(row=0,column=6,padx=2)
lableK = Label(keyboradAtoL,text='K',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableK.grid(row=0,column=7,padx=2)
lableL = Label(keyboradAtoL,text='L',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableL.grid(row=0,column=8,padx=2)

keyboradZtoM = Frame(keyBoardFrame,pady=2)
keyboradZtoM.grid(row=3,column=0)

lableZ = Label(keyboradZtoM,text='Z',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableZ.grid(row=0,column=0,padx=2)
lableX = Label(keyboradZtoM,text='X',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableX.grid(row=0,column=1,padx=2)
lableC = Label(keyboradZtoM,text='C',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableC.grid(row=0,column=2,padx=2)
lableV = Label(keyboradZtoM,text='V',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableV.grid(row=0,column=3,padx=2)
lableB = Label(keyboradZtoM,text='B',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableB.grid(row=0,column=4,padx=2)
lableN = Label(keyboradZtoM,text='N',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableN.grid(row=0,column=5,padx=2)
lableM = Label(keyboradZtoM,text='M',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=5,bd=5)
lableM.grid(row=0,column=6,padx=2)

spaceFrame = Frame(keyBoardFrame)
spaceFrame.grid(row=4,column=0)
labelSpace = Label(spaceFrame,text='Space',font=('arial',10,'bold'),fg='white', relief=GROOVE,bg='black',height=2,width=35,bd=5)
labelSpace.grid(row=0,column=0)

lableNumbers = [lable1,lable2,lable3,lable4,lable5,lable6,lable7,lable8,lable9,lable0]
lableAlpha = [lableA,lableB,lableC,lableD,lableE,lableF,lableG,lableH,lableI,lableJ,lableK,lableL,lableM,lableN,lableO,lableP,lableQ,lableR,lableS,lableT,lableU,lableV,lableW,lableX,lableY,lableZ]

bindingNums = ['1','2','3','4','5','6','7','8','9','0']
bindingCapAlpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
bindingSmAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Color change logic
def changeClr(lable):
    lable.config(bg='green')
    lable.after(100, lambda l=lable: l.config(bg='black'))

for num in range(len(bindingNums)):
    root.bind(bindingNums[num], lambda event, lable=lableNumbers[num]: changeClr(lable))
for num in range(len(bindingCapAlpha)):
    root.bind(bindingCapAlpha[num],lambda event, lable=lableAlpha[num]:changeClr(lable))
for num in range(len(bindingSmAlpha)):
    root.bind(bindingSmAlpha[num],lambda event, lable=lableAlpha[num]:changeClr(lable))
root.bind("<space>", lambda event:changeClr(labelSpace))


root.mainloop()
