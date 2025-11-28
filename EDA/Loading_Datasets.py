#This file exists to load datasets for exploratory data analysis (EDA) purposes.
import pandas as pd
movies_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/movies.csv'
ratings_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/ratings.csv'
links_path = 'https://raw.githubusercontent.com/CreatorRa/Moive-and-TV-Reccomendation-System/refs/heads/main/ml-latest-small/links.csv'

movies_df = pd.read_csv(movies_path)
ratings_df = pd.read_csv(ratings_path)
links_df = pd.read_csv(links_path)
