def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            rows.append(line.strip().split(','))
    return rows

def remove_duplicates(filename):
    # Create a set to store unique user_ids
    unique_user_ids = set()
    # Create a new dataset to store the unique rows
    unique_dataset = [filename[0]]  # Copy the header
    # Iterate through the rows of the dataset
    for row in filename[1:]:
        user_id = row[0]
        # Check if the user_id is not in the set of unique user_ids
        if user_id not in unique_user_ids:
            # Add the row to the unique dataset
            unique_dataset.append(row)
            # Add the user_id to the set of unique user_ids
            unique_user_ids.add(user_id)    
    return unique_dataset

def remove_blank_rows(filename):
    return [row for row in filename if any(cell.strip() for cell in row)]

def capitalize_user_names(filename):
    header = filename[0]
    first_name_index = header.index('first_name')
    last_name_index = header.index('last_name')

    for row in filename[1:]:
        if row[first_name_index]:
            row[first_name_index] = row[first_name_index].capitalize()
        if row[last_name_index]:
            row[last_name_index] = row[last_name_index].capitalize()
    return filename

def remove_invalid_answer_3(filename):
    header = filename[0]
    answer_3_index = header.index('answer_3')

    # Filter rows where answer_3 is within the range [1, 10]
    filtered_dataset = [row for row in filename if row[answer_3_index].isdigit() and 1 <= int(row[answer_3_index]) <= 10]
    cleaned_dataset = [header]+ filtered_dataset
    return cleaned_dataset

def write_to_file(dataset, output_file):
    with open(output_file, 'w') as file:
        # Write the header
        file.write(','.join(dataset[0]) + '\n')
        # Write the data rows
        for row in dataset[1:]:
            file.write(','.join(row) + '\n')

def print_formatted_row(row):
        formatted_row = '\t'.join(str(cell).ljust(15) for cell in row)