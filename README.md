🎬 Movie Recommender System

A Machine Learning–based Movie Recommender System built using Python and Flask, deployed live on Render.
The application recommends similar movies based on a user’s input using a content-based filtering approach and enhances results with movie posters via the TMDB API.

🚀 Live Demo

🔗 Live Application:
https://movie-recommender-system-1-1lih.onrender.com

📂 GitHub Repository:
https://github.com/RAJEEV-01-MAX/movie-recommender-system-/tree/master

🧠 How It Works

The user enters a movie name.

A pre-trained similarity matrix (ML model) finds the most similar movies.

The backend processes the request using Flask.

Movie posters are fetched dynamically using the TMDB API.

Recommended movies are displayed on the web interface.

This is a content-based recommender system, not a random or rule-based system.

🛠️ Tech Stack

Programming Language: Python

Backend Framework: Flask

Machine Learning: Content-based filtering

Libraries: Pandas, NumPy

API Integration: TMDB API

Deployment: Render

Version Control: Git & Git LFS (for large ML files)

📁 Project Structure
movie-recommender-system/
│
├── app.py                  # Flask backend
├── movies.pkl              # Movie dataset
├── similarity.pkl          # ML similarity matrix (Git LFS)
├── requirements.txt        # Dependencies
├── templates/
│   └── index.html          # Frontend UI
└── README.md

⚙️ Installation & Setup (Local)
1️⃣ Clone the repository
git clone https://github.com/RAJEEV-01-MAX/movie-recommender-system-.git
cd movie-recommender-system-

2️⃣ Create a virtual environment
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set TMDB API Key
setx TMDB_API_KEY "your_api_key_here"   # Windows

5️⃣ Run the app
python app.py


Open browser at:
http://127.0.0.1:5000

☁️ Deployment Notes

Deployed using Render

Large ML file (similarity.pkl) managed using Git Large File Storage (LFS)

Environment variables used for secure API key handling

🎯 Key Learnings

End-to-end ML project deployment

Handling large ML models in production

Flask backend development

Third-party API integration

Cloud deployment troubleshooting

📌 Future Improvements

Add user-based collaborative filtering

Improve UI with movie cards and animations

Add search suggestions

Add user ratings and feedback system

👤 Author

Rajeev Aswal
🔗 GitHub: https://github.com/RAJEEV-01-MAX

🔗 LinkedIn: (add your LinkedIn profile link)

⭐ Acknowledgements

TMDB for movie data and posters

Flask & Python open-source community

