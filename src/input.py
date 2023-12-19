import sys
from extract import read_csv
from extract import remove_duplicates
from extract import remove_blank_rows
from extract import capitalize_user_names
from extract import remove_invalid_answer_3
def main():
    filename="results.csv"
    cleaned_data = remove_invalid_answer_3(capitalize_user_names(remove_blank_rows(remove_duplicates(read_csv(filename)))))
    print(cleaned_data)
if __name__ =="__main__":
    sys.exit(main())