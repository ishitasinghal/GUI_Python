import tkinter as tk
mainWindow=tk.Tk()
mainWindow.title("Sentence Reverser")

heading_label=tk.Label(mainWindow, text="Enter the sentence")
heading_label.pack()

sen_feild=tk.Entry(mainWindow)
sen_feild.pack()

def reverse(k):
    s = []
    token = k.split()
    for word in token:
        s.append(word)

    while (len(s)):
        print(s.pop(), end=" ")

#k = "Let the sentence be reversed"
reverse(sen_feild.get())

button = tk.Button(mainWindow, text="Get Value", command=lambda: reverse())
button.pack()
