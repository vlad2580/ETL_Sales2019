import pandas as pd

def save_to_csv(data, filepath):
    """
    Saving data to a CSV file.

    Arguments:
    - data (DataFrame): dataframe with data to be saved.
    - filepath (str): path to the file where the data will be saved.
    """
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    from transform import group_by_product_and_sum, remove_duplicates
    from extract import extract_data

    output_filepath = "data/transformed/aggregated_data.csv"

    result = group_by_product_and_sum(remove_duplicates(extract_data("data/raw/supermarket_sales - Sheet1.csv")))
    
    if result is not None:
        save_to_csv(result, output_filepath)
        print(f"Data successfully saved to {output_filepath}")
    else:
        print("Data transformation error. Unable to continue saving")
