import streamlit as st


def style_background_home():
    # Injecting custom CSS to change the background color
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #5865F2 !important;
            }
            .stApp div[data-testid="stColumn"]{
                background-color: #E0E3FF !important;
                padding:2.5rem !important;
                border-radius:5rem !important;
            }
            div[data-testid="stColumn"] h2 {
                font-family: "Climate Crisis", sans-serif !important;
                font-size: 2.2rem !important;
                color: #222222 !important;
                line-height: 1.2 !important;
                margin-bottom: 1rem !important;
                }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    # Injecting custom CSS to change the background color
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def style_base_layout():
    # Injecting custom CSS to change the background color
    st.markdown(
        """
        <style>
            /*Hide top bar of streamlit */

            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Outfit:wght@100..900&display=swap');
            
            #MainMenu,footer,header {
                visibility: hidden;
            }
            .block-container {
                padding-top:1.5rem !important;
            }
            h1 {
                font-family: "Climate Crisis",sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.3rem !important;
                color: #FFFFFF !important;
                margin-bottom:0rem !important;
            }
            h2 {
                font-family: "Climate Crisis",sans-serif !important;
                font-size: 2.2rem !important;
                line-height: 1.3rem !important;
                margin-bottom:1 rem !important;
                margin-top:1rem !important;
            }
            h3,h4,p {
                font-family: "Outfit",sans-serif !important;

            }

            button[kind = "Primary"]{
                bottom-radius: 1.5rem !important;
                color: white !important;
                background: #5865F2 !important;
                padding:none !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind = "secondary"]{
                bottom-radius: 1.5rem !important;
                color: white !important;
                background: #EB459E !important;
                padding:none !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind = "tertiary"]{
                bottom-radius: 1.5rem !important;
                color: white !important;
                background: black !important;
                padding:none !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button:hover{
                transform:scale(1.05);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
