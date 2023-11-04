import tkinter as tk

# Function to read the input from a file
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Specify the filename
input_filename = 'input.txt'

# Read the input string from the file
input_string = read_input_from_file(input_filename)

# Split the input string into rows using 'Row' as the delimiter
rows = input_string.strip().split('Row ')[1:]

# Initialize the current row index and item index
# Initialize the current row index and item index
current_row_index = len(rows) - 1  # Initialize to the last row index
current_item_index = 0

# Create a Tkinter window
window = tk.Tk()
window.title("Item and Row Display")

# Set the initial window size
window.geometry("400x200")  # Adjust the size as needed

# Set the background color to black
window.configure(bg="black")

# Create a label for displaying the current row with white text
row_label = tk.Label(window, text='', font=("Helvetica", 12), bg="black", fg="white")
row_label.grid(row=0, column=0, padx=20, pady=10, columnspan=3)

# Create a label for displaying the previous item with a smaller font and white text
previous_item_label = tk.Label(window, text='', font=("Helvetica", 8), bg="black", fg="white")
previous_item_label.grid(row=1, column=0, padx=20, pady=5, sticky="w")

# Create a label for displaying the current item with white text
item_label = tk.Label(window, text='', font=("Helvetica", 12), bg="black", fg="white")
item_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")

# Create a label for displaying the next item with font size 8 and white text
next_item_label = tk.Label(window, text='', font=("Helvetica", 8), bg="black", fg="white")
next_item_label.grid(row=1, column=2, padx=20, pady=5, sticky="w")

# Function to advance to the next item
def next_item():
    global current_row_index, current_item_index
    if current_row_index < len(rows):
        row = rows[current_row_index]
        items = [item.strip() for item in row.split(',')]
        if current_row_index % 2 == 1:
            # Odd row, read in reverse
            items = items[::-1]
        # Check if the current item includes (L) or (R) or is blank
        while current_item_index < len(items):
            item = items[current_item_index]
            if '(L)' in item or '(R)' in item or not item:
                current_item_index += 1
            else:
                # Set text color based on item content for the current item label
                if 'B' in item:
                    item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
                elif 'C' in item:
                    item_label.config(text=items[current_item_index], fg='white')  # White text
                else:
                    item_label.config(text=items[current_item_index], fg='white')  # White text
                
                # Set the previous item label with a smaller font
                if current_item_index > 0:
                    previous_item = items[current_item_index - 1]
                    if 'B' in previous_item:
                        previous_item_label.config(text=previous_item, fg='#30b0ff')  # Blue text
                    elif 'C' in previous_item:
                        previous_item_label.config(text=previous_item, fg='white')  # White text
                    else:
                        previous_item_label.config(text=previous_item, fg='white')  # White text
                
                # Set the next item label with font size 8
                if current_item_index < len(items) - 1:
                    next_item = items[current_item_index + 1]
                    if 'B' in next_item:
                        next_item_label.config(text=next_item, font=("Helvetica", 8), fg='#30b0ff')  # Blue text
                    elif 'C' in next_item:
                        next_item_label.config(text=next_item, font=("Helvetica", 8), fg='white')  # White text
                    else:
                        next_item_label.config(text=next_item, font=("Helvetica", 8), fg='white')  # White text
                
                current_item_index += 1
                break
        if current_item_index >= len(items):
            # Move to the next row
            current_row_index -= 1
            current_item_index = 0
            if current_row_index < len(rows):
                row = rows[current_row_index]
                items = [item.strip() for item in row.split(',')]
                if current_row_index % 2 == 1:
                    # Odd row, read in reverse
                    items = items[::-1]
                while current_item_index < len(items):
                    item = items[current_item_index]
                    if '(L)' in item or '(R)' in item or not item:
                        current_item_index += 1
                    else:
                        # Set text color based on item content for both current and next item labels
                        if 'B' in item:
                            item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
                            next_item_label.config(text=items[current_item_index], font=("Helvetica", 8), fg='#30b0ff')  # Blue text
                        elif 'C' in item:
                            item_label.config(text=items[current_item_index], fg='white')  # White text
                            next_item_label.config(text=items[current_item_index], font=("Helvetica", 8), fg='white')  # White text
                        else:
                            item_label.config(text=items[current_item_index], fg='white')  # White text
                            next_item_label.config(text=items[current_item_index], font=("Helvetica", 8), fg='white')  # White text
                        
                        # Set the previous item label with a smaller font
                        if current_item_index > 0:
                            previous_item = items[current_item_index - 1]
                            if 'B' in previous_item:
                                previous_item_label.config(text=previous_item, fg='#30b0ff')  # Blue text
                            elif 'C' in previous_item:
                                previous_item_label.config(text=previous_item, fg='white')  # White text
                            else:
                                previous_item_label.config(text=previous_item, fg='white')  # White text
                        
                        row_label.config(text="Row " + str(current_row_index + 1))
                        current_item_index += 1
                        break
        if current_row_index >= len(rows):
            row_label.config(text="End of Rows")
            item_label.config(text='')
            previous_item_label.config(text='')
            next_item_label.config(text='')


