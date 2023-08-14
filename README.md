ETL Project: Supermarket Sales Data Analysis
This repository contains an ETL pipeline for extracting, transforming, and loading supermarket sales data.

Table of Contents
    Overview
    Prerequisites
    Files Structure
    Usage
    Contributing
    License

Overview
    The primary goal of this project is to process raw supermarket sales data, filter and transform it, and then aggregate the results by product line, showing the total sales for each category.

Prerequisites 
    Python 3.7+
    Pandas library
    CSV files with supermarket sales datф

Files Structure
.
├── data
│   ├── raw
│   │   └── supermarket_sales - Sheet1.csv
│   └── transformed
│       └── aggregated_data.csv
├── extract.py
├── transform.py
└── load.py

Usage
    1) Extract: The extract.py script reads the raw data from the CSV file located in data/raw/.
    
    2)Transform: The transform.py script filters the data for a specific time frame, removes duplicates, and groups the results by the product line, calculating the total sales for each category.
    
    3) Load: The load.py script saves the transformed data into a new CSV file in data/transformed/.


Contributing
    If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

License
    Open source, feel free to use, modify and distribute.


