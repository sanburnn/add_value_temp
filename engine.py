import csv

def increment_csv_column(csv_file, column_number, increment_value):
    try:
        with open(csv_file, 'r', encoding='utf-16') as file:
            reader = csv.reader(file, delimiter='\t')
            rows = list(reader)

        with open(csv_file, 'w', newline='', encoding='utf-16') as file:
            writer = csv.writer(file, delimiter='\t')

            for row in rows:
                try:
                    # Attempt to convert the 3rd column value to a float
                    current_value = float(row[column_number - 1])
                    # Increment the value by the user-specified increment_value
                    row[column_number - 1] = str(current_value + increment_value)
                except ValueError:
                    # If the conversion to float fails, handle the exception
                    print(f"Warning: Ignoring non-float value in row {row}")
                    writer.writerow(row)
                    continue

                # Write the updated row to the CSV file
                writer.writerow(row)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    csv_file = input("Enter the CSV file path: ")
    column_number = int(input("Enter the column number to increment (1-indexed): "))
    increment_value = float(input("Enter the value to increment by: "))

    increment_csv_column(csv_file, column_number, increment_value)

    print("CSV file has been updated.")
