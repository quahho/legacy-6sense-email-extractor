# Imports
import streamlit as st

# ==============================================================================================

# Set tab info
st.set_page_config(
    page_title="Email Conversion",
    page_icon="📧"
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
st.title('Email Conversion 📧')
st.text('')

# Quick links
st.write(
"""
    🔗 **Quick Links**
    - [Outlook Web](https://outlook.office.com/mail/)
    - [Online Converter](https://www.aconvert.com/document/eml-to-html/) 
"""
)
st.markdown("---")

# Set paragraph for Step 1
st.subheader('Step 1: Download Email From Outlook’s Web Version')
st.text('')

st.write("Proceed to [Outlook Web](https://outlook.office.com/mail/) and sign in to your email account on the site if you haven’t already.")

st.write("In the inbox section, select the email you want to download.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/inbox.png", use_column_width='auto', caption='An email being selected in the inbox')
st.text('')

st.write("In the email section, at the top-right corner, click the three dots.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/dots.png", use_column_width='auto', caption='The triple dot being selected at the top right corner of the email')
st.text('')

st.write("In the menu that opens, choose “Download”.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/download.png", use_column_width='auto', caption='Download option found in the list')
st.text('')

st.write("The downloaded email, having the EML extension, will appear in the Downloads folder.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/email-output.png", use_column_width='auto', caption='Downloaded emails in the Downloads folder')
st.markdown("---")

# Set paragraph for Step 2
st.subheader('Step 2: Convert Email to Web Page Using Online Converter')
st.text('')

st.write("Proceed to [Online Converter](https://www.aconvert.com/document/eml-to-html/) and turn off any ad-blocker to prevent limited usage of the site's services.")

st.write("In the center of the site, choose the downloaded email to be converted through the 'Choose Files' button.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/choose-file.png", use_column_width='auto', caption='Choose Files button being selected')
st.text('')

st.write("It is possible to choose one or more file(s) at one go in the file explorer that pops out.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/choose-email.png", use_column_width='auto', caption='Downloaded emails being selected')
st.text('')

st.write("After selection of files, click the 'Convert Now' button to start the conversion process.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/convert.png", use_column_width='auto', caption='Convert Now button being selected')
st.text('')

st.write("The converted emails, now as web pages and having the HTML extension, will appear in a result table.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/conversion-result.png", use_column_width='auto', caption='Converted files listed in a table')
st.markdown("---")

# Set paragraph for Step 3
st.subheader('Step 3: Download Web Page From Generated URL Link')
st.text('')

st.write("In the result table, the generated URL links of the web pages are beside their respective file names.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/generated-link.png", use_column_width='auto', caption='Generated links in the result table')
st.text('')

st.write("To download the web page, right click the generated URL link and select 'Save Link As...' option.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/save-link.png", use_column_width='auto', caption='The Save Link As option being selected')
st.text('')

st.write("In the file explorer that pops out, ensure that the 'Save as type' option is 'HTML Documents (*.html)'.")
st.write("Before clicking the 'Save' button, rename the file accordingly for ease of identifying it later.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/save-webpage.png", use_column_width='auto', caption='The web page being downloaded')
st.text('')

st.write("The downloaded web pages, having the HTML extension, will appear in the Downloads folder.")
st.image("https://raw.githubusercontent.com/quahho/6sense-email-extractor-images/main/webpage-output.png", use_column_width='auto', caption='Downloaded web pages in the Downloads folder')
st.text('')

st.write("With the downloaded web pages ready, head over to the next page for the web page extraction part.")

# ==============================================================================================
