import tkinter as tk
from csv import writer
app = tk.Tk(__name__)
app.title("Form")
app.geometry("300x300")

name = tk.Variable(app)
name.set('')

email = tk.Variable(app)
email.set('')

mobnum = tk.Variable(app)
mobnum.set('')

tk.Label(app,text="Name").place(x=0,y=0)
tk.Entry(app,textvariable=name,font = ('Arial',15)).place(x=0,y=20)

tk.Label(app,text="E-Mail").place(x=0,y=50)
tk.Entry(app,textvariable=email,font = ('Arial',15)).place(x=0,y=70)

tk.Label(app,text="Mobile Number").place(x=0,y=100)
tk.Entry(app,textvariable=mobnum,font = ('Arial',15)).place(x=0,y=120)

def file_entry(n,e,m):
    with open('data_form.csv','a') as f:
        w = writer(f)
        w.writerow([n,e,m])
        f.close()

def Submit():
    Name = name.get()
    Email = email.get()
    mnum = mobnum.get()
    file_entry(Name,Email,mnum)
    print("Data Submitted successfully")
    name.set('')
    email.set('')
    mobnum.set('')
    
tk.Button(app,text="Submit",command = Submit).place(x=100,y=150)

app.mainloop()
