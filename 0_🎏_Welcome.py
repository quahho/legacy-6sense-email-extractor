# Imports
import streamlit as st

# ==============================================================================================

# Set tab info
st.set_page_config(
    page_title="Welcome",
    page_icon="🎏"
)

# ==============================================================================================

# Add sidebar header
st.sidebar.header("About This App")

# Add 6sense logo
st.sidebar.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/6sense-logo.png", use_column_width='always', caption='Made for the one and only')

# Add 2X logo
st.sidebar.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/2x-logo.png", use_column_width='always', caption='Proudly brought to you by')

# Add personal link
st.sidebar.text('')
st.sidebar.write("Powered by : [Vincent Quah](https://bit.ly/3BvREYT)")
st.sidebar.caption('© 2022 Quahho | Handmade in Klang.')
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')

# ==============================================================================================

# Create page title
st.title('Welcome to Streamlit! 🎏')

# Set paragraph text
st.text('')
st.write(
"""
    Hello there! 👋 Welcome to the Streamlit app built specifically to extract the top accounts data from 6sense emails.
    Its modus operandi has two parts which are to be selected from the sidebar. 👈
"""
)
st.text('')
st.subheader('Modus Operandi')
st.write(
"""
    1. Email Conversion 📧
    - Open email in Outlook Web
    - Save email as EML file 
    - Proceed to external converter site
    - Convert EML file to HTML file
"""
)
st.text('')
st.write(
"""
    2. Web Page Extraction 📰
    - Upload HTML file on Streamlit
    - Click button to start process
    - Obtain compiled output CSV file 
"""
)
st.text('')
st.write(
"""
    Each step will be explained in detail with pictures 🖼️ in their respective pages. 
    So head on over there whenever you are ready to get started. Cheers! 🍹
"""
)

# ==============================================================================================
