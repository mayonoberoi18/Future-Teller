import streamlit as st
import streamlit.components.v1 as components

# Load your HTML file
with open("future-teller.html", "r", encoding="utf-8") as f:
    html_contentmt = f.read()

# Render it in the app
components.html( height=600, scrolling=True)
