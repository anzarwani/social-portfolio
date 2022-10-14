import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Social Linktree")
st.write("Book Blogging | Python Dev | Data Science | Ocassionaly a poet | Sometimes a storyteller")

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
    
lottie_animation_1 = "https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json"
 
lottie_anime_json = load_lottie_url(lottie_animation_1)

lottie_animation_2 = "https://assets5.lottiefiles.com/packages/lf20_puciaact.json"
 
lottie_anime_json_2 = load_lottie_url(lottie_animation_2)


st_lottie(lottie_anime_json, key = "hello")
st.write("______________________________________________________________")


st.subheader("works on medium")

link = '[Tonight — Ghazal by Agha Shahid Ali — A Brief Summary](https://medium.com/aghashahidali/tonight-ghazal-by-agha-shahid-ali-a-brief-summary-d4ed1065f902)'
st.markdown(link, unsafe_allow_html=True)

link1 = '[I Dream I Am At The Ghat Of The Only World — An Overview](https://medium.com/@anzar-wani2/i-dream-i-am-at-the-ghat-of-the-only-world-an-overview-3a20af2194a3)'
st.markdown(link1, unsafe_allow_html=True)

link2 = '[Undertones](https://medium.com/@anzar-wani2/undertones-82bb233c7ade)'
st.markdown(link2, unsafe_allow_html=True)

st.subheader("works on github")

link3 = '[Librinth - Literature Blog](https://github.com/anzarwani/librinth)'
st.markdown(link3, unsafe_allow_html=True)

link4 = '[Linear Regression Model Comparison](https://github.com/anzarwani/linear-regression-model-comparison)'
st.markdown(link4, unsafe_allow_html=True)

link5 = '[Heart Attack Chance Prediction](https://github.com/anzarwani/Heart-Attack-Chance-Prediction)'
st.markdown(link5, unsafe_allow_html=True)

