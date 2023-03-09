import os
import pandas as pd


def canada_process_file(dir: str) -> pd.DataFrame:
    filenames = os.listdir(dir)
    
    for filename in filenames:
        pathname = os.path.join(dir, filename)

    return canada


def main():
    directory = "/FINAL_PROJECT_CSE163_INTERST_RATE/Data/"
    canada = canada_process_file(directory + "Canada")

if __name__ == "__main__":
    main() 