import os
import pandas as pd


def australia_process_file(dir: str) -> pd.DataFrame:
    pass


def main():
    directory = ".Data/Australia"
    australia = australia_process_file(directory)
    print(australia)
    pass

if __name__ == "__main__":
    main()