import tkinter as tk
window=tk.Tk()
window.title("Sentence Reverser")

heading_label=tk.Label(window, text="Enter the sentence")
heading_label.pack()

sen_feild=tk.Entry(window)
sen_feild.pack()

def reverse(k):
    s = []
    token = k.split()
    for word in token:
        s.append(word)

    while (len(s)):
        out = []
        out.append(s.pop())
        # out = tk.Text(window, s.pop(), end=" " )
        # out.pack()
        o = tk.Label(window, text=str(out))
        o.pack()
        #s.pop(), end=" "

button = tk.Button(window, text="Find Reverse", command=lambda: reverse(sen_feild.get()))
button.pack()

window.mainloop()
