import streamlit as st
list_models = ["LLama2","Zerphyr 7B"]
def default_config():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
        .block-container {padding-top:0rem}
        div.stButton > button:first-child {
        background-color: transparent;
        border-radius: 0px;
        border: 0px
        </style>
        """, unsafe_allow_html=True)

    # Divide into ration
    with st.sidebar:
        st.button("New chat")