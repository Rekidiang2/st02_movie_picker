import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import random
import requests
from bs4 import BeautifulSoup

import pickle
import sqlite3
#import matplotlib as plt

# == Logo
def logo():
    # source: jason-leung from unsplash
    logo = "images/ktlogo3.png"
    logo = Image.open(logo)
    size=(100,100)
    #resize image
    logo = logo.resize(size)
    st.sidebar.image(logo)

# == Home =======================================================================================
def home():
    st.markdown("""
   **Movie Picker** This help you to a random movie to watch
    """)

    img = Image.open('./images/cover_.png')
    size=(120,30)
    img = img.resize(size)
    st.image(img, caption='Movie Picker')

    st.markdown("""
        To navigate the application, in slider bar  select **About** to have info about the project, **Movie List** To see all movies collection 
       , **Pick Random Movie** to pick a random movie.
        """)
# == Movie List =============================================================================================

def movi_list():
    df = pd.read_csv("data/movies_list.csv")
    st.dataframe(df)

# == Pick Movie ===============================================================================================
def pick_movie_on():
    """For online"""
    URL = 'http://www.imdb.com/chart/top'
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.text, 'lxml') # faster

    # print(soup.prettify())

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1] # last item 
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list =[tag['title'] for tag in inner_movietags] # access attribute 'title'
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags] # access attribute 'data-value'
    movies_list = pd.DataFrame({'titles':titles, 'years':years, 'ratings':ratings,'actors_list':actors_list, })
    movies_list.to_csv("data/movies_list.csv")

    n_movies = len(titles)

    idx = random.randrange(0, n_movies) 
    print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("==>")
    with col2:
        if st.button("Pick a Movie"):
            pass
    with col3:
         st.title("<==")

    col4, col5,  = st.columns(2)
    with col4:
        st.write("Movie Title : ", titles[idx])
        st.write("Release Year : ", years[idx][1:5])
        st.write("Ratings : ", round(ratings[idx], 2))
        st.write("Actors List : ", actors_list[idx])

    with col5:
            st.write("Movie Summary : ")
            st.success(titles[idx] + "  <--  Is the movie to watch")


def pick_movie_off():

    """for Offline"""
    df = pd.read_csv("data/movies_list.csv")
    n_movies = df.shape[0]
    idx = random.randrange(0, n_movies)

    title =  df.titles[idx]
    year = df.years[idx]
    rating = df.ratings[idx]
    actors = df.actors_list[idx]

    col1, col2, col3 = st.columns(3)
    with col1:
        st.title("==>")
    with col2:
        if st.button("Pick a Movie"):
            pass
    with col3:
         st.title("<==")

    col6, col7,  = st.columns(2)
    with col6:
        st.write("Movie Title : ", title)
        st.write("Release Year : ", year[1:5])
        st.write("Ratings : ", round(rating, 2))
        st.write("Actors List : ", actors)
    
    with col7:
            st.write("Movie Summary : ")
    st.success(title + "  <--  Is the movie to watch")

   
# == About ======================================================================
def about():
    st.markdown("""
    ---
    ### Motivation
    **Movie Picker This help you to a random movie to watch. The dataset used was obtain after scrapping from 'http://www.imdb.com/chart/top' the information about the movie can came directement from the website (online) or from the dataset locally saved after scrapping and cleaning.** 
   
   """)

    st.markdown("""
    ---
    ### Navigate the App
    **To navigate the application, in slider bar select About to have info about the project, Movie List To see all movies collection , Pick Random Movie to pick a random movie.** 
    """)

    st.markdown("""
    ---
    ### author
    I’m  Data and technology passionate person, Artificial Intelligence enthusiast, lifelong learner. 
    Since my childhood I was interested to technology and science, but I didn’t get access to it, 
    by the lack of resource and opportunities hopefully grace to massive learning resource available
     on the Internet I’m getting close to my dream. My pleasure is to motivate, guide and teach 
     people with less or without resource accomplish their dream in the world of technology 
     specially kids and young. 
     For more information about me go to my **Website** and **Social Network** platform (👇)
    """)

# == Footer ==========================================================================================
def footer():
    footerr = """
            ---
    
            <div style="background-color:white;padding:1px">
            <h4 style="color:bleu;text-align:center;">Kiese Diangebeni Reagan </h4>
            <p style="color:red;text-align:center;"> = Datalogue Date Passionate =</p>
            <p style="color:bleu;text-align:center;">www.kiese.tech, 
            E-mail : rkiese6@gmail.com</p>
            
            <p style="color:black;text-align:center;">
            <a href="https://twitter.com/ReaganKiese">Twitter</a> - 
            <a href="">Linkedin</a> - 
            <a href="https://github.com/Rekidiang2">Github</a> - 
            <a href="https://medium.com/@rkddatas">Medium</a> - 
            <a href="https://www.kaggle.com/rekidiang">Kaggle</a></p>
            </div><br>"""
    st.markdown(footerr, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)