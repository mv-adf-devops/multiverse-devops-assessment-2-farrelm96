import sys
from extract import read_csv
from extract import remove_duplicates

def main():
    filename="results.csv"
    print(remove_duplicates(read_csv(filename)))
if __name__ =="__main__":
    sys.exit(main())