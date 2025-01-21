import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5497e36994286c2134c658fdf155804b&language=en-US'.format(movie_id))
    response=response.json()
    return "https://image.tmdb.org/t/p/w500/"+response['poster_path']
    




st.title('Movie Recommendation System')

movies_list=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

user_selected_option = st.selectbox("Find movies from the dropdown below", movies['title'].values)

similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(user_provided_title):
    recommended_movie_posters=[]
    movie_index=movies[movies['title']==user_provided_title].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
       
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))  
    return recommended_movies,recommended_movie_posters 


 
center_button = st.button("Submit", type="primary")
if center_button:
        names,posters=recommend(user_selected_option)
       
      
        col1, col2, col3 , col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])
        with col3 :
            st.text(names[4])
            st.image(posters[4])


   

   