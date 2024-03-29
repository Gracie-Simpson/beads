import tkinter as tk
from patternLogic import advance, regress, advance_row, regress_row, jump_to_row
from patternReader import patternReader, read_input_from_file, trackerReader, trackerUpdate


#turn a string into a cleaned up useable matrix
matrix = patternReader(read_input_from_file('smallBlue.txt'))


start_row, row_block = trackerReader()   #get the current row and max row from the tracker file
past_row = current_row = future_row = int(start_row) - 1
past_column = current_column = future_column = len(matrix[current_row]) - 1
past = current = future = matrix[current_row][current_column]

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
past_label = tk.Label(patternDisplay, textvariable=past_val, font=("Helvetica", 15), bg='black')
current_label = tk.Label(patternDisplay, textvariable=current_val, font=("Helvetica", 25), bg='black')
future_label = tk.Label(patternDisplay, textvariable=future_val , font=("Helvetica", 15), bg='black')
row_label = tk.Label(patternDisplay, text="Row: ", bg='black', fg='white')
row_label.grid(row = 0, column=1, padx=40, pady=20)
past_label.grid(row = 1, column = 0, padx=40, pady=20)  
current_label.grid(row = 1, column = 1, padx=40, pady=20)  
future_label.grid(row = 1, column = 2, padx=40, pady=20)  
start_row_label = tk.Label(patternDisplay, text= "Start row: " + str(start_row), bg='black', fg='white')
row_block_label = tk.Label(patternDisplay, text= "Rows: " + str(row_block), bg='black', fg='white')
start_row_label.grid(row=0, column=0, padx=40, pady=20)
row_block_label.grid(row=0, column=2, padx=40, pady=20)



def update_colors(item, label):
    if 'D' in item:
        label.config(fg= '#30b0ff')  # Blue text
    elif 'A' in item:
        label.config(fg= '#ffffff')  # White text
    elif 'C' in item:
        label.config(fg= '#ff0000')  # Red Text
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

def jump_row():
    global matrix, future_row, future_column, current_row, current_column, past_row, past_column, past, current, future
    # Get the text from the entry field
    entry_text = jump_entry.get()
    # Remove any non-numeric characters
    numeric_text = ''.join(c for c in entry_text if c.isdigit())
    # Convert the remaining text to an integer
    new_row = int(numeric_text)
    # Clear the entry field
    jump_entry.delete(0, 'end')
    #actually update rows
    current_row, past_column, current_column, future_column = jump_to_row(matrix, current_row, new_row, past_column, current_column, future_column)
    #update rest of row and col values
    past = current = future = matrix[current_row][past_column]
    past_row = future_row = current_row
    update_labels()

def update_tracker_info():

    if((len(tracker_entry.get().split(", ")) == 2) and (tracker_entry.get().split(", ")[0].isdigit()) and (int(tracker_entry.get().split(", ")[0]) < len(matrix))):
        print("updating tracker")
        trackerUpdate(tracker_entry.get())
        tracker_entry.delete(0, 'end')
        start_row, row_block = trackerReader()
        start_row_label.config(text= "Start row: " + str(start_row))
        row_block_label.config(text= "Rows: " + str(row_block))

#set window size
patternDisplay.geometry("520x420")


# create entry label for a spot to input what row you want to jump to 
jump_label = tk.Label(patternDisplay, text="Jump to row:",  bg='black', fg='white')
jump_label.grid(row=4, column=0, padx=40, pady=20)

# create entry label for a way to update tracker
tracker_update_label = tk.Label(patternDisplay, text="Update tracker:",  bg='black', fg='white')
tracker_update_label.grid(row=5, column=0, padx=40, pady=20)

#create tracker entry field
tracker_entry = tk.Entry(patternDisplay)
tracker_entry.grid(row=5, column=1, padx=40, pady=20)

#create tracker entry button
tracker_button = tk.Button(patternDisplay, text="Enter", command=update_tracker_info, bg='#3d3d3d', fg='white')
tracker_button.grid(row=5, column=2, padx=40, pady=20)

# Create the entry field
jump_entry = tk.Entry(patternDisplay)
jump_entry.grid(row=4, column=1, padx=40, pady=20)

#button to enter row value
enter_button = tk.Button(patternDisplay, text="Enter", command=jump_row, bg='#3d3d3d', fg='white')
enter_button.grid(row=4, column=2, padx=40, pady=20)

# Create a button to trigger the regress function
next_button = tk.Button(patternDisplay, text="Next", command=next_item, bg='#3d3d3d', fg='white')
next_button.grid(row = 2, column = 2, padx=40, pady=20)

# Create a button to trigger the advance function
previous_button = tk.Button(patternDisplay, text="previous", command=past_item, bg='#3d3d3d', fg='white')
previous_button.grid(row = 2, column = 0, padx=40, pady=20)

#create a button to skip to the next row
next_row_button = tk.Button(patternDisplay, text = "Next Row", command=next_row, bg='#3d3d3d', fg='white')
next_row_button.grid(row=3, column=2, padx=40, pady=20)

#create a button to skip to the previous row
past_row_button = tk.Button(patternDisplay, text = "previous Row", command=previous_row, bg='#3d3d3d', fg='white')
past_row_button.grid(row=3, column=0, padx=40, pady=20)
