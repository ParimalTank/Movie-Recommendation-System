import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=491793e7377166aa3e79127c98891c82'.format(movie_id))
    data= response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    recommended_movies = []
    recommended_movies_posters = []
    index = Movies[Movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:11]:
        movie_id=Movies.iloc[i[0]].movie_id
        recommended_movies.append(Movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

st.title("Movie Recommendation System")

Movie_dict = pickle.load(open('movie_dict.pkl','rb'))
Movies= pd.DataFrame(Movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

Selected_Movie_Name= st.selectbox('Select the Movie',Movies['title'].values)

if st.button('Recommend'):
    names, posters= recommend(Selected_Movie_Name)
    p=0
    for i in range(1, 3):
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.text(names[0+p])
            st.image(posters[0+p])
        with col2:
            st.text(names[1+p])
            st.image(posters[1+p])
        with col3:
            st.text(names[2+p])
            st.image(posters[2+p])
        with col4:
            st.text(names[3+p])
            st.image(posters[3+p])
        with col5:
            st.text(names[4+p])
            st.image(posters[4+p])
        p=p+5