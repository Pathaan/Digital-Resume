from pathlib import Path
import streamlit as st
from PIL import Image
# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-picture.png"
# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Md Shahrukh"
PAGE_ICON = ":wave:"
NAME = "Md Shahrukh"
DESCRIPTION = """
Transforming from fixing machines to decoding data: Harnessing my engineering mindset to unlock the secrets within the numbers.
"""
EMAIL = "mdshahrukhbme@email.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/md-shahrukh-locky/",
    "GitHub": "https://github.com/Pathaan",
    "Kaggle": "https://www.kaggle.com/mdshahrukh",
}
PROJECTS = {
    "⚛ Regression - House Price Prediction": "https://github.com/Pathaan/House-Price-Prediction",
    "⚛ Classification - Celebrity Image Classification": "https://github.com/Pathaan/Celebrity-Image-Classification",
    "⚛ Power BI - Revenue Insights in Hospitality Doamin": "https://github.com/Pathaan/Revenue-Insights-In-Hospitality-Domain",
    "⚛ Movie Recommendation System": "https://github.com/Pathaan/Movie-Recommendation-System",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


    
# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# --- EXPERIENCE ---
st.write('\n')
st.subheader("Experience")
st.write(
    
    """
- 💡 Strong hands on experience and knowledge in Python and Excel
- 💡 Good understanding of statistical principles and their respective applications
- 💡 4 Years expereince in Healthcare Sector as an Engineer
"""
)


# --- QUALIFICATIONS ---
st.write('\n')
st.subheader("Qualifications")
st.write(
    
    """
- 👩🏻‍🎓 Postgraduate Diploma in Applied Statistics with Data Analytics and Official Statistics from Indian Statistical Institute, Kolkata
- 🎓 Bachelor's of Science in Mathematics from Silli College Silli, Ranchi University
- 👩🏻 Diploma in Engineering in Medical Laboratory Technology from Sheikhpara Abdur Rahaman Memorial Polytechnic
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Matplotlib), SQL, R Language
- 📊 Data Visulization: PowerBi, MS Excel
- 📚 Machine Learning Skills: Regression, Classification
- 🗄️ Databases: MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "Forecasting Project under Prof. Raju Maiti | Indian Statistical Institute, Kolkata")
st.write("12/2023 - Present")
st.write(
    """
- ► Project: NAVIGATING INFLATION’S IMPACT ON THE MIDDLE CLASS
- ► Focus: Middle-class families (income: 30k to 45k)
- ► Primary objectives:
  - ► Develop effective money-saving strategies
  - ► Identify optimal investment sectors
  - ► Recommend essential health insurance coverage
  - ► Project potential rent fluctuations after five years
  - ► Forecast expected interest rates offered by banks
- ► Methodology:
  - ► Utilize various datasets
  - ► Employ statistical analysis
  - ► Use time series analysis
- ► Ultimate goal: Empower middle-class earners with strategies for resilience against inflationary pressures.
"""
)

# --- JOB 2
st.write("🚧", "Regression Project under Prof. Debasis Sengupta | Indian Statistical Institute, Kolkata")
st.write("11/2023 - Present")
st.write(
    """
- ► Project: ANALYZING THE GROUNDWATER CRISIS IN WEST BENGAL, INDIA
- ► Focus: Predicting impact of upcoming monsoon season on groundwater levels
- ► Data: Over 10 years of data available
- ► Methodology:
  - ► Utilize comprehensive data analysis techniques
  - ► Include machine learning and statistical analysis 
- ► Ultimate goal: Provide valuable insights for understanding and addressing the groundwater crisis in West Bengal
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")