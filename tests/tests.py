from extract import read_csv, remove_duplicates, remove_blank_rows, capitalize_user_names, remove_invalid_answer_3, write_to_file

"""
● The results.csv data file can be successfully processed into an array.
● Each line of the file is read into a new array item.
● The file read method must be in a sub-module.
"""

def test_file_read_into_list():
    # arrange
    filename= "results.csv"
    expected_output = list

    # act
    output = type(read_csv(filename))
    #assert
    assert output == expected_output

def test_list_not_empty():
    # arrange
    filename= "results.csv"
    expected_output = list

    # act
    output = read_csv(filename)
    #assert
    assert len(output) > 0

def test_first_row_is_correct():
    # arrange
    filename="results.csv"
    expected_output= ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    #act
    output = read_csv(filename)

    #assert
    assert output[0] == expected_output

    # test_your_module.py

def test_remove_duplicates():
    # dataset with duplicates
    filename="results.csv"
    dataset_with_duplicates = read_csv(filename)

    # Manually remove duplicates to create the expected result
    expected_result = [dataset_with_duplicates[0]]  # Copy the header
    unique_user_ids = set()

    for row in dataset_with_duplicates[1:]:
        user_id = row[0]
        if user_id not in unique_user_ids:
            expected_result.append(row)
            unique_user_ids.add(user_id)

    # Call the remove_duplicates function
    result = remove_duplicates(dataset_with_duplicates)

    # Assert that the result matches the expected result
    assert result == expected_result

def test_remove_blank_rows():
    # Example dataset with blank rows
    filename= "results.csv"

    # Manually remove blank rows to create the expected result
    expected_result = [filename[0]]  # Copy the header
    for row in filename[1:]:
        if any(cell.strip() for cell in row):
            expected_result.append(row)

    # Call the remove_blank_rows function
    result = remove_blank_rows(filename)

    # Assert that the result matches the expected result
    assert result == expected_result

def test_capitalize_user_names():
    # Example dataset with lowercase names
    filename="results.csv"

    dataset_with_lowercase_names = read_csv(filename)

    # Manually capitalize names to create the expected result
    expected_result = [dataset_with_lowercase_names[0]]  # Copy the header

    for row in dataset_with_lowercase_names[1:]:
        capitalized_row = [row[0]]  # Copy the user_id

        # Capitalize first_name and last_name, if present
        for cell in row[1:3]:
            capitalized_row.append(cell.capitalize() if cell else '')

        # Copy the remaining columns
        capitalized_row.extend(row[3:])
        expected_result.append(capitalized_row)

    # Call the capitalise_user_names function
    result = capitalize_user_names(dataset_with_lowercase_names)

    # Assert that the result matches the expected result
    assert result == expected_result

def test_remove_invalid_answer_3():
    # Example CSV file with values outside the range in the "answer_3" column
    filename = "results.csv"

    try:
        # Call the function
        cleaned_dataset = remove_invalid_answer_3(filename)

        # Extract rows below the header for testing
        cleaned_data_for_test = cleaned_dataset[1:]

        # Create the expected result dynamically
        expected_result = [row for row in filename[1:] if row[5].isdigit() and 1 <= int(row[5]) <= 10]
        expected_result.insert(0, filename[0])

        assert cleaned_data_for_test == expected_result
    except ValueError as e:
        print(f"Error: {e}")

