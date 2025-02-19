#Dudu KABAKÇI 


#TASK-1

text = input("Enter the text: ")
newText = text.strip().upper().replace("A","E")
wordList = newText.split()
print("New text: ",newText)
print("Word list: ",wordList)
print("**************************************")


#TASK-2

text2 = "Python programlama dili"
print("Text :",text2)
reversedText = text2[::-1]
print("Reverses text: ",reversedText)

newText2 = reversedText.replace("amalmargorp","amaldok")
print("Modified text: ",newText2)

finalText = newText2[::-1]
print("Final text: ",finalText)
