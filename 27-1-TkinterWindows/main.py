import tkinter

def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)


# initiate an instance of the Tk() object as window
window = tkinter.Tk()
# give the window a title
window.title("My First GUI Program")
# determine the minimum size of the window
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Create Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# change properties after object creation
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=20, pady=20)
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Button", command=button_clicked)
button.grid(column=1, row=1)
# Button
new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)

# have window class call mainloop to listen to the screen
# this line has to be at the end of the program
window.mainloop()