#!/usr/bin/env python3
import tkinter as tk
import Instructions_editor
import ServerStart

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='replace, append, or clear:')
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 95, window=label1)

label2 = tk.Label(root, text='bots seperated by commas:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 145, window=label2)

label3 = tk.Label(root, text='commands seperated by commas:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 195, window=label3)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 120, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 170, window=entry2)

entry3 = tk.Entry (root) 
canvas1.create_window(200, 220, window=entry3)

def instruct():
    
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()

    Instructions_editor.main(x1,x2,x3)
    
def startserver():
    ServerStart.main()


button1 = tk.Button(text='Start Server', command=startserver, bg='brown', fg='white', font=('helvetica', 20, 'bold'))
canvas1.create_window(200, 30, window=button1)
    
button2 = tk.Button(text='Change Instructions', command=instruct, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 250, window=button2)

root.mainloop()
