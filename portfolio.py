import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jay J. | Portfolio",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
<style>
    /* Clean up the top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    /* Style for profile section */
    .profile-subtitle {
        color: #555555;
        font-size: 1.2rem;
        font-weight: 500;
        margin-bottom: 0px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    # Placeholder for your professional headshot. 
    # Replace "profile_pic.png" with your actual image file path in the same folder.
    try:
        st.image("profile_pic.png", use_container_width=True)
    except FileNotFoundError:
        st.info("📷 Put your 'profile_pic.png' in the same folder as this script to display your photo here.")

with col2:
    st.title("Jay J.")
    st.markdown("<p class='profile-subtitle'>Sr. Punjab Good Governance Fellow | Cloud & Data Architecture Expert</p>", unsafe_allow_html=True)
    st.caption("📍 Chandigarh, India")
    
    # Social/Professional Links
    link_col1, link_col2, link_col3 = st.columns([1, 1, 2])
    with link_col1:
        st.markdown("[🔗 **LinkedIn**](https://linkedin.com/in/your-profile)")
    with link_col2:
        st.markdown("[💻 **GitHub**](https://github.com/jamjayjoshi108)")
    with link_col3:
        st.markdown("[✉️ **Contact Me**](mailto:jamjayjoshi108@gmail.com)")

st.divider()

# --- ABOUT ME SECTION ---
st.header("💡 About Me")
st.write("""
I am a technologist and data architect with over 6 years of experience bridging the gap between scalable cloud infrastructure, AI, and public impact. My career has spanned building high-frequency telemetry pipelines for global tech leaders to managing enterprise-scale cloud migrations. 

Currently, I am passionate about leveraging data engineering, cloud operations, and AI to optimize public administration, enhance governance infrastructure, and drive data-backed decision-making at scale.
""")

st.divider()

# --- HIGHLIGHT METRICS ---
# This gives a "dashboard" feel to your resume, which looks great for a Data Engineer
st.header("📊 Career Highlights")
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Years of Experience", value="6+")
m2.metric(label="Cloud Platforms", value="Azure & AWS")
m3.metric(label="Uptime Managed", value="99.99%")
m4.metric(label="Publications", value="4")

st.divider()

# --- PROFESSIONAL EXPERIENCE ---
st.header("🏛️ Professional Journey")

# 1. Government Role (Current)
with st.expander("🌟 Sr. Punjab Good Governance Fellow | Government of Punjab (Current)", expanded=True):
    st.write("Applying advanced analytics, infrastructure optimization, and data governance strategies to improve public service delivery and state-level operational efficiency.")

# 2. N-iX
with st.expander("☁️ Data / AI-ML Engineer | N-iX (Feb 2025 - Present)"):
    st.markdown("""
    * **Infrastructure & Governance:** Established robust governance controls within Databricks/Azure using Unity Catalog, implementing Table ACLs.
    * **Pipeline Automation:** Designed end-to-end enterprise data ingestion pipelines for production-grade reliability.
    * **AI Agent Workflow:** Built full agent-based AI workflows for data enrichment and autonomous tasks.
    """)

# 3. Enstructure / J&J
with st.expander("🏢 Data Engineering Manager | Enstructure - Deployed at Johnson & Johnson (May 2023 - May 2024)"):
    st.markdown("""
    * **Cloud Migration:** Led a full-scale migration project ensuring seamless transition of data infrastructure.
    * **Containerization:** Deployed containerized microservices (Docker/Kubernetes), cutting deployment time by 40%.
    * **GenAI Integration:** Integrated proprietary GenAI models into real-time analytics pipelines.
    """)

# 4. AWS
with st.expander("🟠 Cloud Support Engineer | Amazon Web Services (Dec 2021 - Jun 2023)"):
    st.markdown("""
    * **Hybrid Cloud Operations:** Migrated a large enterprise platform from on-premises to AWS.
    * **Serverless Solutions:** Built solutions using AWS Lambda & EMR, cutting infrastructure costs by 50%.
    * **Reliability:** Deployed REST APIs with 99.99% uptime for partner system integration.
    """)

# 5. Tesla
with st.expander("🚗 Data Engineer & Analytics | Tesla Inc. (Aug 2020 - Dec 2020)"):
    st.markdown("""
    * **IoT Telemetry:** Built Python pipelines to analyze Model 3 sensor data, improving predictive maintenance by 15%.
    * **Real-Time Streaming:** Used Apache Kafka to stream high-frequency vehicle data for advanced analytics.
    """)

st.divider()

# --- CORE SKILLS ---
st.header("🛠️ Core Competencies")
skill_col1, skill_col2, skill_col3 = st.columns(3)

with skill_col1:
    st.subheader("Cloud & Architecture")
    st.info("Microsoft Azure, AWS, Hybrid Cloud, Microservices")

with skill_col2:
    st.subheader("Data & AI")
    st.success("Databricks, Spark, Kafka, LLM Integration, IoT Telemetry")

with skill_col3:
    st.subheader("DevOps & Security")
    st.warning("Kubernetes, Docker, CI/CD, Azure AD, IaC")

st.divider()

# --- EDUCATION & RESEARCH ---
st.header("🎓 Education & Research")
ed_col1, ed_col2 = st.columns(2)

with ed_col1:
    st.markdown("**Education**")
    st.markdown("- 🇨🇦 **Post-Graduate Diploma, Business Analytics** | Seneca College (GPA: 3.95)")
    st.markdown("- 🇺🇸 **M.S., Information Systems** | Cal State LA (GPA: 3.94)")
    st.markdown("- 🇮🇳 **B.E., Computer Engineering** | Kadi Sarva Vishwavidyalaya (GPA: 3.77)")

with ed_col2:
    st.markdown("**Select Publications**")
    st.markdown("- 📄 The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra (IEEE ICCICN)")
    st.markdown("- 📄 Customer Reading Rate for NYT (WiDS)")
    st.markdown("- 📄 Lung Cancer Nodule Detection using CNN (Cal State LA Symposium)")

# --- FOOTER ---
st.markdown("<br><hr><center>Built with ❤️ using Streamlit | © 2026 Jay J.</center>", unsafe_allow_html=True)
