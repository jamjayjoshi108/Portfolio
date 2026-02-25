import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jay J. | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR SWAG & COLOR ---
st.markdown("""
<style>
    /* Gradient text for the main name */
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #00C6FF, #0072FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 0;
        padding-bottom: 0;
    }
    /* Stylish subtitle */
    .subtitle {
        font-size: 1.2rem;
        color: #888;
        font-weight: 600;
        margin-top: -10px;
        margin-bottom: 15px;
    }
    /* Metric Card Styling */
    div[data-testid="metric-container"] {
        background-color: rgba(0, 114, 255, 0.05);
        border: 1px solid rgba(0, 114, 255, 0.2);
        padding: 5% 5% 5% 10%;
        border-radius: 10px;
        border-left: 5px solid #0072FF;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
    }
    /* Phone number pill */
    .phone-pill {
        display: inline-block;
        background-color: #f0f2f6;
        color: #0072FF;
        padding: 8px 18px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1.1rem;
        border: 1px solid #0072FF;
        margin-top: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2.5], gap="large")

with col1:
    try:
        st.image("profile_pic.png", use_container_width=True)
    except FileNotFoundError:
        st.info("📷 Add 'profile_pic.png' to the repository for maximum impact.")

with col2:
    st.markdown('<p class="gradient-text">JAY J.</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Cloud Architect & Tech-Governance Strategist</p>', unsafe_allow_html=True)
    st.markdown("**📍 Chandigarh, India**")
    
    # Updated contact method as requested
    st.markdown('<div class="phone-pill">📞 +91 79847 51175</div>', unsafe_allow_html=True)
    
    st.write("""
    I build enterprise-grade data pipelines, orchestrate high-availability cloud infrastructure, 
    and drive state-level operational efficiency. From optimizing IoT telemetry to 
    spearheading data governance for public administration, my focus is always on massive, 
    measurable impact at scale.
    """)

st.write("---")

# --- DYNAMIC METRICS DASHBOARD ---
st.subheader("⚡ Impact by the Numbers")
m1, m2, m3, m4 = st.columns(4)

# Using deltas to give it a live, dashboard feel
m1.metric(label="System Uptime Managed", value="99.99%", delta="Zero Downtime", delta_color="normal")
m2.metric(label="Infra Cost Reductions", value="50%", delta="-50% Serverless Ops", delta_color="inverse")
m3.metric(label="Microservice Acceleration", value="40%", delta="Faster Deployments", delta_color="normal")
m4.metric(label="Global Tech Stints", value="4", delta="Tesla, AWS, J&J, Gov", delta_color="off")

st.write("---")

# --- INTERACTIVE TABS ---
# Tabs make the app feel dynamic and prevent scrolling fatigue
tab1, tab2, tab3 = st.tabs(["🏛️ High-Impact Experience", "🛠️ Technical Arsenal", "🎓 Education & Research"])

with tab1:
    st.markdown("### 🏆 Career Milestones")
    
    st.success("**Sr. Punjab Good Governance Fellow | Government of Punjab (Current)** \n*Spearheading data governance and infrastructure optimization to revolutionize public administration and state-level service delivery.*")
    
    st.info("**Data Engineering Manager | Enstructure (Deployed at Johnson & Johnson)** \n*Led full-scale cloud migrations and slashed microservice deployment times by 40% using Docker/Kubernetes.*")
    
    st.warning("**Cloud Support Engineer | Amazon Web Services (AWS)** \n*Architected serverless data solutions, cutting enterprise infrastructure costs by 50% while maintaining 99.99% REST API uptime.*")
    
    st.error("**Data Engineer & Analytics | Tesla Inc.** \n*Engineered Python-based IoT telemetry pipelines for Model 3 sensor data, boosting predictive maintenance accuracy by 15%.*")

with tab2:
    st.markdown("### ⚡ Core Competencies")
    col_a, col_b = st.columns(2, gap="large")
    
    with col_a:
        st.markdown("**Cloud & Infrastructure (Azure/AWS)**")
        st.progress(95, text="Advanced Architecture")
        
        st.markdown("**Data Engineering (Databricks/Spark/Kafka)**")
        st.progress(90, text="Advanced Pipelines")
        
    with col_b:
        st.markdown("**DevOps & Containerization (K8s/Docker)**")
        st.progress(90, text="Advanced Orchestration")
        
        st.markdown("**Governance & Security (PIM/RBAC)**")
        st.progress(85, text="Highly Proficient")

with tab3:
    st.markdown("### 🎓 Academic Excellence")
    
    st.markdown("""
    * 🇨🇦 **Post-Graduate Diploma, Business Analytics** | Seneca College (GPA: **3.95**)
    * 🇺🇸 **M.S., Information Systems** | Cal State LA (GPA: **3.94**)
    * 🇮🇳 **B.E., Computer Engineering** | Kadi Sarva Vishwavidyalaya (GPA: **3.77**)
    """)
    
    st.markdown("### 📄 Select Publications")
    st.markdown("""
    1. *The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra* (IEEE ICCICN)
    2. *Customer Reading Rate for NYT* (WiDS)
    3. *Lung Cancer Nodule Detection using CNN* (Cal State LA Symposium)
    """)

st.write("---")
st.markdown("<center>Engineered with Precision | © 2026 Jay J.</center>", unsafe_allow_html=True)
