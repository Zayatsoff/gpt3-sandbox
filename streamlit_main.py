# Written by https://github.com/Zayatsoff

import streamlit as st
from streamlit_webapp import web_app
from api import GPT

webapp = web_app()
hi = webapp.num_tokens()
gpt = GPT(engine="text-davinci-001", temperature=0.7, max_tokens=hi)
print(hi)
webapp.run(gpt)
