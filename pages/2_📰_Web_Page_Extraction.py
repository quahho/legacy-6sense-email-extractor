# Imports
from random import randint
import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup

# ==============================================================================================
# TAB SETTINGS

# Set tab info
st.set_page_config(
    page_title="Web Page Extraction",
    page_icon="📰"
)

# ==============================================================================================
# ==============================================================================================
# SIDEBAR SETTINGS

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
# ==============================================================================================
# GLOBAL VARIABLES & 

# Initialize global variables
pair = {}
summary_timeframe_list = []
summary_segment_list = []
total_account_list = []
content_timeframe_list = []
content_segment_list = []
account_list = []
domain_list = []
country_list = []
category_list = []
buying_stage_list = []
profile_fit_list = []
account_reach_list = []
active_contact_list = []
web_visit_count_list = []
known_contact_count_list = []
anonymous_count_list = []
web_url_list = []
web_raw_url_list = []
keyword_list = []
bombora_topic_list = []

# Method for extracting a single HTML file
def extractFile(file_name):

    # Feed file to parser
    soup = BeautifulSoup(file_name, "lxml")
    
    try:
        # Get the main content 
        # Route: root -> table -> table -> thead + tbody (clean newline rows)
        content_table_html = [x for x in soup.find("table").find("table").contents if x != '\n']

    except:
        # Set error message if main content cant be found
        st.error('No data could be extracted from the HTML file : ' + file_name.name, icon="🚨")
        st.warning("""
            Possible causes of the *'No data could be extracted from HTML file'* error :
            - Wrong web page being uploaded
            - Update in web page's source code      
        """, icon="⚠️")

        # Set the error state
        global any_start_error 
        any_start_error = True

        # Get out of method block immediately after encountering error
        return

    # --------------------------------------------------------------------------------------------------------------------------------------------------------------

    try:
        # Divider for each run of the script
        # print('============================================================================================')
        
        # Get intro page content
        # Route: content table -> thead -> all tr (clean newline rows)
        intro_page_html = [x for x in content_table_html[0].contents if x != '\n']

        # Get title content
        # Route: intro page -> 1st tr -> table -> tbody (skipped) -> all tr (clean newline rows)
        title_info_html = [x for x in intro_page_html[0].find("table").find_all("tr") if x != '\n']

        # Get segment name
        # Route: title info -> 3rd tr
        segment = title_info_html[2].text.split(':')[1].strip()
        # print('Segment:', segment)

        # Append to summary segment list
        summary_segment_list.append(segment)
        
        # Get non title content
        # Route: intro page -> 2nd tr -> table -> table -> tbody (skipped) -> tr -> all td (clean newline rows)
        non_title_info_html = [x for x in intro_page_html[1].find("table").find("table").find("tr").contents if x != '\n']

        # Get timeframe of data
        # Route: non title info -> 1st td
        timeframe = non_title_info_html[0].text.split(':')[1].strip()
        # print('Timeframe:', timeframe)

        # Append to summary timeframe list
        summary_timeframe_list.append(timeframe)

        # --------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Get account profile pages content
        # content table -> tbody -> tr (skipped) -> td -> all table
        profile_page_html_blocks = [x for x in content_table_html[1].find("td").contents if x.name == 'table']

        # Append to count list
        # total_account_list.append(str(len(profile_page_html_blocks)))
        # print('Total Accounts:', str(len(profile_page_html_blocks)))

        # Extend to timeframe list - set length of list to equal to total accounts found
        # content_timeframe_list.extend([timeframe] * len(profile_page_html_blocks))

        # Extend to content segment list - set length of list to equal to total accounts found
        # content_segment_list.extend([segment] * len(profile_page_html_blocks))

        # Counter
        counter = len(profile_page_html_blocks)

        # Loop through each block to get each account data
        for index, block in enumerate(profile_page_html_blocks):

            # Divider for each account in email
            # print('==============================================')
            # print("Counter:", str(index + 1))

            # Define placeholder
            handled_block = ''

            # Handle case where tbody can be missing
            if block.find_next().name == 'tbody':

                # Go to tbody before getting all tr
                handled_block = block.find_next().contents

            elif block.find_next().name == 'tr':
                
                # Get all tr straightaway
                handled_block = block.contents

            # Remove empty child tr in block
            # Route: block -> tbody -> all tr (clean newline rows)
            clean_block = [x for x in handled_block if x != '\n']

            # --------------------------------------------------------------------------------------------------------------------------------------------------------------
            try:
                # Get the company info part
                # Route: clean block -> 1st tr -> table -> tbody (clean newline rows)
                company_info_html = [x for x in clean_block[0].find("table").find_all("tr") if x != '\n']

                # Get account
                # Route: company info -> 1st tr -> span
                account = company_info_html[0].find("span").text.strip()
                # print("Account:", account)
                
                # Check for 6QA
                if '6QA' in company_info_html[0].text:
                    account = account + '; 6QA'

                # Append to account list
                # account_list.append(account)

                # Get domain
                # Route: company info -> 2nd tr
                domain = company_info_html[1].text.split(',')[0].strip()
                # print("Domain:", domain)

                # Append to domain list
                # domain_list.append(domain)

                # Get country
                # Route: company info -> 2nd tr
                country = company_info_html[1].text.split(',')[1].strip().replace('\n', '')
                # print("Country:", country)

                # Append to country list
                # country_list.append(country)

                # Get category
                # Route: company info -> 3rd tr -> span
                category = company_info_html[2].find("span").text.title().strip()
                # print("Category:", category)

                # Append to category list
                # category_list.append(category)

                #--------------------------------------------------------------------------------------------------------------------------------------------------------------

                # Get the field info part
                # Route: clean block -> 2nd tr
                field_info_html = [x for x in clean_block[1].contents if x != '\n']

                # Get buying stage
                # Route: field info -> 1st tr
                buying_stage = field_info_html[0].text.split(':')[-1].strip()
                # print("Buying Stage:", buying_stage)

                # Append to buying stage list
                # buying_stage_list.append(buying_stage)

                # Get profile fit
                # Route: field info -> 2nd tr
                profile_fit = field_info_html[1].text.split(':')[-1].strip()
                # print("Profile Fit:", profile_fit)

                # Append to profile fit list
                # profile_fit_list.append(profile_fit)

                # Get account reach
                # Route: field info -> 3rd tr
                account_reach = field_info_html[2].text.split(':')[-1].strip()
                # print("Account Reach:", account_reach)

                # Append to account reach list
                # account_reach_list.append(account_reach)

            except:
                counter = counter - 1
                break
                

            #--------------------------------------------------------------------------------------------------------------------------------------------------------------

            # Append to account list
            account_list.append(account)

            # Append to domain list
            domain_list.append(domain)

            # Append to country list
            country_list.append(country)

            # Append to category list
            category_list.append(category)

            # Append to buying stage list
            buying_stage_list.append(buying_stage)

            # Append to profile fit list
            profile_fit_list.append(profile_fit)

            # Append to account reach list
            account_reach_list.append(account_reach)

            #--------------------------------------------------------------------------------------------------------------------------------------------------------------

            # Get the stat info part
            # Route: clean block -> 3rd tr and beyond
            stat_info_html = clean_block[2:]

            # Boolean variables
            has_active = False
            has_webvisit = False
            has_keyword = False
            has_bombora = False

            # Loop through each possible stat row
            for stat in stat_info_html:

                # Check for active contact row
                if stat.text.find("Active") >= 0:

                    # Get target line
                    # Route: 3rd tr and beyond -> table -> tbody -> all tr except 1st tr
                    target_line = [x for x in stat.find("table").find_all("tr") if x != '\n'][1:]

                    # Initialize loop variable
                    i = 0

                    # Initialize contact list
                    contact_list = []

                    # Loop over the contact rows with an interval of 2 (1 is contact info, 1 is contact action)
                    # Stops at the last item since it doesnt have a next item
                    while i < (len(target_line) - 1):

                        # Get contact name
                        contact_name = target_line[i].find("span").text.strip()

                        # Get contact social
                        contact_social = [x.text.strip() for x in target_line[i].find_all("a")]

                        # Create a to-be-removed list - to remove contact name and contact social from full contact info line
                        contact_social.append(contact_name)
                        removed_stuff_list = list(contact_social)
                        
                        # Get full contact info list
                        full_contact_info_line = target_line[i].text.replace('\n', ' ').strip(',').replace(contact_name, '')
                        full_contact_info_list = full_contact_info_line.split(' ')

                        # Get contact job
                        contact_job = ' '.join([x.strip() for x in full_contact_info_list if x not in removed_stuff_list and len(x) > 0]).strip(',').strip()

                        # Get contact email
                        contact_email = target_line[i].find("a")['href'].split(':')[-1].strip()
                        
                        # Clean action string
                        action_str = [[y.strip() for y in x.text.split(' ') if y != '\n' and len(y) > 0] for x in target_line[i + 1].find_all("li")]

                        # Get contact action
                        contact_action = ' | '.join([' '.join(x) for x in action_str])

                        # Put all contact stuffs together, separated by semi colon
                        contact = contact_name + '; ' + contact_email + '; ' + contact_job + '; ' + contact_action
                        # print("Contact:", contact)

                        # Append to contact list
                        contact_list.append(contact)

                        # Set interval of 2
                        i += 2

                    # Append to active contact list
                    active_contact_list.append(' // '.join(contact_list))

                    # Set boolean variable
                    has_active = True 

                # Check for web visit row
                if stat.text.find("Web Visit") >= 0:

                    # Get target line
                    target_line = stat.text
                    
                    # Clean web visit string
                    numbers_only_list = [x for x in target_line.split(' ') if x.isnumeric()]

                    # Get web visit count
                    web_visit = numbers_only_list[0].strip()
                    # print('Web Visit Count:', web_visit)

                    # Append to web visit count list
                    web_visit_count_list.append(web_visit)

                    # Get known contact count
                    known_contact = numbers_only_list[1].strip()
                    # print('Known Contact Count:', known_contact)

                    # Append to known contact count list
                    known_contact_count_list.append(known_contact)

                    # Get anonymous count
                    anonymous = numbers_only_list[2].strip()
                    # print('Anonymous Count:', anonymous)

                    # Append to anonymous count list
                    anonymous_count_list.append(anonymous)
                    
                    # Get all URLs
                    # Route: 3rd tr and beyond -> table -> tbody (skipped) -> all tr except 1st tr
                    url_list = [x.text.strip().split(',')[0] for x in stat.find("table").find_all("tr") if x != '\n'][1:]
                    # print("URL List:", url_list)

                    # Append to known contact count list
                    web_url_list.append(', '.join(url_list))
                    
                    # Route: 3rd tr and beyond -> table -> tbody (skipped) -> all tr
                    raw_url_list = [x.find("a")["href"] for x in stat.find("table").find_all("tr") if x != '\n' and 'href' in str(x)]
                    # print("Raw URL List:", raw_url_list)

                    # Append to raw web url list
                    web_raw_url_list.append(', '.join(raw_url_list))

                    # Set boolean variable
                    has_webvisit = True 
            
                # Check for keyword row
                if stat.text.find("Keyword") >= 0:

                    # Get target line
                    # Route: 3rd tr and beyond -> table -> tbody (skipped) -> last tr -> all span
                    target_line = [x for x in stat.find("table").find_all("tr") if x != '\n'][-1].find_all("span")

                    # Combine the list elements together and remove empty elements
                    keywords_array = [x.text.strip() for x in target_line if len(x.text.strip()) > 0]
                    # print("Keywords:", keywords_array)

                    # Append to profile fit list
                    keyword_list.append(', '.join(keywords_array))

                    # Set boolean variable
                    has_keyword = True 

                # Check for bombora row
                if stat.text.find("Intent") >= 0:

                    # Get target line
                    # Route: 3rd tr and beyond -> table -> tbody (skipped) -> last tr -> all span
                    target_line = stat.find("table").find_all("tr")[-1].text

                    # Get bombora topic
                    bombora_topic = target_line.split(':')[-1].strip()
                    # print("Bombora Topic:", bombora_topic)

                    # Append to bombora topic list
                    bombora_topic_list.append(bombora_topic)

                    # Set boolean variable
                    has_bombora = True 

            
            # Insert empty strings when no occasional data
            if has_active == False:

                # Case when no active contact row
                active_contact_list.append('')

            if has_webvisit == False:

                # Case when no web visit row
                web_visit_count_list.append('') 
                known_contact_count_list.append('') 
                anonymous_count_list.append('')
                web_url_list.append('')
                web_raw_url_list.append('')

            if has_keyword == False:

                # Case when no keyword row
                keyword_list.append('')

            if has_bombora == False:

                # Case when no bombora row
                bombora_topic_list.append('')


        # QUICK FIX 
        # Append to count list
        total_account_list.append(str(counter))
        # print('Total Accounts:', str(len(profile_page_html_blocks)))

        # Extend to timeframe list - set length of list to equal to total accounts found
        content_timeframe_list.extend([timeframe] * counter)
        print(timeframe)
        print(len(account_list))

        # Extend to content segment list - set length of list to equal to total accounts found
        content_segment_list.extend([segment] * counter)

    except Exception as e:
        # Set error message if main content cant be found
        st.error('An error was encountered while extracting the HTML file : ' + file_name.name, icon="🚨")
        st.warning("""
            Possible causes of the *'An error was encountered while extracting the HTML file'* error :
            - Web page itself has no data
            - Update in web page's source code

            Reach out to creator for assistance of this issue.
        """, icon="⚠️")

        # Create an expander to show error description
        with st.expander("View Error Message"):
            st.exception(e)
       
        # Set the error state
        global any_run_error 
        any_run_error = True

        # Get out of method block immediately after encountering error
        return        

