# Written by https://github.com/Zayatsoff

import streamlit as st
from config import api_key
import openai

API_KEY = api_key


class web_app:
    def __init__(
        self,
        description="Description",
        button_text="Submit",
        placeholder=" ",
    ):
        self.btn_txt = button_text
        self.placeholder = placeholder
        self.desc = description
        self.set_openai_key(API_KEY)

    def run(self, gpt):
        st.title("OpenAi's text-davinci-001")
        st.write(" ### Input instructions:")
        self.input = st.text_area(self.placeholder)
        self.button = st.button(self.btn_txt)
        try:
            if self.button:
                st.header("**Result**")
                answer = gpt.submit_request(self.input)
                with st.container():
                    st.markdown(answer["choices"][0]["text"])
        except Exception as e:
            st.success(f"Something Went Wrong! {e}")

    def set_openai_key(self, key):
        """Sets OpenAI key."""
        openai.api_key = key
