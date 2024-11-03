# Movie Content-Based Recommendation System

![alt text](https://github.com/AhmedEssam29/Recommendation_System_KNN/blob/main/download.png?raw=true)


This project demonstrates how to build a content-based movie recommendation system using the TMDB movie dataset. The system recommends movies based on the similarities in features like genres, keywords, cast, and crew, helping users discover films similar to ones they enjoy.
## Project Overview

In this project, we create a recommendation engine using metadata from the TMDB dataset to match users with movies based on content rather than collaborative filtering. By analyzing features such as genres, cast, keywords, and crew members, the model provides recommendations for movies that share similar characteristics.
```bash
pip install foobar
```

## Table of Contents
1. [Datasets](#Datasets)
2. [Installation](#Installation)
3. [Project Structure](#Project#Structure)
4. [Usage](#Usage)
5. [Features](#Features)
6. [Contributions](#Contributions)

## Datasets
The project uses two main datasets from [Kaggle’s TMDB Movie Metadata](#Kaggle’s#TMDB#Movie#Metadata):

1. **tmdb_5000_credits.csv** – Contains data on movie credits, including cast and crew information.
2. **tmdb_5000_movies.csv** – Contains detailed metadata about movies, such as genres, keywords, popularity, release date, and more.

These datasets are preprocessed and merged to create a unified data source for the recommendation system.

## Installation
To set up the project locally, please follow these steps:
1. Clone this repository:

```bash
git clone https://github.com/AhmedEssam29/Recommendation_System_KNN.git
```
2. Navigate to the project directory:
```bash
cd movie-recommender
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```bash
movie-recommender/
├── data/                       # Contains the datasets
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── notebooks/                  # Jupyter notebooks for analysis and development
├── src/                        # Source code for data processing and modeling
│   ├── preprocess.py           # Data preprocessing scripts
│   ├── recommender.py          # Recommendation system implementation
│   └── utils.py                # Utility functions
├── README.md                   # Project documentation
├── requirements.txt            # Project dependencies
└── main.py                     # Main file to run the recommender system
```

## Usage

1. Data Loading: Load the credits and movies datasets.
2. Data Preprocessing:
- Rename columns and merge credits and movies datasets on the movie_id column.
- Drop unnecessary columns (e.g., homepage, status, etc.) for cleaner data.
3. Feature Extraction: Extract relevant features such as genres, keywords, cast, and crew.
4. Modeling and Recommendations:
- Implement a similarity-based content recommendation algorithm to recommend movies based on selected movie attributes.
- Run the system with main.py to see recommendations.

## Running the App:
Run the app using

```bash
streamlit run app.py
```


![alt text](https://github.com/AhmedEssam29/Recommendation_System_KNN/blob/main/app.png?raw=true)