# Method for enable the state after download button has been clicked
def enableDownloadedStatus():

    # Change downloaded status
    st.session_state.downloaded_status = True

# Method for disable the state after download button has been clicked
def disableDownloadedStatus():

    # Change downloaded status
    st.session_state.downloaded_status = False

# ==============================================================================================
# ==============================================================================================
# SESSION STATE VARIABLES

# Set session variable 
if 'uploaded_file_count' not in st.session_state:
    st.session_state.uploaded_file_count = 0

if 'downloaded_status' not in st.session_state:
    st.session_state.downloaded_status = False

if 'post_summary_dataframe' not in st.session_state:
    st.session_state.post_summary_dataframe = ''

if 'post_content_dataframe' not in st.session_state:
    st.session_state.post_content_dataframe = ''

# ==============================================================================================
# PRE RESULT LAYOUT

# Create page title
st.title('Web Page Extraction 📰')
st.text('')

# Step 1 Header
st.subheader('Step 1: Select Extract Date')

# Date input for extract date
selected_date = st.date_input("When's the date of web page extraction")
st.text('')

# Convert date to other formats
main_date = '{dt.day}/{dt.month}/{dt.year}'.format(dt=selected_date)
alt_date = '[{dt.day}-{dt.month}-{dt.year}]'.format(dt=selected_date)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Step 2 Header
st.subheader('Step 2: Select Web Pages')

