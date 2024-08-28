import streamlit as st
import google.generativeai as genai
import os

# Apikeygan waa midka developmentiga : kumeel gaar 
genai.configure(api_key="AIzaSyBnABiGT35_ox16U6ryctXsdQYnlIXjQkM")


model = genai.GenerativeModel('gemini-1.5-flash')

# funtionkan wuxuu qaadanaya optionskii lasoo dortay kadib wuxuu udirayaa api -ga gemini si loo analyze gareeyo
def analyze_interests(selected_options):
    # promptiga loo dirayo gemini
    prompt = f"Based on these interests: {', '.join(selected_options)}, which field of study should a high school student choose?"
    
    # jawaabta gemini
    response = model.generate_content(prompt)
    
    # kadib soo celinaa qoraalka uu anlyze gareeyey
    return response.text


st.title("High School Field of Study Recommendation")
st.write("Please select your interests from the options below:")

# optionska ladooran lahaa
options = [
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", 
    "History", "Geography", "Literature", "Art","Hadith" ,"Tafsiir","Quran",
    "Economics", "Business Studies", "Psychology", "Philosophy", 
    "Political Science", "Sociology", "Environmental Science", 
    "Physical Education", "Engineering", "Languages" ,"Islamic study", "Arabic"
]


selected_options = st.multiselect("Select your interests:", options)


if st.button("Analyze and Recommend"):
    if selected_options:
        analysis_result = analyze_interests(selected_options)
        
        if analysis_result:
            st.success(f"We recommend you to explore the faculty of {analysis_result}.")
        else:
            st.error("Failed to analyze your interests. Please try again.")
    else:
        st.warning("Please select at least one interest.")