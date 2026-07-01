import streamlit as st
from faqs import faqs
from difflib import get_close_matches

st.title("🤖 FAQ Chatbot")

user_question = st.text_input("Ask your question")

if st.button("Get Answer"):
    questions = list(faqs.keys())
    match = get_close_matches(user_question, questions, n=1, cutoff=0.4)

    if match:
        st.success(faqs[match[0]])
    else:
        st.error("Sorry! I don't know the answer.")