# Set key for file uploader
if 'key' not in st.session_state: 
    st.session_state.key = str(randint(1000, 100000000))

# File uploader - allows multiple files - only accept HTML files
uploaded_files = st.file_uploader("Choose one or more HTML file(s)", type='html', accept_multiple_files=True, key=st.session_state.key)
st.text('')

# Initialize variable for change in file count
file_count_change = False

# File count change occurs when number changes to another number
if len(uploaded_files) != st.session_state.uploaded_file_count:
    file_count_change = True

# Reset output related session variables if there are any changes in file count
if file_count_change:
    st.session_state.downloaded_status = False
    st.session_state.post_summary_dataframe = ''
    st.session_state.post_content_dataframe = ''

# Update session variable for uploaded file count after comparison has been made between before and after
st.session_state.uploaded_file_count = len(uploaded_files)

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Step 3 Header
st.subheader('Step 3: Start Process')

# Obtain session variable of downloaded status before the button - the true value of the variable
post_download_status = st.session_state.downloaded_status

# Run button - only clickable if there are uploaded files
if uploaded_files:
    start_process = st.button('Extract Uploaded Web Pages ⛏️', on_click=disableDownloadedStatus())
else:
    start_process = st.button('Extract Uploaded Web Pages ⛏️', disabled=True)

