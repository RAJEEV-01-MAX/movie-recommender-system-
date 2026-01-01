from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load movies.pkl
with open('movies.pkl', 'rb') as f:
    movies = pickle.load(f)

# Get movie titles safely
if hasattr(movies, 'columns'):
    movie_titles = movies['title'].tolist()
else:
    movie_titles = list(movies)

def recommend(movie_name):
    movie_name = movie_name.lower()
    matches = [m for m in movie_titles if movie_name in m.lower()]

    if not matches:
        return ["Movie not found"]

    return matches[:5]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    movie_name = request.form['movie']
    recommendations = recommend(movie_name)

    return render_template(
        'index.html',
        movie_name=movie_name,
        recommendations=recommendations
    )

if __name__ == "__main__":
    app.run(debug=True)
