import csv

def increment_column(csv_file_path, column_number, increment_value, encoding='utf-8', delimiter='\t'):
    # Read the CSV file with the specified delimiter and store data in a list
    with open(csv_file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        data = list(reader)

    # Update the values in the specified column
    for row in data:
        try:
            # Increment the specified column value by the user-input increment_value
            current_value = float(row[column_number - 1])
            row[column_number - 1] = str(current_value + increment_value)
        except (IndexError, ValueError):
            # Handle cases where there is no specified column or the value is not a float
            # If an exception occurs, proceed with writing the entire row back to the CSV file
            print(f"Warning: Skipping row {row} as the value in column {column_number} is not a valid float.")

    # Write the updated data back to the CSV file with the specified delimiter
    with open(csv_file_path, 'w', newline='', encoding=encoding) as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

# Example usage with user input
csv_file_path = input("Enter the path to your CSV file: ")
column_number = int(input("Enter the column number to increment (1-indexed): "))
increment_value = float(input("Enter the value to increment by: "))

# Optional: Specify the encoding (default is 'utf-8')
encoding = input("Enter the encoding of the CSV file (press Enter for default 'utf-8'): ") or 'utf-8'

increment_column(csv_file_path, column_number, increment_value, encoding)
