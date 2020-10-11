# Calculator

from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    # elif text == '-ve':
    #     scvalue.set("-" + scvalue.get())
    #     screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("310x500")
root.title("Calculator")
root.maxsize(310,500)
#root.configure(background="sky blue")

titlelabel = Label(root, text="Standard", font="constantia 14 bold italic", pady=11)
titlelabel.pack(padx=7, pady=7)

scvalue = StringVar()
scvalue.set(" ")
screen = Entry(root, textvar=scvalue, font="constantia 21 bold", bg="pink")
screen.pack(fill=X, padx=10, pady=11, ipadx=15)
# -------------------------------------------------------------------
f = Frame(root, height=50, width=50)
b = Button(f, text="%", padx=22, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="**", padx=22, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=22, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=22, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack(anchor="nw", pady=11, fill=BOTH)


# -----------------------------------------------------------------------
f = Frame(root, height=50, width=50)
b = Button(f, text="7", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=23, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack(anchor="nw", pady=11)

# -------------------------------------------------------------
f = Frame(root, height=50, width=50)
b = Button(f, text="4", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=23, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack(anchor="nw", pady=11)

# --------------------------------------------------------------
f = Frame(root, height=50, width=50)
b = Button(f, text="1", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=23, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=22, pady=11, font="timesnewroman 11 italic", bg="light grey")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack(anchor="nw", pady=11)

# -----------------------------------------------------------------
f = Frame(root, height=50, width=50)
b = Button(f, text="00", padx=19, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=22, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=24, pady=11, font="timesnewroman 11 italic")
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=24, pady=11, font="timesnewroman 11 italic", bg="sky blue")
b.pack(side=LEFT)
b.bind("<Button-1>", click)
f.pack(anchor="nw", pady=11)









root.mainloop()