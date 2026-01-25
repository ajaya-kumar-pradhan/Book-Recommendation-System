import streamlit as st
import pickle
import numpy as np
import os

# Set page config
st.set_page_config(page_title="Book Recommender", layout="wide")

# Flat structure paths (all files in root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')
PIVOT_PATH = os.path.join(BASE_DIR, 'book_pivot.pkl')
BOOKS_PATH = os.path.join(BASE_DIR, 'books.pkl')

# Custom CSS for Modern LOOK
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&family=Open+Sans:wght@400;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Open Sans', sans-serif;
    }

    .book-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        text-align: center;
        margin-bottom: 1rem;
    }

    .book-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        border: 1px solid #ff9900;
    }

    .book-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #333;
        margin-top: 8px;
        line-height: 1.2;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_data():
    try:
        if not all([os.path.exists(MODEL_PATH), os.path.exists(PIVOT_PATH), os.path.exists(BOOKS_PATH)]):
             return None, None, None
             
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(PIVOT_PATH, 'rb') as f:
            book_pivot = pickle.load(f)
        with open(BOOKS_PATH, 'rb') as f:
            books_metadata = pickle.load(f)
        return model, book_pivot, books_metadata
    except Exception as e:
        return None, None, None

model, book_pivot, books_metadata = load_data()

# Header Area
col_logo, col_title = st.columns([1, 6])
with col_logo:
    logo_path = os.path.join(BASE_DIR, 'logo.png')
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)
with col_title:
    st.title("Kindle Recommendation System")

tab1, tab2 = st.tabs(["🎯 Recommendations", "📊 Data Insights"])

with tab1:
    if model is None or book_pivot is None:
        st.error("Error: Model files not found in the root directory. Please check GitHub.")
    else:
        selected_book = st.selectbox("Select a book you enjoyed:", book_pivot.index.values)

        if st.button('🚀 Get Recommendations'):
            with st.spinner('Thinking...'):
                query_index = np.where(book_pivot.index == selected_book)[0][0]
                distances, indices = model.kneighbors(book_pivot.iloc[query_index,:].values.reshape(1, -1), n_neighbors=6)
                
                cols = st.columns(5)
                for i in range(1, 6):
                    idx = indices.flatten()[i]
                    title = book_pivot.index[idx]
                    meta = books_metadata[books_metadata['title'] == title]
                    poster = meta.iloc[0]['image_url'] if not meta.empty else "https://via.placeholder.com/150"
                    
                    with cols[i-1]:
                        st.markdown(f'<div class="book-card"><img src="{poster}" style="width:100%; border-radius:8px;"><div class="book-title">{title}</div></div>', unsafe_allow_html=True)

with tab2:
    st.header("Kindle Book Insights")
    if books_metadata is not None:
        colA, colB = st.columns(2)
        with colA:
            st.subheader("Top Authors")
            st.bar_chart(books_metadata['author'].value_counts().head(10))
        with colB:
            st.subheader("Top Publishers")
            st.bar_chart(books_metadata['publisher'].value_counts().head(10))
