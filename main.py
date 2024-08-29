import streamlit as st
import google.generativeai as genai

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


image_html = """
    <style>
        .rounded-image {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
    </style>
    <img src="https://scontent.fmgq1-2.fna.fbcdn.net/v/t39.30808-6/449754289_441560052013054_8584737888116144419_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=6ee11a&_nc_ohc=mzu3IowziXsQ7kNvgH5jmf4&_nc_ht=scontent.fmgq1-2.fna&oh=00_AYDbAybpreyZGeYQFZhbyKO37cfb8UnFc8_Qc9FBN13FSQ&oe=66D53E02" class="rounded-image">
"""

st.markdown(image_html, unsafe_allow_html=True)
st.write("PyCon Event programm submit 2024")

st.title("PyCon Academic Advisor AI")

st.write("")
st.write("Please select your interests from the options below:")

# optionska ladooran lahaa
options = [
    "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science", 
    "History", "Geography", "Literature", "Art","Journalism", 
    "Islamic Study","Hadith","Tafsiir","Somali",
    "Economics", "Business Studies", "Psychology", "Philosophy", 
    "Political Science", "Sociology", "Environmental Science", 
    "Physical Education", "Engineering", "Languages","Arabic","English" ,
]

st.markdown("""
    <style>
    /* Style the input box */
    div[data-baseweb="select"] > div {
        border: 2px solid skyblue !important;
        border-radius: 5px !important;
        /*background-color: #2d2d2d !important; */ /* Dark background for dark theme */
    }
    
    /* Style the selected options (within the input box) */
    div[data-baseweb="tag"] {
        background-color: skyblue !important;
        color: white !important;
    }
    
    /* Style the options in the dropdown */
    div[role="listbox"] > div {
        background-color: lightblue !important;
        color: black !important;
    }
    
    /* Style the selected options in the dropdown */
    div[role="listbox"] > div[aria-selected="true"] {
        background-color: skyblue !important;
        color: white !important;
    }
    span[data-baseweb="tag"] {
  background-color: blue !important;
    </style>
""", unsafe_allow_html=True)


selected_options = st.multiselect("Select your interests:", options)




st.markdown("""
    <style>
    .stButton > button {
        color: skyblue !important;
        border: 2px solid skyblue !important;
        background-color: transparent !important;
        border-radius: 5px !important;
    }

    /* Optional: Change button hover effect */
    .stButton > button:hover {
    }
    </style>
""", unsafe_allow_html=True)




if st.button("Analyze and Recommend"):
    if selected_options:
        analysis_result = analyze_interests(selected_options)
        
        if analysis_result:
            st.success(f"We recommend you to explore the faculty of {analysis_result}.")
        else:
            st.error("Failed to analyze your interests. Please try again.")
    else:
        st.warning("Please select at least one interest.")