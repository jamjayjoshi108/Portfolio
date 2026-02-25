import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Jay J. | Tech & Governance",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED CSS INJECTION ---
st.markdown("""
<style>
    /* Hide standard Streamlit header and footer for a pure website feel */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 1rem; max-width: 1200px;}

    /* Animations */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }
    @keyframes fadein {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Hero Section Styling */
    .hero-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 2rem;
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
        animation: fadein 1s ease-out;
    }
    .hero-text { flex: 2; padding-right: 2rem; }
    .hero-name {
        font-size: 4rem;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #1e3c72, #2a5298, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.1;
    }
    .hero-subtitle { font-size: 1.5rem; color: #555; font-weight: 600; margin-top: 10px; }
    .contact-badge {
        display: inline-block;
        background: #1e3c72;
        color: white;
        padding: 10px 25px;
        border-radius: 50px;
        font-weight: bold;
        font-size: 1.1rem;
        box-shadow: 0 5px 15px rgba(30, 60, 114, 0.4);
        margin-top: 15px;
        transition: transform 0.3s;
    }
    .contact-badge:hover { transform: scale(1.05); }

    /* Floating Profile Pic */
    .hero-img-container {
        flex: 1;
        display: flex;
        justify-content: center;
        animation: float 6s ease-in-out infinite;
    }
    .hero-img {
        width: 250px;
        height: 250px;
        border-radius: 50%;
        object-fit: cover;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        border: 5px solid white;
    }

    /* Swag Cards for Experience */
    .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
    .exp-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-top: 4px solid transparent;
        transition: all 0.3s ease;
        animation: fadein 1.5s ease-out;
        position: relative;
        overflow: hidden;
    }
    .exp-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    
    /* Specific Brand Card Borders on Hover */
    .card-gov:hover { border-top: 4px solid #FF9933; }
    .card-aws:hover { border-top: 4px solid #FF9900; }
    .card-tesla:hover { border-top: 4px solid #E31937; }
    .card-jj:hover { border-top: 4px solid #D51900; }

    .brand-logo { height: 40px; margin-bottom: 15px; display: block; }
    .exp-title { font-size: 1.2rem; font-weight: 800; color: #222; margin-bottom: 5px; }
    .exp-desc { color: #666; font-size: 0.95rem; line-height: 1.5; }

    /* Tech Stack Pills */
    .tech-container { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 2rem; animation: fadein 2s ease-out; }
    .tech-pill {
        background: white;
        border: 1px solid #ddd;
        padding: 8px 18px;
        border-radius: 20px;
        font-weight: 600;
        color: #333;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: all 0.2s;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .tech-pill:hover { background: #1e3c72; color: white; border-color: #1e3c72; transform: scale(1.05); }

    /* Section Headers */
    .section-title {
        font-size: 2rem; font-weight: 800; color: #111; margin-top: 3rem; margin-bottom: 1rem;
        border-bottom: 3px solid #00C6FF; display: inline-block; padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (HTML INJECTED) ---
# Note: Ensure 'profile_pic.png' is in your repo. The HTML will try to render it. 
# If it fails, it will show a clean fallback circle.
st.markdown("""
<div class="hero-container">
    <div class="hero-text">
        <h1 class="hero-name">JAY J.</h1>
        <div class="hero-subtitle">Cloud Architect & Tech-Governance Strategist</div>
        <p style="color: #666; font-size: 1.1rem; margin-top: 15px; max-width: 600px;">
            I build enterprise-grade data pipelines, orchestrate high-availability cloud infrastructure, 
            and drive state-level operational efficiency. Specializing in highly scalable systems and data-backed public administration.
        </p>
        <div class="contact-badge">📞 +91 79847 51175</div>
    </div>
    <div class="hero-img-container">
        <img src="https://raw.githubusercontent.com/jamjayjoshi108/Portfolio/main/profile_pic.png" alt="Jay J." class="hero-img" onerror="this.src='https://ui-avatars.com/api/?name=Jay+J&background=1e3c72&color=fff&size=250'">
    </div>
</div>
""", unsafe_allow_html=True)


# --- HIGH-IMPACT EXPERIENCE (DYNAMIC CARDS WITH LOGOS) ---
st.markdown('<div class="section-title">High-Impact Experience</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card-grid">
    <div class="exp-card card-gov">
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg" class="brand-logo" alt="Gov">
        <div class="exp-title">Sr. Good Governance Fellow</div>
        <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Government of Punjab | Current</div>
        <div class="exp-desc">Spearheading data governance, infrastructure optimization, and AI implementation to revolutionize public administration and service delivery at a state-wide level.</div>
    </div>
    
    <div class="exp-card card-aws">
        <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" class="brand-logo" alt="AWS">
        <div class="exp-title">Cloud Support Engineer</div>
        <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Amazon Web Services (AWS)</div>
        <div class="exp-desc">Architected serverless data processing solutions using Lambda & EMR. Cut enterprise infrastructure costs by 50% while maintaining 99.99% REST API uptime.</div>
    </div>
    
    <div class="exp-card card-tesla">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg" class="brand-logo" alt="Tesla">
        <div class="exp-title">Data Engineer & Analytics</div>
        <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Tesla Inc.</div>
        <div class="exp-desc">Engineered robust Python-based IoT telemetry pipelines for Model 3 sensor data via Kafka, boosting predictive maintenance accuracy by 15%.</div>
    </div>
    
    <div class="exp-card card-jj">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b5/Johnson_and_Johnson_Logo.svg" class="brand-logo" style="height: 25px; margin-bottom: 25px;" alt="J&J">
        <div class="exp-title">Data Engineering Manager</div>
        <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Enstructure (Deployed at J&J)</div>
        <div class="exp-desc">Led cross-functional enterprise cloud migrations. Slashed microservice deployment times by 40% utilizing Docker and Kubernetes orchestration.</div>
    </div>
</div>
""", unsafe_allow_html=True)


