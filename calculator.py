from tkinter import *
from tkinter import messagebox

root = Tk()
height = 440
width = 280
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.overrideredirect(True)

main_frame = Frame(root, relief=SUNKEN, bg="light grey", width=640, height=670)
main_frame.place(x=0, y=0)

frame1 = Frame(main_frame, width=280, bg="light grey", height=900)
frame1.place(x=0, y=0)
            
fA = Frame(frame1, width=280, bg="light grey", height=370)
fA.place(x=0, y=0)

fA2 = Frame(fA, width=280, bg="light grey", height=370)
fA2.place(x=0, y=0)

fC = Frame(frame1, width=700, bg="light grey", height=70)
fC.place(x=0, y=370)

def exit_app():
    if messagebox.askyesno('Exit', 'Are you sure you want to exit?'):root.destroy()
        
lblCalculator = LabelFrame(fA2, font=('arial', 10, 'bold'), fg="black", bg="light grey", width=280, height=370,
                                       text="calculator")
lblCalculator.place(x=0, y=0)

text_Input = StringVar()

txtDisplay = Entry(lblCalculator, width=17, font=('arial', 20), textvariable=text_Input, bd=1, bg="yellow",
                               justify='right')
txtDisplay.place(x=7, y=7)

def btnclick(numbers):
                current = text_Input.get()
                text_Input.set(current + str(numbers))
def btnClearDisplay():
                text_Input.set("")

def btnEqualsInput():
                try:
                    result = str(eval(text_Input.get()))
                    text_Input.set(result)
                except:
                    messagebox.showerror("Error", "Invalid input")

Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), relief="raised", width=3,
                   text="7", bg="light grey", command=lambda: btnclick(7)).place(x=7, y=45)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="8",
                   bg="light grey", command=lambda: btnclick(8)).place(x=70, y=45)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="9",
                   bg="light grey", command=lambda: btnclick(9)).place(x=132, y=45)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="+",
                   bg="light grey", command=lambda: btnclick("+")).place(x=200, y=45)

Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="4",
                   bg="light grey", command=lambda: btnclick(4)).place(x=7, y=110)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="5",
                   bg="light grey", command=lambda: btnclick(5)).place(x=70, y=110)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="6",
                   bg="light grey", command=lambda: btnclick(6)).place(x=132, y=110)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="-",
                   bg="light grey", command=lambda: btnclick("-")).place(x=200, y=110)

Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="1",
                   bg="light grey", command=lambda: btnclick(1)).place(x=7, y=175)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="2",
                   bg="light grey", command=lambda: btnclick(2)).place(x=70, y=175)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="3",
                   bg="light grey", command=lambda: btnclick(3)).place(x=132, y=175)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="x",
                   bg="light grey", command=lambda: btnclick("*")).place(x=200, y=175)

Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="0",
                   bg="light grey", command=lambda: btnclick(0)).place(x=7, y=240)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text=".",
                   bg="light grey", command=lambda: btnclick(".")).place(x=70, y=240)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="C",
                   bg="light grey", command=btnClearDisplay).place(x=132, y=240)
Button(lblCalculator, padx=9, pady=9, bd=2, fg="black", font=('arial', 15, 'bold'), width=3, text="/",
                   bg="light grey", command=lambda: btnclick("/")).place(x=200, y=240)
Button(lblCalculator, padx=5, pady=5, bd=2, fg="black", font=('arial', 15, 'bold'), width=20, text="=",
                   bg="light grey", command=btnEqualsInput).place(x=7, y=300)

Button(fC, padx=16, pady=8, bd=1, fg="purple", font=('arial', 10, 'bold'), activebackground="red", width=10,
                   text="EXIT", bg="grey", command=exit_app).place(x=85, y=15)
root.mainloop()
                