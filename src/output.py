import sys
from extract import read_csv, print_formatted_row
def main():
    filename = "clean_results.csv"
    data =read_csv(filename)
    def print_formatted_row(row):
        formatted_row = '\t'.join(str(cell).ljust(15) for cell in row)
        print(formatted_row)

# Print header separately
    print_formatted_row(data[0])

# Print data rows
    for row in data[1:]:
        print_formatted_row(row)
if __name__ =="__main__":
    sys.exit(main())