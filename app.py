import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

st.set_page_config(page_title="Amazon Kindle Book Recommendation", layout="wide")
# Load data with caching for performance
@st.cache_resource
def load_data():
    try:
        popular_df = pickle.load(open('popular.pkl', 'rb'))
        pt = pickle.load(open('pt.pkl', 'rb'))
        books = pickle.load(open('books.pkl', 'rb'))
        model = pickle.load(open('model.pkl', 'rb'))
        return popular_df, pt, books, model
    except FileNotFoundError:
        st.error("Model files not found. Please run data_prep.py first.")
        return None, None, None, None

popular_df, pt, books, model = load_data()

# App UI
st.title("📚 Amazon Kindle Book Recommendation")

st.sidebar.image("logo.png", width="stretch")
menu = st.sidebar.selectbox("Navigate", ["Home (Popular Books)", "Get Recommendations"])

if menu == "Home (Popular Books)" and popular_df is not None:
    st.header("Top 50 Most Popular Books")
    
    # Display books in a grid
    cols_per_row = 4
    for i in range(0, len(popular_df), cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(popular_df):
                book = popular_df.iloc[i + j]
                with cols[j]:
                    st.image(book['Image-URL-M'], width=150)
                    st.subheader(book['Book-Title'])
                    st.write(f"Author: {book['Book-Author']}")
                    st.write(f"Avg Rating: {book['avg_rating']:.2f}")

elif menu == "Get Recommendations" and pt is not None:
    st.header("Find Your Next Favorite Read")
    
    book_list = pt.index.values
    selected_book = st.selectbox("Type or select a book you liked:", book_list)

    if st.button("Recommend"):
        # Fetch index
        index = np.where(pt.index == selected_book)[0][0]
        
        # Get similar neighbors
        distances, neighbor_indices = model.kneighbors(pt.iloc[index, :].values.reshape(1, -1), n_neighbors=6)
        
        # Display recommendations
        st.subheader(f"Books similar to '{selected_book}':")
        cols = st.columns(5)
        
        for i in range(1, len(neighbor_indices[0])): # skip the first one (itself)
            rec_book_title = pt.index[neighbor_indices[0][i]]
            # Find book details
            book_info = books[books['Book-Title'] == rec_book_title].iloc[0]
            
            with cols[i-1]:
                st.image(book_info['Image-URL-M'], width=150)
                st.write(f"**{rec_book_title}**")
                st.write(f"_{book_info['Book-Author']}_")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed for Kindle Book Dataset Analysis.")
