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

    /* Hero Section Styling (Desktop Default) */
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
    /* Adjusted minmax to 280px to prevent horizontal scrolling on small phones */
    .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
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

    /* Education Box Base Heights */
    .edu-box { min-height: 340px; }

    /* ======================================================= */
    /* 📱 MOBILE RESPONSIVE CSS (Triggers on screens < 768px)  */
    /* ======================================================= */
    @media (max-width: 768px) {
        .hero-container {
            flex-direction: column-reverse; /* Stacks image on top of text */
            text-align: center;
            padding: 1.5rem 1rem;
        }
        .hero-text {
            padding-right: 0;
            margin-top: 1.5rem;
        }
        .hero-name {
            font-size: 2.8rem; /* Scaled down for mobile */
        }
        .hero-subtitle {
            font-size: 1.2rem;
        }
        .hero-img {
            width: 180px; /* Scaled down for mobile */
            height: 180px;
        }
        .section-title {
            font-size: 1.8rem;
        }
        /* Removes forced height so mobile text doesn't overflow */
        .edu-box { 
            min-height: auto; 
            margin-bottom: 1.5rem;
        }
        .tech-pill {
            font-size: 0.9rem;
            padding: 6px 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- HERO SECTION (HTML INJECTED) ---
st.markdown("""
<div class="hero-container">
<div class="hero-text">
<h1 class="hero-name">JAY J.</h1>
<div class="hero-subtitle">Cloud Architect & Tech-Governance Strategist</div>
<p style="color: #666; font-size: 1.1rem; margin-top: 15px; max-width: 600px; margin-left: auto; margin-right: auto;">
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
st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

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
<img src="https://raw.githubusercontent.com/jamjayjoshi108/Portfolio/main/Johnson_and_Johnson_Logo.svg.png" class="brand-logo" style="height: 25px; object-fit: contain; margin-bottom: 25px;" alt="J&J">
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
    <div class="tech-pill">🟦 Microsoft Azure</div>
    <div class="tech-pill">🟧 Amazon Web Services (AWS)</div>
    <div class="tech-pill">🧠 Artificial Intelligence</div>
    <div class="tech-pill">🤖 Machine Learning</div>
    <div class="tech-pill">🧱⚡ Databricks & Spark</div>
    <div class="tech-pill">☸️🐳 Kubernetes & Docker</div>
    <div class="tech-pill">🐍🔴 Python & SQL</div>
    

</div>
""", unsafe_allow_html=True)


# --- EDUCATION ---
st.markdown('<div class="section-title">Education & Qualifications</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="edu-box" style="background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 5px solid #1e3c72; display: flex; flex-direction: column; justify-content: space-between;">
<div>
<h4 style="margin:0; color: #1e3c72; font-weight: 800;">Post-Graduate Diploma, Business Analytics</h4>
<p style="margin:5px 0 0 0; color: #555;">🇨🇦 Seneca College, Canada • <b style="color:#222;">GPA: 3.95</b></p>
</div>
<hr style="border: 0.5px solid #f0f0f0; margin: 15px 0;">
<div>
<h4 style="margin:0; color: #1e3c72; font-weight: 800;">M.S., Information Systems</h4>
<p style="margin:5px 0 0 0; color: #555;">🇺🇸 Cal State LA, USA • <b style="color:#222;">GPA: 3.94</b></p>
</div>
<hr style="border: 0.5px solid #f0f0f0; margin: 15px 0;">
<div>
<h4 style="margin:0; color: #1e3c72; font-weight: 800;">B.E., Computer Engineering</h4>
<p style="margin:5px 0 0 0; color: #555;">🇮🇳 Kadi Sarva Vishwavidyalaya, India • <b style="color:#222;">GPA: 3.77</b></p>
</div>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="edu-box" style="background: linear-gradient(135deg, #ffffff 0%, #f4f7f6 100%); padding: 25px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 5px solid #00C6FF; display: flex; flex-direction: column;">
<h4 style="margin: 0 0 15px 0; color: #00C6FF; font-weight: 800; font-size: 1.3rem;">Select Publications</h4>
<div style="margin-bottom: 12px; padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
<p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra</p>
<p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 IEEE ICCICN</p>
</div>
<div style="margin-bottom: 12px; padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
<p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">Customer Reading Rate for NYT</p>
<p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 WiDS</p>
</div>
<div style="padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
<p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">Lung Cancer Nodule Detection using CNN</p>
<p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 Cal State LA Symposium</p>
</div>
</div>
""", unsafe_allow_html=True)

st.write("<br><br><br>", unsafe_allow_html=True)

#=================================================================================
# V1
#=================================================================================

# import streamlit as st

# # --- PAGE CONFIGURATION ---
# st.set_page_config(
#     page_title="Jay J. | Tech & Governance",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # --- ADVANCED CSS INJECTION ---
# st.markdown("""
# <style>
#     /* Hide standard Streamlit header and footer for a pure website feel */
#     header {visibility: hidden;}
#     footer {visibility: hidden;}
#     .block-container {padding-top: 1rem; padding-bottom: 1rem; max-width: 1200px;}

#     /* Animations */
#     @keyframes float {
#         0% { transform: translateY(0px); }
#         50% { transform: translateY(-15px); }
#         100% { transform: translateY(0px); }
#     }
#     @keyframes fadein {
#         from { opacity: 0; transform: translateY(20px); }
#         to { opacity: 1; transform: translateY(0); }
#     }

#     /* Hero Section Styling */
#     .hero-container {
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         padding: 2rem;
#         background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
#         border-radius: 20px;
#         box-shadow: 0 10px 30px rgba(0,0,0,0.05);
#         margin-bottom: 2rem;
#         animation: fadein 1s ease-out;
#     }
#     .hero-text { flex: 2; padding-right: 2rem; }
#     .hero-name {
#         font-size: 4rem;
#         font-weight: 900;
#         background: -webkit-linear-gradient(45deg, #1e3c72, #2a5298, #00C6FF);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         margin: 0;
#         line-height: 1.1;
#     }
#     .hero-subtitle { font-size: 1.5rem; color: #555; font-weight: 600; margin-top: 10px; }
#     .contact-badge {
#         display: inline-block;
#         background: #1e3c72;
#         color: white;
#         padding: 10px 25px;
#         border-radius: 50px;
#         font-weight: bold;
#         font-size: 1.1rem;
#         box-shadow: 0 5px 15px rgba(30, 60, 114, 0.4);
#         margin-top: 15px;
#         transition: transform 0.3s;
#     }
#     .contact-badge:hover { transform: scale(1.05); }

#     /* Floating Profile Pic */
#     .hero-img-container {
#         flex: 1;
#         display: flex;
#         justify-content: center;
#         animation: float 6s ease-in-out infinite;
#     }
#     .hero-img {
#         width: 250px;
#         height: 250px;
#         border-radius: 50%;
#         object-fit: cover;
#         box-shadow: 0 20px 40px rgba(0,0,0,0.2);
#         border: 5px solid white;
#     }

#     /* Swag Cards for Experience */
#     .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem; }
#     .exp-card {
#         background: white;
#         border-radius: 15px;
#         padding: 1.5rem;
#         box-shadow: 0 10px 20px rgba(0,0,0,0.05);
#         border-top: 4px solid transparent;
#         transition: all 0.3s ease;
#         animation: fadein 1.5s ease-out;
#         position: relative;
#         overflow: hidden;
#     }
#     .exp-card:hover {
#         transform: translateY(-10px);
#         box-shadow: 0 15px 30px rgba(0,0,0,0.1);
#     }
    
#     /* Specific Brand Card Borders on Hover */
#     .card-gov:hover { border-top: 4px solid #FF9933; }
#     .card-aws:hover { border-top: 4px solid #FF9900; }
#     .card-tesla:hover { border-top: 4px solid #E31937; }
#     .card-jj:hover { border-top: 4px solid #D51900; }

#     .brand-logo { height: 40px; margin-bottom: 15px; display: block; }
#     .exp-title { font-size: 1.2rem; font-weight: 800; color: #222; margin-bottom: 5px; }
#     .exp-desc { color: #666; font-size: 0.95rem; line-height: 1.5; }

#     /* Tech Stack Pills */
#     .tech-container { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 2rem; animation: fadein 2s ease-out; }
#     .tech-pill {
#         background: white;
#         border: 1px solid #ddd;
#         padding: 8px 18px;
#         border-radius: 20px;
#         font-weight: 600;
#         color: #333;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.02);
#         transition: all 0.2s;
#         display: flex;
#         align-items: center;
#         gap: 8px;
#     }
#     .tech-pill:hover { background: #1e3c72; color: white; border-color: #1e3c72; transform: scale(1.05); }

#     /* Section Headers */
#     .section-title {
#         font-size: 2rem; font-weight: 800; color: #111; margin-top: 3rem; margin-bottom: 1rem;
#         border-bottom: 3px solid #00C6FF; display: inline-block; padding-bottom: 5px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- HERO SECTION (HTML INJECTED) ---
# # Note: Ensure 'profile_pic.png' is in your repo. The HTML will try to render it. 
# # If it fails, it will show a clean fallback circle.
# st.markdown("""
# <div class="hero-container">
#     <div class="hero-text">
#         <h1 class="hero-name">JAY J.</h1>
#         <div class="hero-subtitle">Cloud Architect & Tech-Governance Strategist</div>
#         <p style="color: #666; font-size: 1.1rem; margin-top: 15px; max-width: 600px;">
#             I build enterprise-grade data pipelines, orchestrate high-availability cloud infrastructure, 
#             and drive state-level operational efficiency. Specializing in highly scalable systems and data-backed public administration.
#         </p>
#         <div class="contact-badge">📞 +91 79847 51175</div>
#     </div>
#     <div class="hero-img-container">
#         <img src="https://raw.githubusercontent.com/jamjayjoshi108/Portfolio/main/profile_pic.png" alt="Jay J." class="hero-img" onerror="this.src='https://ui-avatars.com/api/?name=Jay+J&background=1e3c72&color=fff&size=250'">
#     </div>
# </div>
# """, unsafe_allow_html=True)


# # --- HIGH-IMPACT EXPERIENCE (DYNAMIC CARDS WITH LOGOS) ---
# st.markdown('<div class="section-title">High-Impact Experience</div>', unsafe_allow_html=True)

# st.markdown("""
# <div class="card-grid">
# <div class="exp-card card-gov">
# <img src="https://upload.wikimedia.org/wikipedia/commons/5/55/Emblem_of_India.svg" class="brand-logo" alt="Gov">
# <div class="exp-title">Sr. Good Governance Fellow</div>
# <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Government of Punjab | Current</div>
# <div class="exp-desc">Spearheading data governance, infrastructure optimization, and AI implementation to revolutionize public administration and service delivery at a state-wide level.</div>
# </div>
# <div class="exp-card card-aws">
# <img src="https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg" class="brand-logo" alt="AWS">
# <div class="exp-title">Cloud Support Engineer</div>
# <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Amazon Web Services (AWS)</div>
# <div class="exp-desc">Architected serverless data processing solutions using Lambda & EMR. Cut enterprise infrastructure costs by 50% while maintaining 99.99% REST API uptime.</div>
# </div>
# <div class="exp-card card-tesla">
# <img src="https://upload.wikimedia.org/wikipedia/commons/b/bd/Tesla_Motors.svg" class="brand-logo" alt="Tesla">
# <div class="exp-title">Data Engineer & Analytics</div>
# <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Tesla Inc.</div>
# <div class="exp-desc">Engineered robust Python-based IoT telemetry pipelines for Model 3 sensor data via Kafka, boosting predictive maintenance accuracy by 15%.</div>
# </div>
# <div class="exp-card card-jj">
# <img src="https://raw.githubusercontent.com/jamjayjoshi108/Portfolio/main/Johnson_and_Johnson_Logo.svg.png" class="brand-logo" style="height: 25px; object-fit: contain; margin-bottom: 25px;" alt="J&J">
# <div class="exp-title">Data Engineering Manager</div>
# <div style="color: #888; font-size: 0.85rem; margin-bottom: 10px;">Enstructure (Deployed at J&J)</div>
# <div class="exp-desc">Led cross-functional enterprise cloud migrations. Slashed microservice deployment times by 40% utilizing Docker and Kubernetes orchestration.</div>
# </div>
# </div>
# """, unsafe_allow_html=True)


# # --- TECHNICAL ARSENAL (HOVER PILLS) ---
# st.markdown('<div class="section-title">Technical Arsenal</div>', unsafe_allow_html=True)

# st.markdown("""
# <div class="tech-container">
#     <div class="tech-pill">☁️ Microsoft Azure</div>
#     <div class="tech-pill">🟧 AWS Platform</div>
#     <div class="tech-pill">🧱 Databricks & Spark</div>
#     <div class="tech-pill">☸️ Kubernetes & Docker</div>
#     <div class="tech-pill">🐍 Python & Scala</div>
#     <div class="tech-pill">📡 Kafka & IoT Telemetry</div>
#     <div class="tech-pill">🔐 Privileged Identity Mgmt (PIM)</div>
#     <div class="tech-pill">⚙️ CI/CD & Terraform</div>
# </div>
# """, unsafe_allow_html=True)


# # --- EDUCATION ---
# st.markdown('<div class="section-title">Education & Qualifications</div>', unsafe_allow_html=True)
# col1, col2 = st.columns(2)

# with col1:
#     st.markdown("""
# <div style="background: white; padding: 25px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 5px solid #1e3c72; min-height: 340px; display: flex; flex-direction: column; justify-content: space-between;">
# <div>
# <h4 style="margin:0; color: #1e3c72; font-weight: 800;">Post-Graduate Diploma, Business Analytics</h4>
# <p style="margin:5px 0 0 0; color: #555;">🇨🇦 Seneca College, Canada • <b style="color:#222;">GPA: 3.95</b></p>
# </div>
# <hr style="border: 0.5px solid #f0f0f0; margin: 15px 0;">
# <div>
# <h4 style="margin:0; color: #1e3c72; font-weight: 800;">M.S., Information Systems</h4>
# <p style="margin:5px 0 0 0; color: #555;">🇺🇸 Cal State LA, USA • <b style="color:#222;">GPA: 3.94</b></p>
# </div>
# <hr style="border: 0.5px solid #f0f0f0; margin: 15px 0;">
# <div>
# <h4 style="margin:0; color: #1e3c72; font-weight: 800;">B.E., Computer Engineering</h4>
# <p style="margin:5px 0 0 0; color: #555;">🇮🇳 Kadi Sarva Vishwavidyalaya, India • <b style="color:#222;">GPA: 3.77</b></p>
# </div>
# </div>
# """, unsafe_allow_html=True)

# with col2:
#     st.markdown("""
# <div style="background: linear-gradient(135deg, #ffffff 0%, #f4f7f6 100%); padding: 25px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 5px solid #00C6FF; min-height: 340px; display: flex; flex-direction: column;">
# <h4 style="margin: 0 0 15px 0; color: #00C6FF; font-weight: 800; font-size: 1.3rem;">Select Publications</h4>
# <div style="margin-bottom: 12px; padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
# <p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">The Future of Document Retrieval: Harnessing OpenAI & AWS Kendra</p>
# <p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 IEEE ICCICN</p>
# </div>
# <div style="margin-bottom: 12px; padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
# <p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">Customer Reading Rate for NYT</p>
# <p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 WiDS</p>
# </div>
# <div style="padding: 12px; background: white; border-radius: 8px; border-left: 3px solid #1e3c72; box-shadow: 0 2px 5px rgba(0,0,0,0.02);">
# <p style="margin: 0; color: #222; font-weight: 700; font-size: 0.95rem;">Lung Cancer Nodule Detection using CNN</p>
# <p style="margin: 4px 0 0 0; color: #888; font-size: 0.8rem; font-weight: 600;">📄 Cal State LA Symposium</p>
# </div>
# </div>
# """, unsafe_allow_html=True)

# st.write("<br><br><br>", unsafe_allow_html=True)


