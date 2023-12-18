from extract import read_csv, remove_duplicates

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
    # Example dataset with duplicates
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


