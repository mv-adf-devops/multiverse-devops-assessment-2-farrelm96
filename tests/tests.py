from extract import read_csv

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