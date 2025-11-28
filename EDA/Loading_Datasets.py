#This file exists to load datasets for exploratory data analysis purposes.
import pandas as pd

def load_data():
    """
    Loads the MovieLens datasets (movies, ratings, links) from a remote URL.

    Returns:
        tuple: A tuple containing three pandas DataFrames: (movies_df, ratings_df, links_df).
    """
    movies_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/movies.csv'
    ratings_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/ratings.csv'
    links_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/links.csv'

    movies_df = pd.read_csv(movies_path)
    ratings_df = pd.read_csv(ratings_path)
    links_df = pd.read_csv(links_path)
    
    return movies_df, ratings_df, links_df

if __name__ == '__main__':
    # This block will only run when the script is executed directly
    # For example, by running `python EDA/Loading_Datasets.py` in the terminal
    movies, ratings, links = load_data()
    print("Data loaded successfully!")
    print("\nMovies DataFrame head:")
    print(movies.head())
    print("\nRatings DataFrame head:")
    print(ratings.head())
    print("\nLinks DataFrame head:")
    print(links.head())
