# Deployment Instructions

Follow these steps to deploy your Book Recommendation System online using Streamlit Cloud.

## 1. Prepare your GitHub Repository
- Create a new repository on [GitHub](https://github.com).
- Upload the following files to the repository:
    - `app.py`
    - `requirements.txt`
    - `popular.pkl`
    - `pt.pkl`
    - `books.pkl`
    - `model.pkl`

> [!TIP]
> Since `.pkl` files can be large, you might need to use [Git LFS](https://git-lfs.github.com/) OR if they are small enough (< 25MB), regular upload works. If they are very large, you might need to store them on a cloud drive and download them in `app.py`.

## 2. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Connect your GitHub account.
3. Click "New app".
4. Select your repository, branch, and `app.py` as the main file.
5. Click "Deploy".

## 3. Local Testing
To test the app locally before uploading:
```bash
pip install -r requirements.txt
streamlit run app.py
```
