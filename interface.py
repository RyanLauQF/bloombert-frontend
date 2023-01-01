import streamlit as st
import json
import requests

st.title("BloomBERT: A Task Classifier based on Blooms Taxonomy")

user_input = st.text_input("Enter task")

json_input = {"text": user_input}

if st.button('Calculate') or user_input:
    # post a request to backend api running on Google Cloud
    res = requests.post(url="https://bloom-bert-api-dmkyqqzsta-as.a.run.app/predict", data=json.dumps(json_input))
    st.write(res.json())
