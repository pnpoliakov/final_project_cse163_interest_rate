import os
import pandas as pd


def canada_process_file(dir: str) -> pd.DataFrame:
    filenames = os.listdir(dir)
    fname_pd_dict: dict[str, pd.DataFrame] = {}
    for filename in filenames:
        pathname = os.path.join(dir, filename)
        if os.path.isfile(pathname):
            if os.path.splitext(pathname)[1] == ".csv":
                fname_pd_dict[filename] = pd.read_csv(pathname)
    
    sorted_stock_index = fname_pd_dict["ca_monthly_stock_index.csv"][["Date", "High_Index", "Low_Index"]]
    sorted_stock_index = sorted_stock_index.groupby("Date")["High_Index", "Low_Index"].sum()
    
    # sorted_cpi = fname_pd_dict["ca_quarterly_cpi.csv"]

    # sorted_gdp = fname_pd_dict["ca_quarterly_gdp.csv"][["Date", "GDP per capita"]][:56]

    # sorted_interest_rate = fname_pd_dict["ca_quarterly_interest_rate.csv"]

    # sorted_unemployment_rate = fname_pd_dict["ca_quarterly_unemployment_rate.csv"][["Date", "Unemployment Rate"]][:56]


    # merged_zero = sorted_gdp.merge(sorted_interest_rate, left_on="Date", right_on="Date")
    # merged_one = sorted_cpi.merge(sorted_unemployment_rate, left_on="Date", right_on="Date")
    # merged = merged_zero.merge(merged_one, left_on="Date", right_on="Date")
    # # finalized = sorted_stock_index.append(merged)

    return sorted_stock_index


def main():
    directory = "./Data/Canada/"
    canada = canada_process_file(directory)
    print(canada)

if __name__ == "__main__":
    main() 