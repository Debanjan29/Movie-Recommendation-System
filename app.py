import streamlit as st
import pandas as pd
import pickle
import requests

y=['Batman','Joker']
y=pd.read_csv('new.csv')
y=y['title']
new=pd.read_csv('new.csv')
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index=new[new['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:12]
    
    k=[]
    k_poster=[]
    for i in movies_list:
        if i not in k:
            movie_id = new.iloc[i[0]].movie_id
            # Fetch Poster 
            k_poster.append(fetch_poster(movie_id))
            k.append(new['title'][i[0]])
    
    return k,k_poster

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title("Movie Recommender System")


option=st.selectbox('Hi World',y)

if st.button("Recommend",type="primary"):
    k,k_poster=recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5,gap="medium")
    with col1:
        st.text(k[0])
        st.image(k_poster[0])
    with col2:
        st.text(k[1])
        st.image(k_poster[1])

    with col3:
        st.text(k[2])
        st.image(k_poster[2])
    with col4:
        st.text(k[3])
        st.image(k_poster[3])
    with col5:
        st.text(k[4])
        st.image(k_poster[4])

    col6, col7, col8, col9, col10 = st.columns(5,gap="medium")

    with col6:
        st.text(k[5])
        st.image(k_poster[5])
    
    with col7:
        st.text(k[6])
        st.image(k_poster[6])
    
    with col8:
        st.text(k[7])
        st.image(k_poster[7])

    with col9:
        st.text(k[8])
        st.image(k_poster[8])

    with col10:
        st.text(k[9])
        st.image(k_poster[9])