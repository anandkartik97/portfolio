from pathlib import Path

import streamlit
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
resume_file = current_dir / "CV.pdf"
profile_pic = current_dir / "profile_pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Kartik Anand"
PAGE_ICON = ":wave:"
NAME = "Kartik Anand"
DESCRIPTION = """
Collaborative professional with ~4 years of experience in the financial services industry. 
Excellent problem-solving skills that help drive results in an extremely fast-paced environment.
Background in software development and analytics. Strategic and decisive thinker with strong communication skills and interpersonal abilities.
"""
EMAIL = "anandkartik97@gmail.com"
SOCIAL_MEDIA = {
    "📍 Singapore": "",
    "💬 LinkedIn": "https://www.linkedin.com/in/kartik-anand-44323312a/",
    "📞 +65-97850414": "",
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
    st.image(profile_pic, width=300)
    st.write('\n')
    st.write('Data Analytics | Quant Trading | FinTech')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA), gap='large')
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- ⚡Python  ⚡Java  ⚡SQL  ⚡Airflow ⚡Plotly ⚡Tableau ⚡PowerBI ⚡MS Excel
- ⚡Postgres  ⚡PySpark  ⚡Amazon Athena  ⚡AWS SageMaker ⚡Hue ⚡Magellan ⚡ Jenkins
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("💼", "**Data Analytics Associate | NatWest Group**")
st.write("11/2021 - 10/2022")
st.write(
    """
- ► Developed spreadsheet analyzer tool that retrieves cellular information from EUDAs and uses visualizations to highlight the areas subject to higher risks
- ► Text analytics on historic audit reports for readability, sentiment & wordcloud analysis aiding audit team validate the adherence of audit report ratings
- ► Extracted and identified articles requiring IA coverage from regulatory websites using Python. Built a Flask app with dynamic visuals allowing senior management to view and modify the underlying data
- ► Developed a negative news bot to fetch news articles and perform sentiment analysis to classify negative articles
"""
)

# --- JOB 2
st.write('\n')
st.write("💼", "**Technlogy Analyst - C10 | Citi**")
st.write("08/2020 - 11/2021")
st.write(
    """
- ► Automated the outbound flow for SFTR Regulatory Reporting by using Apache Camel routing framework to generate and transfer the outbound files
- ► Streamlined and optimized the ETL pipeline catering to a huge volume of data (50+ GB daily) and stored it in 3 different data stores: Mongo, Elastic and Impala saving 2+ hours of efforts daily
- ► Created Tableau dashboard to increase the acceptance rates (ack-nack ratio) by 10% and performed time series analysis of ACKs/NACKs/Exceptions
"""
)

# --- JOB 3
st.write('\n')
st.write("💼", "**Technlogy Analyst - C09 | Citi**")
st.write("08/2019 - 07/2020")
st.write(
    """
- ► As a part of Client Connectivity Team, Developed microservices using Java for OneConnect which is a low latency global order routing platform
- ► Designed and implemented Risk & Compliance Checks and enhanced the Filter Module for OneView
"""
)

# --- JOB 4
st.write('\n')
st.write("💼", "**Data Science Intern | Royal Bank of Scotland**")
st.write("05/2018 - 07/2018")
st.write(
    """
- ► Conceptualized and delivered 2 self-service automated tools written in Python reducing the data validation TAT by 80%
"""
)

# --- Achievements & Awards ---
st.write('\n')
st.subheader("Achievements & Awards")
st.write("---")
st.markdown("🏆 Citi Gratitude Platinum Award ; Citi Gratitude Gold Award ; Citi Gratitude Copper Award")
st.markdown("Recognized with exemplary performance awards for reaching the extra mile to deliver in all endeavors by "
            "Senior Management")
st.markdown("🏆 HackBangalore'18")
st.markdown("Awarded for the best pitch and idea by Mercedes Benz R&D Germany")
st.markdown("🏆 Versatile Student Award")
st.markdown("Award for Academic Excellence (School Topper) and all-round performance in 2015")
st.markdown("🏆 CBSE Certificate of Merit")
st.markdown("Awarded for being in top 0.1% of successful candidates in Physics")

# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
st.markdown("✔️ Fraud Analytics")
st.markdown("Compared various Supervised Machine Learning techniques like Logistic Regression, Decision Trees, "
            "Naive Bayes, Support Vector Machine to detect fraud in publicly available credit card data set")
st.markdown('Published research paper in Springer Nature Singapore')
st.write('https://link.springer.com/chapter/10.1007/978-981-15-5616-6_8')
st.markdown("✔️ Real Time Face Recognition")
st.markdown("Generated training data set of images to build a classifier to recognize faces. Extracted faces from "
            "live video using HaarCascades Classifier, followed by face recognition using KNN algorithm")

# --- Certifications ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.markdown("🎯 Practical Data Science with Amazon SageMaker - AWS")
st.markdown("🎯 The Complete Introduction to Data Analytics with Tableau - Udemy")
st.markdown("🎯 Alteryx Designer Core Certification - Alteryx.com")

# --- Positions of Responsibility ---
st.write('\n')
st.subheader("Positions of Responsibility")
st.write("---")
st.markdown("🤝 CSR - Social Contributor")
st.markdown('Successfully led a team of 20+ volunteers to organise Sport Day event for 150+ primary school students '
            'in association with New Vision NGO')
st.markdown("🤝 Tech Head - Annual Literary Fest, DTU")
st.markdown('Successfully led a team of 20+ people and created a visually appealing web portal responsible for '
            'registration of 1200+ participants')