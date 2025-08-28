import streamlit as st

def show_guide_utilisateur():
    st.write("guide")

    st.markdown("""
        <style>
                
            .stApp {
                margin-top: 0;
                padding: 0;
                background-color: #f2f2f2; 
            }
                
        </style>
    """, unsafe_allow_html=True)