# --- TECHNICAL ARSENAL (HOVER PILLS) ---
st.markdown('<div class="section-title">Technical Arsenal</div>', unsafe_allow_html=True)

st.markdown("""
<div class="tech-container">
    <div class="tech-pill">☁️ Microsoft Azure</div>
    <div class="tech-pill">🟧 AWS Platform</div>
    <div class="tech-pill">🧱 Databricks & Spark</div>
    <div class="tech-pill">☸️ Kubernetes & Docker</div>
    <div class="tech-pill">🐍 Python & Scala</div>
    <div class="tech-pill">📡 Kafka & IoT Telemetry</div>
    <div class="tech-pill">🔐 Privileged Identity Mgmt (PIM)</div>
    <div class="tech-pill">⚙️ CI/CD & Terraform</div>
</div>
""", unsafe_allow_html=True)


# --- EDUCATION ---
st.markdown('<div class="section-title">Academic Pedigree</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 4px solid #1e3c72;">
        <h4 style="margin:0; color: #222;">Post-Graduate Diploma, Business Analytics</h4>
        <p style="margin:0; color: #666;">Seneca College, Canada • <b>GPA: 3.95</b></p>
        <hr style="margin: 10px 0; border: 0.5px solid #eee;">
        <h4 style="margin:0; color: #222;">M.S., Information Systems</h4>
        <p style="margin:0; color: #666;">Cal State LA, USA • <b>GPA: 3.94</b></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border-left: 4px solid #00C6FF;">
        <h4 style="margin: 0; margin-bottom: 10px; color: #222;">Select Publications</h4>
        <p style="margin: 3px 0; color: #555; font-size: 0.9rem;">📄 <i>The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra</i> (IEEE ICCICN)</p>
        <p style="margin: 3px 0; color: #555; font-size: 0.9rem;">📄 <i>Customer Reading Rate for NYT</i> (WiDS)</p>
        <p style="margin: 3px 0; color: #555; font-size: 0.9rem;">📄 <i>Lung Cancer Nodule Detection using CNN</i> (Cal State LA Symposium)</p>
    </div>
    """, unsafe_allow_html=True)

st.write("<br><br><br>", unsafe_allow_html=True)


#=================================================================================
# import streamlit as st

# # --- PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="Jay J. | Portfolio",
#     page_icon="⚡",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # --- CUSTOM CSS FOR SWAG & COLOR ---
# st.markdown("""
# <style>
#     /* Gradient text for the main name */
#     .gradient-text {
#         background: -webkit-linear-gradient(45deg, #00C6FF, #0072FF);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-size: 3.5rem;
#         font-weight: 900;
#         margin-bottom: 0;
#         padding-bottom: 0;
#     }
#     /* Stylish subtitle */
#     .subtitle {
#         font-size: 1.2rem;
#         color: #888;
#         font-weight: 600;
#         margin-top: -10px;
#         margin-bottom: 15px;
#     }
#     /* Metric Card Styling */
#     div[data-testid="metric-container"] {
#         background-color: rgba(0, 114, 255, 0.05);
#         border: 1px solid rgba(0, 114, 255, 0.2);
#         padding: 5% 5% 5% 10%;
#         border-radius: 10px;
#         border-left: 5px solid #0072FF;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.05);
#         transition: transform 0.2s ease;
#     }
#     div[data-testid="metric-container"]:hover {
#         transform: translateY(-5px);
#     }
#     /* Phone number pill */
#     .phone-pill {
#         display: inline-block;
#         background-color: #f0f2f6;
#         color: #0072FF;
#         padding: 8px 18px;
#         border-radius: 30px;
#         font-weight: 700;
#         font-size: 1.1rem;
#         border: 1px solid #0072FF;
#         margin-top: 10px;
#         margin-bottom: 20px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- HERO SECTION ---
# col1, col2 = st.columns([1, 2.5], gap="large")

# with col1:
#     try:
#         st.image("profile_pic.png", use_container_width=True)
#     except FileNotFoundError:
#         st.info("📷 Add 'profile_pic.png' to the repository for maximum impact.")

# with col2:
#     st.markdown('<p class="gradient-text">JAY J.</p>', unsafe_allow_html=True)
#     st.markdown('<p class="subtitle">Cloud Architect & Tech-Governance Strategist</p>', unsafe_allow_html=True)
#     st.markdown("**📍 Chandigarh, India**")
    
#     # Updated contact method as requested
#     st.markdown('<div class="phone-pill">📞 +91 79847 51175</div>', unsafe_allow_html=True)
    
#     st.write("""
#     I build enterprise-grade data pipelines, orchestrate high-availability cloud infrastructure, 
#     and drive state-level operational efficiency. From optimizing IoT telemetry to 
#     spearheading data governance for public administration, my focus is always on massive, 
#     measurable impact at scale.
#     """)

# st.write("---")

# # --- DYNAMIC METRICS DASHBOARD ---
# st.subheader("⚡ Impact by the Numbers")
# m1, m2, m3, m4 = st.columns(4)

# # Using deltas to give it a live, dashboard feel
# m1.metric(label="System Uptime Managed", value="99.99%", delta="Zero Downtime", delta_color="normal")
# m2.metric(label="Infra Cost Reductions", value="50%", delta="-50% Serverless Ops", delta_color="inverse")
# m3.metric(label="Microservice Acceleration", value="40%", delta="Faster Deployments", delta_color="normal")
# m4.metric(label="Global Tech Stints", value="4", delta="Tesla, AWS, J&J, Gov", delta_color="off")

# st.write("---")

# # --- INTERACTIVE TABS ---
# # Tabs make the app feel dynamic and prevent scrolling fatigue
# tab1, tab2, tab3 = st.tabs(["🏛️ High-Impact Experience", "🛠️ Technical Arsenal", "🎓 Education & Research"])

# with tab1:
#     st.markdown("### 🏆 Career Milestones")
    
#     st.success("**Sr. Punjab Good Governance Fellow | Government of Punjab (Current)** \n*Spearheading data governance and infrastructure optimization to revolutionize public administration and state-level service delivery.*")
    
#     st.info("**Data Engineering Manager | Enstructure (Deployed at Johnson & Johnson)** \n*Led full-scale cloud migrations and slashed microservice deployment times by 40% using Docker/Kubernetes.*")
    
#     st.warning("**Cloud Support Engineer | Amazon Web Services (AWS)** \n*Architected serverless data solutions, cutting enterprise infrastructure costs by 50% while maintaining 99.99% REST API uptime.*")
    
#     st.error("**Data Engineer & Analytics | Tesla Inc.** \n*Engineered Python-based IoT telemetry pipelines for Model 3 sensor data, boosting predictive maintenance accuracy by 15%.*")

# with tab2:
#     st.markdown("### ⚡ Core Competencies")
#     col_a, col_b = st.columns(2, gap="large")
    
#     with col_a:
#         st.markdown("**Cloud & Infrastructure (Azure/AWS)**")
#         st.progress(95, text="Advanced Architecture")
        
#         st.markdown("**Data Engineering (Databricks/Spark/Kafka)**")
#         st.progress(90, text="Advanced Pipelines")
        
#     with col_b:
#         st.markdown("**DevOps & Containerization (K8s/Docker)**")
#         st.progress(90, text="Advanced Orchestration")
        
#         st.markdown("**Governance & Security (PIM/RBAC)**")
#         st.progress(85, text="Highly Proficient")

# with tab3:
#     st.markdown("### 🎓 Academic Excellence")
    
#     st.markdown("""
#     * 🇨🇦 **Post-Graduate Diploma, Business Analytics** | Seneca College (GPA: **3.95**)
#     * 🇺🇸 **M.S., Information Systems** | Cal State LA (GPA: **3.94**)
#     * 🇮🇳 **B.E., Computer Engineering** | Kadi Sarva Vishwavidyalaya (GPA: **3.77**)
#     """)
    
#     st.markdown("### 📄 Select Publications")
#     st.markdown("""
#     1. *The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra* (IEEE ICCICN)
#     2. *Customer Reading Rate for NYT* (WiDS)
#     3. *Lung Cancer Nodule Detection using CNN* (Cal State LA Symposium)
#     """)

# st.write("---")
# st.markdown("<center>Engineered with Precision | © 2026 Jay J.</center>", unsafe_allow_html=True)
