import streamlit as st
import base64


# generic function to load gifs into streamlit markdown from filepath
def get_gif(filepath):
    file_ = open(filepath, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


def home(): # home page

    st.title("World War 2 Bomings Animated")
    st.markdown("### Intro")
    st.write("Welcome to my WW2 Bombings Dashboard!")
    st.write("")
    st.write("Watch as World War 2 unfolds, with an animated visualization of devastating bombings that shaped the course of the war across the globe.")
    st.write("")
    st.write("Scroll down in this tab for a global bombing map animation, or the Europe/Asia tabs for their respective regions. If you cannot see the other tabs on the right, click the '>' symbol in the top left of the screen")
    st.image("images/pic1.jpg")
    st.markdown("### About the Data")
    st.write("The data is from The Theater History of Operations Reports (THOR) datase (see Acknowledgements tab for more info), and a public domain dataset with events throughout the years from Kaggle.")
    st.write("")
    st.write("This dataset only captures the bomb locations from Allied forces, although I am working on scraping further data relating to Axis bombing targets.")
    st.write("")
    st.markdown("### Animation of (Allied) global bombing activity during WW2")
    # plotting gif
    filepath = "gifs/mainviz.gif"
    data_url = get_gif(filepath)
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def europe():

    st.title("Europe Page")
    st.write("Welcome to the Europe page. Please see below the map of European bombs as World War 2 unfolds.")
    st.markdown("### Animation of (Allied) WW2 European bombing activity")
    # plotting gif
    filepath = "gifs/Europeviz.gif"
    data_url = get_gif(filepath)
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )

def Acknowledgements():
    st.title("Acknowledgements")
    st.write("1 - Lt Col Jenns Robertson of the US Air Force developed the Theater History of Operations Reports (THOR) and posted them online after receiving Department of Defense approval.")
    st.write("2 - Events data is public domain, sourced from: https://www.kaggle.com/datasets/ramjasmaurya/world-war-2-archive")


def asia():

    st.title("Asia Page")
    st.write("Welcome to the Asia page. Please see below the map of Asian/Australian bombs as World War 2 unfolds.")
    st.write("")
    st.write("Expect to wait a while before you see any activity in Asia.")
    st.write("")
    st.write("")
    st.markdown("### Animation of (Allied) WW2 Asian/Oceania bombing activity")
    # plotting gif
    filepath = "gifs/Asiaviz.gif"
    data_url = get_gif(filepath)
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Europe", "Asia", "Acknowledgements"])

    if page == "Home":
        home()
    elif page == "Europe":
        europe()
    elif page == "Asia":
        asia()
    elif page == "Acknowledgements":
        Acknowledgements()


if __name__ == "__main__":
    main()
