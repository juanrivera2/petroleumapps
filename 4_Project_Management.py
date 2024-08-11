import streamlit as st
import streamlit.components.v1 as components



#BUSINESS CASE: 
# Ref 1: https://www.constructiondive.com/news/construction-wastes-billions-labor-lean-planning/696421/

st.title("Construction lost as much as $40B on poor productivity in 2022")
st.header("Nearly half of respondents (45%) said they saw declining labor productivity on their jobsites in the last 12 to 18 months")
st.image('project management.jpeg', caption='https://www.constructiondive.com/news/construction-wastes-billions-labor-lean-planning/696421/')



#MICROSOFT SOLUTION (VideoAnalyzer):


path_to_html = "/Users/juanrivera/Desktop/chatbot1/Streamlit/pages/10_project_management_video.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Show an external HTML")
components.html(html_data,height=2000)









