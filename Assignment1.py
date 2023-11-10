import pandas as pd
import matplotlib.pyplot as plt

def read_sales_dataset(dataset_path):
    """
    Read the sales dataset from a CSV file.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.

    Returns:
    - pd.DataFrame: The DataFrame containing the sales data.
    """
    data = pd.read_csv(dataset_path)
    return data

def count_sales_by_channel(data):
    """
    Preprocess the data and count the number of sales by sales channel over time.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the sales data.

    Returns:
    - pd.DataFrame: The pivot table with sales counts by year and sales channel.
    """
    data['ShipDate'] = pd.to_datetime(data['ShipDate'])
    data['Year'] = data['ShipDate'].dt.year
    sales_by_channel = data.groupby(['Year', 'Sales Channel']).size().unstack().fillna(0)
    return sales_by_channel

def create_line_plot(sales_by_channel):
    """
    Create a line plot to visualize the sales distribution by sales channel over time.

    Parameters:
    - sales_by_channel (pd.DataFrame): The pivot table with sales counts by year and sales channel.
    """
    plt.figure(figsize=(10, 6))
    sales_by_channel.plot(kind='line', marker='o')
    plt.xlabel('Shipped Date')
    plt.ylabel('Number of Sales')
    plt.title('Sales Distribution by Sales Channel Over Time')
    plt.legend(title='Sales Channel')
    
    plt.show()

def analyze_sales_dataset(dataset_path):
    """
    Main function to perform the analysis and create a line plot of sales distribution.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.
    """
    sales_data = read_sales_dataset(dataset_path)
    sales_by_channel = count_sales_by_channel(sales_data)
    create_line_plot(sales_by_channel)

dataset_path = 'C:/Users/PREDATOR/Downloads/US_Regional_Sales_Data.csv' 
analyze_sales_dataset(dataset_path)
