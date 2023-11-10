import pandas as pd
import matplotlib.pyplot as plt

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
