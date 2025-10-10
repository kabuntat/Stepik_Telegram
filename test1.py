from tkinter import ttk
import tkinter
import  time

root = tkinter.Tk()
root.geometry("300x300+150+150")



def sleep_func():
    time.sleep(5)
    lab['text'] += 10

btn = ttk.Button(root, text='Run', command=sleep_func)
btn.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

lab = ttk.Label(root, text=0)
lab.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


root.mainloop()