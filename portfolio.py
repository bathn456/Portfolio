import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# --- ASSET HANDLING ---
# 1. Load Icon: Checks for local 'icon.png', falls back to online URL if missing
icon_path = "icon.png"
if os.path.exists(icon_path):
    page_icon = icon_path
else:
    # Fallback to the online black "B" if local file isn't found
    page_icon = "https://img.icons8.com/ios-glyphs/30/000000/b.png"

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Batuhan Yılmaz | AI Architect",
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- STATE MANAGEMENT FOR NAVIGATION ---
if 'page' not in st.session_state:
    st.session_state.page = "Overview"

def set_page(page_name):
    st.session_state.page = page_name

# --- CUSTOM "CUPERTINO" STYLING ---
st.markdown("""
    <style>
    /* 1. Global Background - Apple Off-White */
    .stApp {
        background-color: #f5f5f7;
        color: #1d1d1f;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* 2. Custom Navbar Styling (Secondary Buttons) */
    div.stButton > button[kind="secondary"] {
        background-color: transparent;
        color: #1d1d1f;
        border: none;
        font-size: 1rem;
        font-weight: 500;
        padding: 0.5rem 1rem;
        transition: color 0.2s, background-color 0.2s;
    }
    
    div.stButton > button[kind="secondary"]:hover {
        color: #0071e3;
        background-color: rgba(0, 113, 227, 0.1);
        border-radius: 8px;
    }
    
    div.stButton > button[kind="secondary"]:focus {
        background-color: #0071e3 !important;
        color: white !important;
        border-radius: 20px;
    }

    /* 3. Primary CTA Button Styling (The "View Projects" Button) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0071e3 0%, #0077ed 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.6rem 1.8rem;
        font-size: 1.1rem;
        font-weight: 600;
        box-shadow: 0 4px 14px rgba(0, 113, 227, 0.3);
        transition: all 0.3s ease;
        letter-spacing: 0.02em;
    }

    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 113, 227, 0.4);
        background: linear-gradient(135deg, #0077ed 0%, #0088ff 100%);
        border: none;
    }

    /* 4. Typography - San Francisco Style */
    h1, h2, h3, h4 {
        font-weight: 600;
        letter-spacing: -0.02em;
        color: #1d1d1f;
    }
    
    p {
        color: #86868b;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    
    /* 5. Hero Name - Massive & Clean */
    .hero-name {
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(180deg, #1d1d1f 0%, #424245 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        line-height: 1.05;
        letter-spacing: -0.03em;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #86868b;
        font-weight: 400;
        margin-bottom: 40px;
        max-width: 600px;
    }
    
    /* 6. Bento Box Cards */
    .apple-card {
        background: #ffffff;
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 24px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.04);
        transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        border: 1px solid rgba(0,0,0,0.02);
    }
    
    .apple-card:hover {
        transform: scale(1.01);
        box-shadow: 0 12px 40px rgba(0,0,0,0.08);
    }
    
    /* 7. Tags & Badges */
    .tech-badge {
        display: inline-block;
        padding: 6px 14px;
        margin: 0 6px 8px 0;
        background: #f5f5f7;
        color: #1d1d1f;
        border-radius: 980px; /* Pill shape */
        font-size: 0.85rem;
        font-weight: 500;
    }
    
    /* Remove default padding - Adjusted to 3.5rem to prevent top bar overlap */
    .block-container {
        padding-top: 3.5rem;
        padding-bottom: 5rem;
    }
    
    /* Link styling */
    a {
        color: #0071e3;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION BAR ---
col_logo, col_nav1, col_nav2, col_nav3, col_nav4, col_social = st.columns([2, 1, 1, 1, 1, 1])

with col_logo:
    st.markdown("<h3 style='margin:0; padding-top:5px;'>Batuhan Yılmaz</h3>", unsafe_allow_html=True)

with col_nav1:
    if st.button("Overview", type="secondary"):
        set_page("Overview")
with col_nav2:
    if st.button("Expertise", type="secondary"):
        set_page("Expertise")
with col_nav3:
    if st.button("Projects", type="secondary"):
        set_page("Projects")
with col_nav4:
    if st.button("Contact", type="secondary"):
        set_page("Contact")

with col_social:
    st.markdown("""
        <div style="text-align: right; padding-top: 10px;">
            <a href="https://github.com/" target="_blank" style="color:#1d1d1f; font-weight:bold; font-size: 0.9rem;">GitHub ↗</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- PAGE ROUTING ---
page = st.session_state.page

# --- OVERVIEW SECTION ---
if page == "Overview":
    st.markdown("<br>", unsafe_allow_html=True)
    
    c1, c2 = st.columns([1.5, 1])
    
    with c1:
        st.markdown('<div class="hero-name">Engineering<br>Intelligence.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">High-precision RAG architectures grounded in scientific rigor.</div>', unsafe_allow_html=True)
        
        col_cta1, col_cta2 = st.columns([1, 2])
        with col_cta1:
            # Using type="primary" triggers our custom CSS above
            if st.button("View Projects 🚀", key="hero_cta", type="primary"):
                set_page("Projects")
                st.rerun()
                
        with col_cta2:
            # 2. Resume File Logic
            resume_path = "resume.pdf"
            if os.path.exists(resume_path):
                with open(resume_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download Resume",
                        data=pdf_file,
                        file_name="Batuhan_Yilmaz_CV.pdf",
                        mime="application/pdf"
                    )
            else:
                st.download_button(
                    label="Download Resume (Demo)",
                    data="Please add a file named resume.pdf to the root directory.",
                    file_name="placeholder.txt"
                )

    with c2:
        # Elegant smooth mesh visualization
        x = np.linspace(-3, 3, 50)
        y = np.linspace(-3, 3, 50)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(X) * np.cos(Y)

        fig = go.Figure(data=[go.Surface(
            z=Z, x=X, y=Y,
            colorscale=[[0, '#eef2f3'], [1, '#0071e3']], 
            showscale=False,
            opacity=0.9
        )])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # "Feature" Grid - Bento Box Style
    st.subheader("Core Technologies")
    row1_1, row1_2, row1_3 = st.columns(3)
    
    with row1_1:
        st.markdown("""
        <div class="apple-card">
            <h3 style="color:#0071e3;">RAG Systems</h3>
            <p>Advanced vector search architectures that eliminate hallucinations.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with row1_2:
        st.markdown("""
        <div class="apple-card">
            <h3 style="color:#bf4800;">Deep Learning</h3>
            <p>Custom neural networks optimized for predictive accuracy.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with row1_3:
        st.markdown("""
        <div class="apple-card">
            <h3 style="color:#8e8e93;">Scientific Rigor</h3>
            <p>Methodologies backed by the latest peer-reviewed research.</p>
        </div>
        """, unsafe_allow_html=True)

# --- EXPERTISE SECTION ---
elif page == "Expertise":
    st.title("Technical Proficiencies")
    st.markdown("A seamless blend of academic theory and production engineering.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="apple-card">
            <h3>Generative AI & LLMs</h3>
            <p>Building the next generation of context-aware applications.</p>
            <br>
            <div>
                <span class="tech-badge">LangChain</span>
                <span class="tech-badge">Pinecone</span>
                <span class="tech-badge">OpenAI</span>
                <span class="tech-badge">LlamaIndex</span>
                <span class="tech-badge">Vector DBs</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        c_a, c_b = st.columns(2)
        with c_a:
             st.markdown("""
            <div class="apple-card">
                <h4>Data Science</h4>
                <p style="font-size:0.9rem">Pandas, NumPy, Scikit-Learn</p>
            </div>
            """, unsafe_allow_html=True)
        with c_b:
             st.markdown("""
            <div class="apple-card">
                <h4>Deployment</h4>
                <p style="font-size:0.9rem">Streamlit, Docker, Firebase</p>
            </div>
            """, unsafe_allow_html=True)
            
    with col2:
        st.markdown("""
        <div class="apple-card" style="height: 100%;">
            <h4>Skill Metrics</h4>
            <br>
        """, unsafe_allow_html=True)
        
        skill_df = pd.DataFrame({
            "Skill": ["RAG Architecture", "Python", "Streamlit", "Deep Learning"],
            "Value": [95, 90, 95, 85]
        })
        
        fig_skills = px.bar(skill_df, x="Value", y="Skill", orientation='h', text="Value")
        fig_skills.update_traces(marker_color='#1d1d1f', textposition='inside', textfont_color='white')
        fig_skills.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False),
            margin=dict(l=0, r=0, t=0, b=0),
            height=300
        )
        st.plotly_chart(fig_skills, use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- PROJECTS SECTION ---
elif page == "Projects":
    st.title("Selected Works")
    st.markdown("Innovation in every line of code.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="apple-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
             <h2 style="margin:0;">PDF Chatbot RAG System</h2>
             <span style="color:#2ecc71; font-weight:600; font-size:0.8rem;">● Live</span>
        </div>
        <p style="margin-top:10px; font-size:1.1rem;">
            A production-ready intelligent document assistant.
        </p>
        <p style="font-size:0.95rem; color:#86868b;">
            Uses advanced vector embeddings to retrieve precise context from uploaded PDF documents, effectively eliminating AI hallucinations.
        </p>
        <br>
        <span class="tech-badge">Streamlit</span>
        <span class="tech-badge">RAG</span>
        <span class="tech-badge">LLM Integration</span>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 4])
    with c1:
        st.link_button("Launch App ↗", "https://pdf-chatbot-rag-system-batuhanyilmaz.streamlit.app")
        
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="apple-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
             <h2 style="margin:0;">Deep Learning Portfolio Hub</h2>
             <span style="color:#2ecc71; font-weight:600; font-size:0.8rem;">● Live</span>
        </div>
        <p style="margin-top:10px; font-size:1.1rem;">
            The central nervous system for my research.
        </p>
        <p style="font-size:0.95rem; color:#86868b;">
            A Firebase-hosted platform dedicated to showcasing deep learning experiments, technical documentation, and scientific analysis.
        </p>
        <br>
        <span class="tech-badge">Firebase</span>
        <span class="tech-badge">Web Dev</span>
        <span class="tech-badge">Research</span>
    </div>
    """, unsafe_allow_html=True)
    
    c3, c4 = st.columns([1, 4])
    with c3:
        st.link_button("Visit Site ↗", "https://deeplearningwithbatuhanyilmaz.web.app")

# --- CONTACT SECTION ---
elif page == "Contact":
    st.title("Get in Touch")
    
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("""
        <div class="apple-card">
            <h3>Contact Information</h3>
            <br>
            <p><b>Email</b><br>ybatu42@gmail.com</p>
            <p><b>Phone</b><br>+90 551 706 52 03</p>
            <p><b>Location</b><br>Çanakkale, Türkiye</p>
            <br>
            <p style="font-size:0.9rem; color:#86868b;">
                Available for AI Engineering roles and consulting.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="apple-card">
            <h3>Send a Message</h3>
            <p style="font-size:0.9rem">I'll get back to you as soon as possible.</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            st.text_input("Name")
            st.text_input("Email")
            st.text_area("Message")
            st.form_submit_button("Send Message")
