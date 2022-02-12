import streamlit as st
from streamlit_webapp import web_app
from api import GPT

webapp = web_app()
gpt = GPT(engine="text-davinci-001", temperature=0.7, max_tokens=10)
webapp.run(gpt)
