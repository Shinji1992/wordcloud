import streamlit as st
from wordcloud import WordCloud
import trafilatura

st.write("# Create Word Cloud")
st.write("[by Shinji](https://github.com/Shinji1992)")

def main():
    max_word = st.sidebar.slider("Max Words", 100, 1000,500)
    max_font = st.sidebar.slider("Max Font Size", 50, 500,100)
    width = st.sidebar.slider("Width", 100, 1000,600)
    height = st.sidebar.slider("Height", 100, 1000,300)
    color_list = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
    color = st.sidebar.selectbox('Color',color_list)
    background_color_list = ['white','black','red', 'green', 'blue', 'yellow']
    background_color = st.sidebar.selectbox('Background Color',background_color_list)

    user_input = st.text_input("Paste URL")
    if user_input is not None:
        if st.button("Create"):
            downloaded = trafilatura.fetch_url(user_input)
            text = trafilatura.extract(downloaded, include_comments=False, include_tables=False)
            word_cloud = WordCloud(background_color=background_color,colormap=color,
            max_words=max_word,max_font_size=max_font,width=width, height=height).generate(text).to_array()
            st.image(word_cloud)

if __name__=="__main__":
  main()
