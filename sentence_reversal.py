import tkinter as tk
window=tk.Tk()
window.title("Sentence Reverser")

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

button = tk.Button(mainWindow, text="Find Reverse", command=lambda: reverse(sen_feild.get()))
button.pack()

window.mainloop()
