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



def read_movie_dataset(dataset_path):
    """
    Read the movie dataset from a CSV file.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.

    Returns:
    - pd.DataFrame: The DataFrame containing the movie data.
    """
    data = pd.read_csv(dataset_path)
    return data

def create_pie_chart(data):
    """
    Create a pie chart to visualize the distribution of movies by release year.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing movie data.
    """
    release_year_counts = data['RELEASE_YEAR'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(release_year_counts, labels=release_year_counts.index, startangle=140, autopct='%1.1f%%')
    plt.title('Distribution of Movies by Release Year (1954-1975)')
    
    plt.show()

def analyze_movie_dataset(dataset_path, start_year, end_year):
    """
    Analyze the movie dataset and create a pie chart of movie distribution by release year
    within the specified range.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.
    - start_year (int): The start year for filtering movies.
    - end_year (int): The end year for filtering movies.
    """
    movie_data = read_movie_dataset(dataset_path)

    # Filter the dataset to include only movies released between start_year and end_year
    filtered_data = movie_data[(movie_data['RELEASE_YEAR'] >= start_year) & (movie_data['RELEASE_YEAR'] <= end_year)]

    create_pie_chart(filtered_data)

dataset_path = "C:/Users/PREDATOR/Downloads/Best Movie by Year Netflix.csv"
analyze_movie_dataset(dataset_path, 1954, 1975)



def get_tv_shows(csv_path):
    """
    Get TV show data from a CSV file.

    Parameters:
    - csv_path (str): The file path to the CSV dataset.

    Returns:
    - pd.DataFrame: The DataFrame containing TV show data.
    """
    data = pd.read_csv(csv_path)
    return data

def calculate_average_scores_by_genre(data):
    """
    Preprocess the data and calculate the average scores of TV shows by genre.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing TV show data.

    Returns:
    - pd.Series: A Series containing the average scores sorted by genre.
    """
    tv_shows = data[data['NUMBER_OF_SEASONS'] > 0]  # Filter for TV shows
    average_scores = tv_shows.groupby('MAIN_GENRE')['SCORE'].mean().sort_values(ascending=False)
    return average_scores

def create_bar_graph(data, title, xlabel, ylabel):
    """
    Create a bar graph to visualize the average scores of TV shows by genre.

    Parameters:
    - data (pd.Series): A Series containing the data to be plotted.
    - title (str): The title of the bar graph.
    - xlabel (str): The label for the x-axis.
    - ylabel (str): The label for the y-axis.
    """
    plt.figure(figsize=(12, 6))
    data.plot(kind='bar')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    plt.show()

def analyze_tv_shows_dataset(dataset_path):
    """
    Main function to analyze and visualize the TV shows dataset.

    Parameters:
    - dataset_path (str): The file path to the CSV dataset.
    """
    tv_shows_data = get_tv_shows(dataset_path)
    avg_scores_by_genre = calculate_average_scores_by_genre(tv_shows_data)
    
    create_bar_graph(avg_scores_by_genre, 
                     title='Average Scores of TV Shows by Genre',
                     xlabel='Genre',
                     ylabel='Average Score')

csv_path = "C:/Users/PREDATOR/Downloads/Best Show by Year Netflix.csv"
analyze_tv_shows_dataset(csv_path)

