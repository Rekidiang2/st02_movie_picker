import streamlit as st
from helper import home, movi_list, pick_movie_off, pick_movie_on, about, footer, logo


# Sidebar Configuration
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#99ffcc,#99ffcc);
    color: purple;
}
</style>
""",
    unsafe_allow_html=True,
)

def main():
    logo()
    st.sidebar.title("Movie Picker")
    # basic layout
    menu = ["Pick Movie", "Movie List", "About"]
    choice = st.sidebar.radio("Menu", menu)
    # siderbar method
    #st.write(dir(st.sidebar))

    html_temp = """
    <div style="background-color:blue;padding:0.5px">
    <h1 style="color:white;text-align:center;">Movie Picker </h1>
    </div><br>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)

    if choice == "Pick Movie":
        #st.title("Home")
        #pick_movie_on()
        pick_movie_off()
    elif choice == "Movie List":
        st.subheader("Movie Collection")
        movi_list()

    elif choice == "About":
        #st.title("About")
        about()


    footer()

if __name__ == '__main__':
    main()