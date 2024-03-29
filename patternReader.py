# Function to read the input from a file
def read_input_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def patternReader(inputString):

    # Remove spaces
    inputString = inputString.replace(" ", "")

    # Remove newlines
    inputString = inputString.replace("\n", "")

    #add commas after new rows
    inputString = inputString.replace("(L)", "(L),")
    inputString = inputString.replace("(R)", "(R),")

    # Split the input string into rows using 'Row' as the delimiter
    rows = inputString.strip().split('Row')[1:]
    
    # Create an empty list to store the matrix
    matrix = []

    for i, row in enumerate(rows):
        elements = row.split(',')
        if i % 2 == 1:
            matrix.append(elements)
        else:
            matrix.append(elements[::-1])

    # Create a new matrix to store the filtered elements
    filtered_matrix = []

    # Iterate through the original matrix
    for row in matrix:
        # Create a new row to store the filtered elements for this row
        filtered_row = []
        
        # Iterate through the elements in the current row
        for element in row:
            # Check if the element contains '(L)'
            if '(L)' not in element and '(R)' not in element:
                # If it doesn't contain '(L)' or '(R)', add it to the filtered row
                filtered_row.append(element)
        
        # Add the filtered row to the filtered matrix
        filtered_matrix.append(filtered_row)
    
    #return the desired matrix
    return filtered_matrix


def trackerReader():
    tracker = read_input_from_file('tracker.txt')
    tracker = tracker.split(", ")
    current_row = tracker[0]
    max_row = tracker[1]
    return current_row, max_row

def trackerUpdate(text):
    #open file in overwrite mode
    tracker = open('C:/Users/Jgrac/beads/tracker.txt', 'w')
    tracker.write(text)
    tracker.close()