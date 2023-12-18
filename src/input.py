import sys
from extract import read_csv

def main():
    filename="results.csv"
    print(read_csv(filename))

if __name__ =="__main__":
    sys.exit(main())