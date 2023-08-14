import pandas as pd

def extract_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data has been extracted")
        return data
    except Exception as e:
        print(f"Got mistake while extracting data")

if __name__ == "__main__":
    filepath = "data/raw/supermarket_sales - Sheet1.csv"  # замените на ваш путь к файлу
    extracted_data = extract_data(filepath)
    print(extracted_data.head())  # Выводим первые 5 строк для проверки
