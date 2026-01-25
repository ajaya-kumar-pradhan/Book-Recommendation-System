import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
import pickle
import os

# Set paths
DATA_DIR = r"C:\Users\ajaya\Downloads\kindle book"
BOOKS_PATH = os.path.join(DATA_DIR, 'Books.csv')
USERS_PATH = os.path.join(DATA_DIR, 'Users.csv')
RATINGS_PATH = os.path.join(DATA_DIR, 'Ratings.csv')

def prepare_data():
    print("Loading data...")
    books = pd.read_csv(BOOKS_PATH, low_memory=False)
    users = pd.read_csv(USERS_PATH, low_memory=False)
    ratings = pd.read_csv(RATINGS_PATH, low_memory=False)

    # 1. Data Cleaning (Handling the manual fixes from the notebook)
    # Fix three specific columns that are shifted in the original dataset
    # ISBN 0789466953
    books.loc[books['ISBN'] == '0789466953', 'Book-Title'] = 'DK Readers: Creating the X-Men, How Comic Books Come to Life (Level 4: Proficient Readers)'
    books.loc[books['ISBN'] == '0789466953', 'Book-Author'] = 'James Buckley'
    books.loc[books['ISBN'] == '0789466953', 'Year-Of-Publication'] = '2000'
    books.loc[books['ISBN'] == '0789466953', 'Publisher'] = 'DK Publishing Inc'

    # ISBN 078946697X
    books.loc[books['ISBN'] == '078946697X', 'Book-Title'] = 'DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient Readers)'
    books.loc[books['ISBN'] == '078946697X', 'Book-Author'] = 'Michael Teitelbaum'
    books.loc[books['ISBN'] == '078946697X', 'Year-Of-Publication'] = '2000'
    books.loc[books['ISBN'] == '078946697X', 'Publisher'] = 'DK Publishing Inc'

    # ISBN 2070426769
    books.loc[books['ISBN'] == '2070426769', 'Book-Title'] = "Peuple du ciel, suivi de 'Les Bergers"
    books.loc[books['ISBN'] == '2070426769', 'Book-Author'] = 'Jean-Marie Gustave Le ClÃ?Â©zio'
    books.loc[books['ISBN'] == '2070426769', 'Year-Of-Publication'] = '2003'
    books.loc[books['ISBN'] == '2070426769', 'Publisher'] = 'Gallimard'

    # Convert Year-Of-Publication to numeric
    books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'], errors='coerce')

    # Merge ratings and books
    print("Merging data...")
    ratings_with_name = ratings.merge(books, on='ISBN')

    # 2. Collaborative Filtering (Filtering for performance)
    print("Filtering data...")
    # Users who have rated more than 200 books
    x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
    knowledge_users = x[x].index
    filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(knowledge_users)]

    # Books with at least 50 ratings
    y = filtered_rating.groupby('Book-Title').count()['Book-Rating'] >= 50
    famous_books = y[y].index
    final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]

    # 3. Create Pivot Table
    print("Creating pivot table...")
    pt = final_ratings.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
    pt.fillna(0, inplace=True)

    # 4. Train Model
    print("Training model...")
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(pt)

    # 5. Top 50 Popular Books (For Home Page)
    print("Calculating popular books...")
    num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
    num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

    avg_rating_df = ratings_with_name.groupby('Book-Title').mean(numeric_only=True)['Book-Rating'].reset_index()
    avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)

    popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')
    # Use common threshold: books with > 250 ratings
    popular_df = popular_df[popular_df['num_ratings'] >= 250].sort_values('avg_rating', ascending=False).head(50)
    popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']]

    # 6. Save objects
    print("Saving objects...")
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('pt.pkl', 'wb') as f:
        pickle.dump(pt, f)
    with open('books.pkl', 'wb') as f:
        books_to_save = books.drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-M']]
        pickle.dump(books_to_save, f)
    with open('popular.pkl', 'wb') as f:
        pickle.dump(popular_df, f)

    print("Success! Data prepared.")

if __name__ == "__main__":
    prepare_data()
