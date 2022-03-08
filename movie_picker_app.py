import streamlit as st


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
    # basic layout
    menu = ["Home", "Movie List", "Pick Random Movie", "About"]
    choice = st.sidebar.radio("Menu", menu)
    # siderbar method
    #st.write(dir(st.sidebar))

    html_temp = """
    <div style="background-color:blue;padding:0.5px">
    <h1 style="color:white;text-align:center;">Diabetes Prediction </h1>
    </div><br>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)

    if choice == "Home":
        #st.title("Home")
        
        home()
    elif choice == "Movie List":
        st.subheader("Movie Collection")
        movi_list()

    elif choice == "Pick Random Movie":
        st.header("Pick Random Movie")
        pick_movie_on()
        #pick_movie_off()

    elif choice == "About":
        #st.title("About")
        about()


    footer()

if __name__ == '__main__':
    main()