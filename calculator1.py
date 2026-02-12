import tkinter

button_values = [
    ["AC","+/-","%","÷"],
    ["7","8","9","×"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","√","="]

]

right_symbols = ["÷","×","-","+","="]
top_symbols = ["AC","+/-","%"]

row_count = len(button_values) #5
colmn_count = len(button_values[0]) #4



color_light_gray = "#A9A9A9"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk() #create the window
window.title("calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                                             foreground=color_white, anchor="e", width=colmn_count)

label.grid(row=0, column=0, columnspan=colmn_count, sticky="we")

for row in range(row_count):
    for column in range(colmn_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=colmn_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row+1, column=column)
frame.pack()

#A+B, A-B, A*B, A/B

A = "0"
operator = None
B = None

def button_clicked(value):
    global A, B, operator

    current_text = label["text"]

    # DIGITS
    if value in "0123456789":
        if current_text == "0":
            label["text"] = value
        else:
            label["text"] += value

    # DECIMAL
    elif value == ".":
        if "." not in current_text:
            label["text"] += "."

    # OPERATORS
    elif value in ["+", "-", "×", "÷"]:
        A = float(current_text)
        operator = value
        label["text"] = "0"

    # EQUALS
    elif value == "=":
        if operator is not None:
            B = float(current_text)

            try:
                if operator == "+":
                    result = A + B
                elif operator == "-":
                    result = A - B
                elif operator == "×":
                    result = A * B
                elif operator == "÷":
                    result = A / B

                label["text"] = str(result)
                A = result
            except ZeroDivisionError:
                label["text"] = "Error"

            operator = None

    # CLEAR
    elif value == "AC":
        A = "0"
        B = None
        operator = None
        label["text"] = "0"

    # PERCENT
    elif value == "%":
        number = float(current_text)
        label["text"] = str(number / 100)

    # NEGATIVE
    elif value == "+/-":
        if current_text.startswith("-"):
            label["text"] = current_text[1:]
        else:
            if current_text != "0":
                label["text"] = "-" + current_text

    # SQUARE ROOT
    elif value == "√":
        number = float(current_text)
        if number >= 0:
            label["text"] = str(number ** 0.5)
        else:
            label["text"] = "Error"

#center the window
window.update() # update window with the new size dimentions
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenmmwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

#format "(w)×(h)=(x)+(y)"

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()