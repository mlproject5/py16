import streamlit as st
from transformers import pipeline
import random
import re

st.set_page_config(page_title='HeadlineGen', page_icon='news.png', layout="centered", initial_sidebar_state="auto", menu_items=None)

hide_streamlit_style = """
    <style>
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def hgen1():
    def generate_headline(news_paragraph):
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', news_paragraph)
        headline = random.choice(sentences)
        headline = headline.strip()
        return headline

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>News Headline "
            "Generator</h1></center>",
            unsafe_allow_html=True)

        news_paragraph = st.text_area("Enter a news paragraph", height=200, key="hgen1_text_area")

        if st.button("Generate Headline"):
            if news_paragraph:
                headline = generate_headline(news_paragraph)
                st.success(headline)
            else:
                st.warning("Please enter a news paragraph.")

    if __name__ == "__main__":
        main()

def hgen2():
    def generate_headline(news_paragraph):
        summarization_pipeline = pipeline("summarization")

        while True:
            summary = summarization_pipeline(news_paragraph, max_length=50, min_length=10, do_sample=False)[0][
                'summary_text']
            sentences = summary.split('. ')

            capitalized_sentences = [sentence.capitalize() for sentence in sentences]

            capitalized_summary = '. '.join(capitalized_sentences)

            if capitalized_summary[0].isalpha():
                return capitalized_summary

    def main():
        st.markdown(
            "<center><h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 32px;'>News Headline "
            "Generator</h1></center>",
            unsafe_allow_html=True)

        news_paragraph = st.text_area("Enter a news paragraph", height=200, key="hgen2_text_area")

        if st.button("Generate Headline"):
            if news_paragraph:
                headline = generate_headline(news_paragraph)
                st.success(headline)
            else:
                st.warning("Please enter a news paragraph.")

    if __name__ == "__main__":
        main()


def main():
    st.sidebar.markdown("""
            <style>
                .sidebar-text {
                    text-align: center;
                    font-size: 32px;
                    font-weight: bold;
                    font-family: Comic Sans MS;
                }
            </style>
            <p class="sidebar-text">Headline</p>
        """, unsafe_allow_html=True)
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTqY_1bS-UuoRjHbYJAxUdrNrBgYsT22f3zJw&usqp=CAU",
        use_column_width=True)
    st.sidebar.markdown("<h1 style='font-family: Comic Sans MS; font-weight: 300; font-size: 24px;'>News Headline "
                "Generator</h1></center>", unsafe_allow_html=True)
    selected_sidebar = st.sidebar.radio("Please Select One", ["Method 1", "Method 2"])

    if selected_sidebar == "Method 1":
        hgen1()
    elif selected_sidebar == "Method 2":
        hgen2()

if __name__ == "__main__":
    main()
