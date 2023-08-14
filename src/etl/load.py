import pandas as pd

def save_to_csv(data, filepath):
    """
    Сохранение данных в CSV-файл.

    Аргументы:
    - data (DataFrame): датафрейм с данными для сохранения.
    - filepath (str): путь к файлу, в который будут сохранены данные.
    """
    data.to_csv(filepath, index=False)

if __name__ == "__main__":
    from transform import group_by_product_and_sum, remove_duplicates
    from extract import extract_data

    output_filepath = "data/transformed/aggregated_data.csv"

    # Предположим, что result это переменная, которую вы экспортировали из transform.py
    # Вам нужно удостовериться, что у вас есть такая переменная в transform.py и что она содержит итоговые данные.
    result = group_by_product_and_sum(remove_duplicates(extract_data("data/raw/supermarket_sales - Sheet1.csv")))
    
    if result is not None:
        save_to_csv(result, output_filepath)
        print(f"Данные успешно сохранены в {output_filepath}")
    else:
        print("Ошибка трансформации данных. Невозможно продолжить сохранение.")
