import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load data
@st.cache_data
def load_data():
    movies = pd.read_csv("D:/projects/Recommendation_System_KNN/KNN Movie Recommendation/movies.csv")
    ratings = pd.read_csv("D:/projects/Recommendation_System_KNN/KNN Movie Recommendation/ratings.csv")
    return movies, ratings

# Create a user-item matrix
@st.cache_data
def create_user_item_matrix(movies, ratings):
    merged_df = pd.merge(ratings, movies, on='movieId')
    user_movie_matrix = merged_df.pivot_table(index='userId', columns='title', values='rating').fillna(0)
    return user_movie_matrix

# Generate recommendations based on user similarity
def get_recommendations(movie_title, user_movie_matrix, n_recommendations=5):
    cosine_sim = cosine_similarity(user_movie_matrix.T)  # Transpose to get movie similarity
    movie_index = user_movie_matrix.columns.get_loc(movie_title)
    sim_scores = list(enumerate(cosine_sim[movie_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n_recommendations + 1]
    movie_indices = [i[0] for i in sim_scores]
    return user_movie_matrix.columns[movie_indices]

# Streamlit app layout
st.title("Collaborative Movie Recommendation System")
st.write("Select a movie title to get recommendations based on ratings:")

# Load data and create matrix
movies, ratings = load_data()
user_movie_matrix = create_user_item_matrix(movies, ratings)

# Movie selection
movie_title = st.selectbox("Choose a movie", user_movie_matrix.columns)

if st.button("Recommend"):
    recommendations = get_recommendations(movie_title, user_movie_matrix)
    st.write("Movies you might like:")
    for rec in recommendations:
        st.write(rec)
