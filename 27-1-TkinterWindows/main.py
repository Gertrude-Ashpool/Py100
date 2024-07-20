import tkinter

# initiate an instance for the TK() object as window
window = tkinter.Tk()
# give the window a title
window.title("My First GUI Program")
# determine the minimum size of the window
window.minsize(width=500, height=300)

# Create Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# lay out the label to center
my_label.pack()

# have window class call mainloop to listen to the screen
# this line has to be at the end of the program
window.mainloop()