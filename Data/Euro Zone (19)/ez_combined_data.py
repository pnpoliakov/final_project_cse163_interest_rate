import os
import pandas as pd


def euro_zone_process_file(dir: str) -> pd.DataFrame:
    pass


def main():
    directory = ".Data/Euro Zone"
    euro_zone = euro_zone_process_file(directory)
    print(euro_zone)
    pass

if __name__ == "__main__":
    main()