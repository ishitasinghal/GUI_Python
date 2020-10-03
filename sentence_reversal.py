import tkinter as tk
import datetime

rowfor = 1
window=tk.Tk()
window.title("Sentence Reverser")
window.resizable(False,True)
heading_label=tk.Label(window, text="Enter the sentence",fg="white",bg="red")
heading_label.grid(row=0,column=0,sticky="nsew")

columnForEntry = tk.Frame(window)
columnForEntry.grid(row=1,column=0,sticky="nsew")
sen_feild=tk.Entry(columnForEntry,width=23,fg="blue",bg="lightblue")
sen_feild.grid(row=0,column=0,sticky="nsew")

SenEntry = tk.Frame(window)
SenEntry.grid(row=2,column=0,sticky="nsew")
senHead = tk.Label(SenEntry,text="Time",width=15,fg="white",bg="blue")
senHead.grid(row=0,column=0,sticky="nsew")
senHead2 = tk.Label(SenEntry,text="Sentence",width=15,fg="white",bg="blue")
senHead2.grid(row=0,column=1,sticky="nsew")

def reverse(k):
    global rowfor
    s = []
    token = k.split()
    for word in token:
        s.append(word)

    while (len(s)):
        time = f"{datetime.datetime.now()}"
        time = time[:-7]
        d = tk.Label(SenEntry, text=time,width=15,fg="blue",bg="lightblue")
        d.grid(row=rowfor,column=0,sticky="nsew")
        o = tk.Label(SenEntry, text=s.pop(),width=15,fg="blue",bg="lightblue")
        o.grid(row=rowfor,column=1,sticky="nsew")
        rowfor += 1

button = tk.Button(columnForEntry, text="Find Reverse",fg="white",bg="green",width=10 ,command=lambda: reverse(sen_feild.get()))
button.grid(row=0,column=1,sticky="nsew")

window.mainloop()
