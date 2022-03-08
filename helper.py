import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
#import cv2 as cv
import pickle
import sqlite3
#import matplotlib as plt

# == Logo
def logo():
    # source: jason-leung from unsplash
    logo = "images/rkd_logo_fin.png"
    image = Image.open(logo)
    img_logo = np.array(image) 
    img_shape = (150, 100)
    #img_logo = cv.resize(img_logo, img_shape, interpolation=cv.INTER_AREA)
    #st.sidebar.image(img_logo)
#logo()
# == Home =======================================================================================
def home():
    st.markdown("""
   **Movie Picker** This help you to a random movie to watch
    """)

    image = Image.open('images/cover.png')
    image = np.array(image) 
    img_shape = (120, 30)
    #image = cv.resize(image, img_shape, interpolation=cv.INTER_AREA)
    st.image(image, caption='Movie Picker', use_column_width=True)

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

    n_movies = len(titles)

    
    idx = random.randrange(0, n_movies) 
    print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')

def movie_picker_off():
    """for Offline"""
    df = pd.read_csv("data/movies_list.csv")
    n_movies = df.shape[0]
    idx = random.randrange(0, n_movies)

    title =  df.titles[idx]
    year = df.years[idx]
    rating = df.ratings[idx]
    actors = df.actors_list[idx]

   
# == About ======================================================================
def about():
    st.markdown("""
    ### Motivation
    **Diabetes** is one of the diseases that affects many people in the world, detecting it early will allow effective 
   care taking of patient. This application  allows automatic and rapid prediction of diabetes in **prediabetic stage** 
   using certain symptom measurements.
   """)

    st.markdown("""
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
            <div style="background-color:blue;padding:1px">
            <h4 style="color:white;text-align:center;">Kiese Diangebeni Reagan </h4>
            <p style="color:red;text-align:center;"> = Datalogue Date Passionate =</p>
            <p style="color:white;text-align:center;">www.kiese.tech, 
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