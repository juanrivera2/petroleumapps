#Framework supporting MLOps Apps
#%%
import streamlit as st 
from PIL import Image, ImageEnhance
from streamlit_extras.app_logo import add_logo

# add kitten logo

#Large Language Model Library
from langchain_community.llms import OpenAI
import docx
import datetime
import time
import base64


#Front-End
with st.sidebar:
    page_icon="OptiLaborAI.png",
    layout="wide"
    add_logo("OptiLaborAI.png")
    st.markdown("<h1 style='text-align:center;font-family:Georgia'>💸 OptiLabor AI </h1>",unsafe_allow_html=True)
    st.markdown("This is your AI assistant and your best friend from now in your cconstruction project. \n\
                It provides you valuable information about your project in matter of seconds,  \n\
                helps you to collaborate with your team in real time (no more expensive and lengthy ROFs!) and accurately predicts the resources and labor you need."
                )
    st.markdown("<h2 style='text-align:center;font-family:Georgia'>Features</h1>",unsafe_allow_html=True)
    st.markdown(" - OL Takeoff - Submit your blue print, OL AI will do the rest and give you the accurate BOQ (Bill of Quantities")
    st.markdown(" - OL Doc Wizard - No more headaches with invoices, receipts, contracts, agreements or searching info on documents. OLBot comes to the rescue to find all you need in seconds. Also, create your reports")   
    st.markdown(" - OL Virtual Design - 3D models enable teams to identify clashes, interferences, or design flaws early in the process, reducing costly changes during construction.")
    st.markdown(" - OL Project Management - The integration of Internet of Things (IoT) and Artificial Intelligence (AI) offers several significant benefits for project management. Collecting vast amounts of real-time data from construction sites, AI algorithms can analyze this data to provide insights into various aspects of the project, including progress tracking, equipment usage, material inventory, and environmental conditions.")
    st.markdown(" - OL Decision Making - OL Decision Making helps stakeholders visualize key performance indicators (KPIs), project progress, resource allocation, budget status, and other critical metrics in real-time. It also simplifies compliance monitoring and reporting in the construction industry creating automated reports from the represented data.")   

    st.markdown("-------")
    
    


# App framework
#TO ADD THE VIDEO:

video_file = open('Untitled video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

st.image('OptiLabor.png', caption='OptiLabor Features')




# %%
