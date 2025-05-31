import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Modeli yükle
with open("anime_recommender_lightfm.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
dataset = data["dataset"]
interactions = data["interactions"]
user_id_map = data["user_id_map"]
item_id_map = data["item_id_map"]
anime_df = data["anime"]

# Ters eşlemeler
reverse_user_map = {v: k for k, v in user_id_map.items()}
reverse_item_map = {v: k for k, v in item_id_map.items()}

# Başlık
st.title("🎌 Anime Tavsiye Sistemi (LightFM)")

# Kullanıcı seçimi
user_ids = list(user_id_map.keys())
user_id_input = st.selectbox("👤 Bir kullanıcı ID seçin:", user_ids)

# Kullanıcı indeksini al
user_index = user_id_map[user_id_input]

# Tüm anime indekslerini al
n_items = interactions.shape[1]
known_positives = interactions.tocsr()[user_index].indices

# Öneri skorlarını hesapla
scores = model.predict(user_ids=user_index, item_ids=np.arange(n_items))
top_items = np.argsort(-scores)

# Kullanıcının zaten izlediklerini göster
st.subheader("✅ İzledikleriniz:")
for idx in known_positives[:5]:
    anime_id = reverse_item_map[idx]
    title = anime_df[anime_df["anime_id"] == anime_id]["name"].values[0]
    st.write("✔️", title)

# Önerilen anime'ler
st.subheader("🤖 Size Önerilenler:")
count = 0
for idx in top_items:
    if idx not in known_positives:
        anime_id = reverse_item_map[idx]
        title = anime_df[anime_df["anime_id"] == anime_id]["name"].values[0]
        st.write("⭐", title)
        count += 1
        if count >= 10:
            break
