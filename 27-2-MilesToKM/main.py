import tkinter


def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=f"{km}")


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)

miles_input = tkinter.Entry(width=8)
miles_input.insert(0, string="0")
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

button = tkinter.Button(text="Calculate", command=convert)
button.grid(row=2, column=1)


window.mainloop()