
file_path = '/Users/dimas/Downloads/test2.xls'  # Replace with the path to your text file

# Try different encodings to read the file
encodings_to_try = ['utf-8', 'latin-1', 'utf-16']

lines = None
for encoding in encodings_to_try:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            lines = file.readlines()
        break  # Stop trying encodings if successful
    except UnicodeDecodeError:
        pass

if lines is None:
    raise ValueError("Unable to determine the correct encoding for the file.")

# Process the data
for i in range(1, len(lines)):
    values = lines[i].split()  # Assuming space or tab as the delimiter
    if len(values) >= 3:  # Make sure the third column exists
        try:
            # Convert the third column value to float and add 0.5
            values[2] = str(float(values[2]) + 0.5)
            lines[i] = ' '.join(values)

        except ValueError:
            # Handle the case where the value in the third column is not a valid float
            pass

# Write the modified data back to the text file
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("0.5 has been added to the values in the third column starting from the second row in the text file.")