# Function to display the previous item
def previous_item():
    global current_row_index, current_item_index
    if current_row_index < len(rows):
        if current_item_index > 0:
            current_item_index -= 1
            row = rows[current_row_index]
            items = [item.strip() for item in row.split(',')]
            if current_row_index % 2 == 1:
                # Odd row, read in reverse
                items = items[::-1]
            
            # Set text color based on item content for both current and next item labels
            if 'B' in items[current_item_index]:
                item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
                next_item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
            elif 'C' in items[current_item_index]:
                item_label.config(text=items[current_item_index], fg='white')  # White text
                next_item_label.config(text=items[current_item_index], fg='white')  # White text
            else:
                item_label.config(text=items[current_item_index], fg='white')  # White text
                next_item_label.config(text=items[current_item_index], fg='white')  # White text
            
            # Set the previous item label with a smaller font
            if current_item_index > 0:
                previous_item = items[current_item_index - 1]
                if 'B' in previous_item:
                    previous_item_label.config(text=previous_item, fg='#30b0ff')  # Blue text
                elif 'C' in previous_item:
                    previous_item_label.config(text=previous_item, fg='white')  # White text
                else:
                    previous_item_label.config(text=previous_item, fg='white')  # White text
        else:
            # If at the beginning of the row, move to the previous row
            if current_row_index > 0:
                current_row_index -= 1
                row = rows[current_row_index]
                items = [item.strip() for item in row.split(',')]
                if current_row_index % 2 == 1:
                    # Odd row, read in reverse
                    items = items[::-1]
                
                # Set text color based on item content for both current and next item labels
                if 'B' in items[-1]:
                    item_label.config(text=items[-1], fg='#30b0ff')  # Blue text
                    next_item_label.config(text=items[-1], fg='#30b0ff')  # Blue text
                elif 'C' in items[-1]:
                    item_label.config(text=items[-1], fg='white')  # White text
                    next_item_label.config(text=items[-1], fg='white')  # White text
                else:
                    item_label.config(text=items[-1], fg='white')  # White text
                    next_item_label.config(text=items[-1], fg='white')  # White text
                
                # Set the previous item label with a smaller font
                if len(items) > 1:
                    if 'B' in items[-2]:
                        previous_item_label.config(text=items[-2], fg='#30b0ff')  # Blue text
                    elif 'C' in items[-2]:
                        previous_item_label.config(text=items[-2], fg='white')  # White text
                    else:
                        previous_item_label.config(text=items[-2], fg='white')  # White text
                
            row_label.config(text="Row " + str(current_row_index + 1))


# Function to skip to the next row
def next_row():
    global current_row_index, current_item_index
    current_row_index -= 1
    current_item_index = 0
    if current_row_index < len(rows):
        row = rows[current_row_index]
        items = [item.strip() for item in row.split(',')]
        if current_row_index % 2 == 1:
            # Odd row, read in reverse
            items = items[::-1]
        while current_item_index < len(items):
            item = items[current_item_index]
            if '(L)' in item or '(R)' in item or not item:
                current_item_index += 1
            else:
                # Set text color based on item content for both current and next item labels
                if 'B' in item:
                    item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
                    next_item_label.config(text=items[current_item_index], fg='#30b0ff')  # Blue text
                elif 'C' in item:
                    item_label.config(text=items[current_item_index], fg='white')  # White text
                    next_item_label.config(text=items[current_item_index], fg='white')  # White text
                else:
                    item_label.config(text=items[current_item_index], fg='white')  # White text
                    next_item_label.config(text=items[current_item_index], fg='white')  # White text
                
                # Set the previous item label with a smaller font
                if current_item_index > 0:
                    previous_item = items[current_item_index - 1]
                    if 'B' in previous_item:
                        previous_item_label.config(text=previous_item, fg='#30b0ff')  # Blue text
                    elif 'C' in previous_item:
                        previous_item_label.config(text=previous_item, fg='white')  # White text
                    else:
                        previous_item_label.config(text=previous_item, fg='white')  # White text
                
                row_label.config(text="Row " + str(current_row_index + 1))
                current_item_index += 1
                break
    else:
        row_label.config(text="End of Rows")
        item_label.config(text='')
        previous_item_label.config(text='')
        next_item_label.config(text='')

# Create a button to advance to the next item with white text and dark gray background
next_button = tk.Button(window, text="Next Item", command=next_item, fg="white", bg="#222222")
next_button.grid(row=2, column=1, padx=20, pady=10, sticky="w")

# Create a button to skip to the next row with white text and dark gray background
skip_button = tk.Button(window, text="Skip to Next Row", command=next_row, fg="white", bg="#222222")
skip_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

# Create a button to display the previous item with white text and dark gray background
previous_button = tk.Button(window, text="Previous Value", command=previous_item, fg="white", bg="#222222")
previous_button.grid(row=2, column=0, padx=20, pady=10, sticky="w")

# Initialize the initial row label
row_label.config(text="Row 124")

# Run the Tkinter main loop
window.mainloop()
