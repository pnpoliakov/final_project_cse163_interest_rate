import os
import pandas as pd


def turkey_process_file(dir: str) -> pd.DataFrame:
    pass


def main():
    directory = ".Data/Turkey"
    turkey = turkey_process_file(directory)
    print(turkey)
    pass

if __name__ == "__main__":
    main()