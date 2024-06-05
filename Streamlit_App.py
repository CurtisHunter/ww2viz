import streamlit as st
import base64

def get_gif(filepath):
    file_ = open(filepath, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url


def home():

    st.title("Home Page")
    st.write("Welcome to the Home page!")

    filepath = "gifs/mainviz.gif"
    data_url = get_gif(filepath)

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def europe():


    st.title("Europe Page")
    st.write("Welcome to the Europe page!")

    filepath = "gifs/Europeviz.gif"
    data_url = get_gif(filepath)

    st.write(filepath)

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def asia():

    st.title("Asia Page")
    st.write("Welcome to the Asia page!")
    st.write("Expect to wait a while before activity reaches Asia")

    filepath = "gifs/Asiaviz.gif"
    data_url = get_gif(filepath)

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="main viz">',
        unsafe_allow_html=True,
    )


def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Europe", "Asia"])

    if page == "Home":
        home()
    elif page == "Europe":
        europe()
    elif page == "Asia":
        asia()


if __name__ == "__main__":
    main()
