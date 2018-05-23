from tkinter import *



##def nothing(e):
##    print(listbox.get(listbox.curselection()))
##

root = Tk()
frame = Frame(root, width = 200, height = 100, relief = SOLID)
frame.place(x = 0, y = 0)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame)
listbox.pack()

for i in range(1, 4):
    listbox.insert(END, i)


for a in range(10):
    print(listbox.get(a))

# attach listbox to scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#listbox.bind("<<ListboxSelect>>", nothing)


mainloop()



