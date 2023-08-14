import pandas as pd

def remove_duplicates(data):
    """
    Удаляет дубликаты из DataFrame.

    Аргументы:
    - data (DataFrame): исходные данные.

    Возвращает:
    - DataFrame: данные без дубликатов.
    """
    initial_length = len(data)
    data_without_duplicates = data.drop_duplicates()
    final_length = len(data_without_duplicates)
    
    print(f"Удалено {initial_length - final_length} дубликатов.")
    
    return data_without_duplicates

def group_by_product_and_sum(data):
    return data.groupby('Product line')['Total'].sum().reset_index()

if __name__ == "__main__":
    from extract import extract_data

    filepath = "data/raw/supermarket_sales - Sheet1.csv"
    raw_data = extract_data(filepath)

    if raw_data is not None:
        # Преобразование колонки 'Date' к формату даты
        raw_data['Date'] = pd.to_datetime(raw_data['Date'])
        filtered_data = raw_data[(raw_data['Date'] >= '1/9/2019') & (raw_data['Date'] <= '30/11/2019') & (raw_data['Rating'] > 7.5)]

        transformed_data = remove_duplicates(filtered_data)

         # Группировка данных по категории и подсчет общей стоимости продуктов
        result = group_by_product_and_sum(transformed_data)
        print(result)
        
    else:
        print("Ошибка извлечения данных. Невозможно продолжить трансформацию.")

