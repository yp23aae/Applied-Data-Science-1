import pandas as pd
import matplotlib.pyplot as plt

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
