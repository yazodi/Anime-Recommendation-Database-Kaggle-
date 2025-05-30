# 🎌 Anime Recommendation System with LightFM

This project builds a **collaborative filtering-based anime recommendation system** using the [Anime Recommendations Database](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).  
We use the [LightFM](https://making.lyst.com/lightfm/docs/home.html) library to recommend anime to users based on their past ratings.

---

## 📦 Dataset

- `anime.csv`: Contains metadata for each anime (name, genre, type, rating)
- `rating.csv`: User-anime interactions (user_id, anime_id, rating)

---

## 🔧 Technologies Used

- `pandas`, `numpy`, `matplotlib` – for data processing and visualization
- `lightfm` – for building the recommendation engine

---

## 🧠 Methodology

1. Loaded and cleaned the anime and rating datasets.
2. Filtered out unrated data (ratings = -1).
3. Built a **user-anime interaction matrix** using LightFM's `Dataset`.
4. Trained a **LightFM model** using the `warp` loss function.
5. Recommended top-N unseen animes for any given user.

---

## 🔎 Sample Visualization

- 📊 Top 10 Most Rated Anime  
- 🎭 Top 10 Most Common Genres

These plots help understand viewing trends and user preferences.

---

## 🚀 How to Run

1. Clone the repo
2. Install requirements:

```bash
pip install -r requirements.txt

anime-recommendation-lightfm/
├── anime.csv
├── rating.csv
├── anime_recommender_lightfm.ipynb
├── requirements.txt
└── README.md

✍️ Author
Hande Çarkcı
📫 GitHub | 💼 AI & Data Science Enthusiast




---

## 🎓 Disclaimer – Educational Purpose

This project is developed **solely for educational purposes** as part of a learning process in recommendation systems and machine learning.

All datasets used are publicly available for non-commercial use via Kaggle.  
The author does not claim ownership of the dataset or intend to use it for commercial purposes.


