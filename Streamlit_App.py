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
    st.write("Welcome to my WW2 Bombings Dashboard!")
    st.write("Watch as World War 2 unfolds, with an animated visualization of the bombing locations over the course of the war.")


    # plotting gif
    filepath = "gifs/mainviz.gif"
    data_url = get_gif(filepath)
    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def europe():

    st.title("Europe Page")
    st.write("Welcome to the Europe page!")

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
    st.write("Welcome to the Asia page!")
    st.write("")
    st.write("")
    st.write("")
    st.write("Expect to wait a while before activity reaches Asia")

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
