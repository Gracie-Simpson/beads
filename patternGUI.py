import tkinter as tk
from patternLogic import advance, regress, advance_row, regress_row
from patternReader import patternReader, read_input_from_file


#turn a string into a cleaned up useable matrix
matrix = patternReader(read_input_from_file('bagStrap.txt'))


past = current = future = matrix[-1][-1]
past_row = current_row = future_row = len(matrix)-1
past_column = current_column =future_column = len(matrix[len(matrix)-1])-1

#create a window to display info
patternDisplay = tk.Tk()
patternDisplay.title("Pattern Displayer")
patternDisplay.configure(bg='black')

# Create a StringVar to store the variable's value
past_val = tk.StringVar()
current_val = tk.StringVar()
future_val = tk.StringVar()
row_val = tk.StringVar()
row_text = tk.StringVar()

#initialize the values
past_val.set(past)
current_val.set(current)
future_val.set(future)
row_val.set(current_row)
row_text.set('row')

# Create a Label widget to display the variable's value
past_label = tk.Label(patternDisplay, textvariable=past_val, font=("Helvetica", 10), bg='black')
current_label = tk.Label(patternDisplay, textvariable=current_val, font=("Helvetica", 14), bg='black')
future_label = tk.Label(patternDisplay, textvariable=future_val , font=("Helvetica", 10), bg='black')
row_label = tk.Label(patternDisplay, text="Row: ", bg='black', fg='white')
row_label.grid(row = 0, column=1, padx=10, pady=10)
past_label.grid(row = 1, column = 0, padx=10, pady=10)  
current_label.grid(row = 1, column = 1, padx=10, pady=10)  
future_label.grid(row = 1, column = 2, padx=10, pady=10)  


def update_colors(item, label):
    if 'C' in item:
        label.config(fg='#30b0ff')  # Blue text
    elif 'A' in item:
        label.config(fg='white')  # White text
    else:
        label.config(fg='Black')  # black text


def update_labels():
    global past, current, future, past_label, current_label, future_label, current_row
    # Set a value for the variable
    past_val.set(past)
    current_val.set(current)
    future_val.set(future)
    row_label.config(text = "Row: " + str(current_row + 1))
    update_colors(current, current_label)
    update_colors(past, past_label)
    update_colors(future, future_label)

def next_item():
    global past, current, future, future_row, future_column, current_row, current_column, past_row, past_column
    row, column = regress(matrix, future_row, future_column)
    past = current
    current = future
    future = matrix[row][column]
    past_row = current_row
    past_column = current_column
    current_row = future_row
    current_column = future_column
    future_row = row
    future_column = column
    update_labels()


def past_item():
    global past, current, future, future_row, future_column, current_row, current_column, past_row, past_column
    row, column = advance(matrix, past_row, past_column)
    future = current
    current = past
    past = matrix[row][column]
    future_row = current_row
    future_column = current_column
    current_row = past_row
    current_column = past_column
    past_row = row
    past_column = column
    update_labels()

def next_row():
    global matrix, future_row, future_column, current_row, current_column, past_row, past_column, past, current, future
    current_row, past_column, current_column, future_column = regress_row(matrix, current_row, past_column, current_column, future_column)
    past_row = future_row = current_row
    past = current = future = matrix[current_row][past_column]
    update_labels()

def previous_row():
    global matrix, future_row, future_column, current_row, current_column, past_row, past_column, past, current, future
    current_row, past_column, current_column, future_column = advance_row(matrix, current_row, past_column, current_column, future_column)
    past_row = future_row = current_row
    past = current = future = matrix[current_row][past_column]
    update_labels()

#set window size
patternDisplay.geometry("300x200")



# Create a button to trigger the regress function
next_button = tk.Button(patternDisplay, text="Next", command=next_item, bg='#3d3d3d', fg='white')
next_button.grid(row = 2, column = 1, padx=10, pady=10)

# Create a button to trigger the advance function
previous_button = tk.Button(patternDisplay, text="previous", command=past_item, bg='#3d3d3d', fg='white')
previous_button.grid(row = 2, column = 0, padx=10, pady=10)

#create a button to skip to the next row
next_row_button = tk.Button(patternDisplay, text = "Next Row", command=next_row, bg='#3d3d3d', fg='white')
next_row_button.grid(row=3, column=1, padx=10, pady=10)

#create a button to skip to the previous row
past_row_button = tk.Button(patternDisplay, text = "previous Row", command=previous_row, bg='#3d3d3d', fg='white')
past_row_button.grid(row=3, column=0, padx=10, pady=10)