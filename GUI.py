#!/usr/bin/env python3
import tkinter as tk
import Instructions_editor
import ServerStart
import subprocess
import os

def main():
    root= tk.Tk()

    canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
    canvas1.pack()

    label4 = tk.Label(root, text='EasyBot')
    label4.config(font=('helvetica', 20))
    canvas1.create_window(200, 40, window=label4)


    label1 = tk.Label(root, text='replace, append, or clear:')
    label1.config(font=('helvetica', 10))
    canvas1.create_window(200, 145, window=label1)

    label2 = tk.Label(root, text='bots seperated by commas:')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(200, 195, window=label2)

    label3 = tk.Label(root, text='commands seperated by commas:')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(200, 245, window=label3)

    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 170, window=entry1)

    entry2 = tk.Entry (root) 
    canvas1.create_window(200, 220, window=entry2)

    entry3 = tk.Entry (root) 
    canvas1.create_window(200, 270, window=entry3)

    def instruct():
        
        x1 = entry1.get()
        x2 = entry2.get()
        x3 = entry3.get()

        Instructions_editor.main(x1,x2,x3)
        
    def startserver():
        proc = subprocess.Popen('./ServerStart.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        
        

    def killserver():
        os.system("pkill python3")



    button1 = tk.Button(text='Start Server', command=startserver, bg='brown', fg='white', font=('helvetica', 20, 'bold'))
    canvas1.create_window(200, 80, window=button1)
        
    button2 = tk.Button(text='Exit', command=killserver, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 120, window=button2)

    button3 = tk.Button(text='Change Instructions', command=instruct, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
    canvas1.create_window(200, 300, window=button3)

    root.mainloop()


if __name__ == '__main__':
    main()
