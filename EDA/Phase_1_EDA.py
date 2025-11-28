# This script performs the first phase of exploratory data analysis (EDA).
# It loads the datasets and displays basic information about them.

from Loading_Datasets import load_data
import pandas as pd

def perform_eda():
    """
    Loads the data and performs basic exploratory data analysis.
    """
    try:
        movies_df, ratings_df, links_df = load_data()
        print("Data loaded successfully!")

        print("\n" + "="*30)
        print("Initial EDA - First Look at the Data")
        print("="*30 + "\n")

        # Display the first 5 rows of each dataframe
        print("--- Movies DataFrame (movies_df) ---")
        print(movies_df.head())
        print("\nShape:", movies_df.shape)
        print("\nInfo:")
        movies_df.info()
        print("\n" + "="*30 + "\n")

        print("--- Ratings DataFrame (ratings_df) ---")
        print(ratings_df.head())
        print("\nShape:", ratings_df.shape)
        print("\nInfo:")
        ratings_df.info()
        print("\n" + "="*30 + "\n")

        print("--- Links DataFrame (links_df) ---")
        print(links_df.head())
        print("\nShape:", links_df.shape)
        print("\nInfo:")
        links_df.info()
        print("\n" + "="*30 + "\n")

        print("EDA Phase 1 script finished.")

    except ImportError:
        print("Error: Could not import 'load_data' from 'Loading_Datasets'.")
        print("Please ensure 'Loading_Datasets.py' is in the same directory (EDA).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    # To run this script, navigate to the root directory of the project in your terminal
    # and execute the command: python -m EDA.Phase_1_EDA
    # This ensures that Python can correctly resolve the module imports.
    perform_eda()