# ==============================================================================================
# POST RESULT LAYOUT

# Runs before the download button is clicked
if start_process:

    # Initialize a no-error state
    any_start_error = False
    any_run_error = False

    # Extraction result label
    st.text('')
    st.write('Extraction Result:')

    # Set a spinner to wait for extract method to finish
    with st.spinner('Wait for it...'):

        # Loop through each uploaded file
        for uploaded_file in uploaded_files:

            # Runs method when there is no error
            if any_start_error == False and any_run_error == False:
                extractFile(uploaded_file)

    # Runs when there is no error
    if any_start_error == False and any_run_error == False:

        # Create dictionary for output dataframe
        output_dict = {
            'Extract Date': main_date,
            'Timeframe': content_timeframe_list,
            'Segment Name': content_segment_list,
            'Account Name': account_list,
            'Domain': domain_list,
            'Country': country_list,
            'Category': category_list,
            'Buying Stage': buying_stage_list,
            'Profile Fit': profile_fit_list,
            'Account Reach': account_reach_list,
            'Active Contact': active_contact_list,
            'Web Visit Count': web_visit_count_list,
            'Known Contact Count': known_contact_count_list,
            'Anonymous Count': anonymous_count_list,
            'Web URLs': web_url_list,
            'Raw Web URLs': web_raw_url_list,
            'Keywords': keyword_list,
            'Bombora Company Surge Topics': bombora_topic_list
        }
        # print(output_dict)
        print('Extract Date =', len(main_date))
        print('Timeframe =', len(content_timeframe_list))
        print('Segment Name =', len(content_segment_list))
        print('Account Name =', len(account_list))
        print('Domain =', len(domain_list))
        print('Country =', len(country_list))
        print('Category =', len(category_list))
        print('Buying Stage =', len(buying_stage_list))
        print('Profile Fit =', len(profile_fit_list))
        print('Account Reach =', len(account_reach_list))
        print('Active Contact =', len(active_contact_list))
        print('Web Visit Count =', len(web_visit_count_list))
        print('Known Contact Count =', len(known_contact_count_list))
        print('Anonymous Count =', len(anonymous_count_list))
        print('Web URLs =', len(web_url_list))
        print('Raw Web URLs =', len(web_raw_url_list))
        print('Keywords =', len(keyword_list))
        print('Bombora Company Surge Topics =', len(bombora_topic_list))
        # Create output dataframe
        output_dataframe = pd.DataFrame(output_dict)

        # Set the post output dataframe
        st.session_state.post_content_dataframe = output_dataframe

        #---------------------------------------------------------------------------------------

        # Create dictionary for summary dataframe
        summary_dict = {
            'Timeframe': summary_timeframe_list,
            'Segment Name': summary_segment_list,
            'Total Top Accounts': total_account_list
        }

        # Create output dataframe - set index to start from 1
        summary_dataframe = pd.DataFrame(summary_dict)
        summary_dataframe.index = summary_dataframe.index + 1

        # Set the post summary dataframe
        st.session_state.post_summary_dataframe = summary_dataframe

        #---------------------------------------------------------------------------------------
        
        # Print success message
        st.success('Data successfully extracted from all web pages. Process Completed!', icon="✅")

        # Extraction summary label
        st.text('')
        st.write('Extraction Summary:')

        # Display output dataframe
        st.dataframe(summary_dataframe, use_container_width=True)

        # Step 4 Header
        st.text('')
        st.subheader('Step 4: Export Result')

        # Create Download button
        st.download_button(
            label='Download Compiled CSV File 📥',
            data=output_dataframe.to_csv(encoding='utf-8-sig', index=False),
            file_name=alt_date + '-Compiled-6sense-Email-Extracted-Top-Accounts.csv',
            mime='text/csv',
            on_click=enableDownloadedStatus() 
        )

        # Split label
        st.write('------- OR -------')

        # Create Restart button
        if st.button('Restart 🔄') and 'key' in st.session_state.keys():

            # Remove file uploader key and refresh page
            st.session_state.pop('key')
            st.experimental_rerun()


# Runs after the download button has been clicked
elif post_download_status:

    # Extraction result label
    st.text('')
    st.write('Extraction Result:')

    # Print success message
    st.success('Data successfully extracted from all web pages. Process Completed!', icon="✅")

    # Extraction summary label
    st.text('')
    st.write('Extraction Summary:')

    # Display output dataframe
    st.dataframe(st.session_state.post_summary_dataframe, use_container_width=True)

    # Step 4 Header
    st.text('')
    st.subheader('Step 4: Export Result')

    # Create Download button
    st.download_button(
        label='Download Compiled CSV File 📥',
        data=st.session_state.post_content_dataframe.to_csv(encoding='utf-8-sig', index=False),
        file_name= alt_date + '-Compiled-6sense-Email-Extracted-Top-Accounts.csv',
        mime='text/csv',
        on_click=enableDownloadedStatus() 
    )

    # Split label
    st.write('------- OR -------')

    # Create Restart button
    if st.button('Restart 🔄') and 'key' in st.session_state.keys():

        # Remove file uploader key and refresh page
        st.session_state.pop('key')
        st.experimental_rerun()
