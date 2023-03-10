import os
import pandas as pd


def congregate(dir: str) -> pd.DataFrame:
    filenames = os.listdir(dir)
    fname_pd_dict: dict[str, pd.DataFrame] = {}
    for filename in filenames:
        pathname = os.path.join(dir, filename)
        if os.path.isfile(pathname):
            if os.path.splitext(pathname)[1] == ".csv":
                fname_pd_dict[filename] = pd.read_csv(pathname)

    interest_rates = fname_pd_dict['au_quarterly_interest_rate.csv']
    merged_interest_rates = interest_rates.groupby('TIME')["Value"].mean()
    merged_interest_rates = merged_interest_rates.reset_index()

    cpi = fname_pd_dict[]
    pass


def main():
    directory = ".Data/Australia"
    australia = congregate(directory)
    print(australia)
    pass

if __name__ == "__main__":
    main()