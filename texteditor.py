import tkinter as tk 
from tkinter.filedialog import askopenfilename, asksaveasfilename

#function to open the file

def open_file():
    filepath=askopenfilename(
        filetypes = [('Text files','*.txt'),('All files','*.*')]
    )
    if not filepath:
        return
    txt_edit.delete(1.0,tk.END)
    with open(filepath,'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END,text)
    window.title(f'Text Editor - {filepath}')

#function to save file

def save_file():
    filepath = asksaveasfilename(
        defaultextension = 'txt',
        filetypes = [('Text files','*.txt'),('All files','*.*')]

    )
    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text = txt_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f'Text Editor - {filepath}')



window = tk.Tk()
window.title('Text Editor')
window.iconbitmap(r'd.ico')
window.rowconfigure(0,minsize=900,weight=1)
window.columnconfigure(1,minsize=900,weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window,relief=tk.RAISED,bd=2)
open_btn = tk.Button(fr_buttons, text = 'Open',command=open_file)
save_btn = tk.Button(fr_buttons, text = 'Save as',command=save_file)

open_btn.grid(row=0,column=0,sticky='ew',padx=5,pady=5)
save_btn.grid(row=1,column=0,sticky='ew',padx=5)
fr_buttons.grid(row=0,column=0,sticky='ns')
txt_edit.grid(row=0,column=1,sticky='nsew')



#function to save file

def save_file():
    filepath = asksaveasfilename(
        defaultextension = 'txt',
        filetypes = [('Text files','*.txt'),('All files','*.*')]

    )
    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text = txt_edit.get(1.0,tk.END)
        output_file.write(text)
    window.title(f'Text Editor - {filepath}')

window.mainloop()