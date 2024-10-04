import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load csv
movie_df = pd.read_csv("D:\\Data sets\\tmdb_5000_movies.csv", encoding='utf-8')

# Gabungkan judul dan genre
movie_df['combined'] = movie_df['title'] + ' ' + movie_df['genres']

# Membuat TF-IDF untuk judul dan genre 
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(movie_df['combined'])

def get_recommendations_by_keyword(keyword):
    # Vectorisasi kata kunci
    keyword_vector = tfidf_vectorizer.transform([keyword])

    # Hitung kemiripan antara kata kunci dengan semua film
    cosine_sim = cosine_similarity(keyword_vector, tfidf_matrix).flatten()

    # Urutkan indeks film berdasarkan skor kemiripan
    sim_scores = cosine_sim.argsort()[::-1]

    # Ambil indeks 10 film dengan skor tertinggi
    movie_indices = sim_scores[:10]

    # Ambil judul dan genre film
    movie_recommendations = movie_df[['title', 'genres']].iloc[movie_indices]

    return movie_recommendations

# Minta input dari pengguna
keyword = input("Cari film apa? : ")

# Panggil fungsi rekomendasi
recommended_movies = get_recommendations_by_keyword(keyword)

# Tampilkan rekomendasi
print("Rekomendasi film berdasarkan kata kunci '{}':".format(keyword))
print(recommended_movies)