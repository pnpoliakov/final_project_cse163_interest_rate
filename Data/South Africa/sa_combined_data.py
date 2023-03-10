import os
import pandas as pd


def south_africa_process_file(dir: str) -> pd.DataFrame:
    pass


def main():
    directory = ".Data/South Africa"
    south_africa = south_africa_process_file(directory)
    print(south_africa)
    pass

if __name__ == "__main__":
    main()