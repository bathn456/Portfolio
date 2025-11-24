import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ahmet Batuhan Yilmaz | AI Architect",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapsed for a cleaner initial look
)

# --- CUSTOM MODERN STYLING ---
st.markdown("""
    <style>
    /* 1. Global Background - Deep Space Gradient */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #1a1c24 0%, #0e1117 100%);
        color: #f0f2f6;
    }
    
    /* 2. Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #11131a;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    /* 3. Typography Upgrade */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', sans-serif; /* Cleaner modern font */
        letter-spacing: -0.5px;
    }
    h1 { font-weight: 800; }
    
    /* 4. Hero Name - Modern Gradient */
    .hero-name {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #00C9FF 0%, #92FE9D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        color: #a0aec0;
        font-weight: 400;
        margin-bottom: 30px;
        border-left: 3px solid #00C9FF;
        padding-left: 15px;
    }
    
    /* 5. Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px -10px rgba(0, 201, 255, 0.15);
        border-color: rgba(0, 201, 255, 0.3);
    }
    
    /* 6. Skill Tags */
    .tech-tag {
        display: inline-block;
        padding: 5px 12px;
        margin: 0 6px 8px 0;
        background: rgba(0, 201, 255, 0.1);
        border: 1px solid rgba(0, 201, 255, 0.2);
        color: #92FE9D;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Remove default streamlit top padding */
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://api.dicebear.com/9.x/notionists/svg?seed=Ahmet", width=120)
    st.markdown("### Ahmet Batuhan Yilmaz")
    st.caption("AI Architect & Researcher")
    
    st.markdown("---")
    
    # Modern Icon Navigation
    page = st.radio(
        "",
        ["Home", "Expertise", "Projects", "Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.link_button("GitHub", "https://github.com/")
    with col_s2:
        st.link_button("LinkedIn", "https://linkedin.com/")
        
    st.caption("© 2025 Ahmet B. Yilmaz")

# --- HOME SECTION ---
if page == "Home":
    # 2-Column Hero Layout
    col_hero_text, col_hero_img = st.columns([1.2, 1])
    
    with col_hero_text:
        st.markdown('<div class="hero-name">Build. Scale.<br>Innovate.</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-subtitle">I engineer AI systems grounded in scientific rigor. Specializing in RAG architectures that eliminate hallucinations and deliver real business value.</div>', unsafe_allow_html=True)
        
        # Call to Actions
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.link_button("Explore Projects 🚀", "https://github.com/")
        with c2:
            st.download_button("Download CV 📄", "Placeholder Data", "Ahmet_Yilmaz_CV.pdf")
            
        st.markdown("---")
        
        # Quick Stats in Glass Cards
        st.markdown("""
        <div class="glass-card">
            <h4 style="margin:0; color:#00C9FF;">Core Focus</h4>
            <p style="margin:0; color:#a0aec0; font-size:0.9rem;">
                Retrieval-Augmented Generation (RAG) • Large Language Models • Deep Learning Research
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_hero_img:
        # Modern 3D Mesh Visualization
        # Creating a wireframe landscape to represent "Data Topology"
        x = np.linspace(-5, 5, 50)
        y = np.linspace(-5, 5, 50)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        Z = np.sin(R)

        fig = go.Figure(data=[go.Surface(
            z=Z, 
            x=X, 
            y=Y,
            colorscale='Viridis', 
            opacity=0.8,
            showscale=False
        )])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

# --- EXPERTISE SECTION ---
elif page == "Expertise":
    st.title("Technical Arsenal ⚔️")
    st.markdown("Bridging the gap between **academic theory** and **scalable production**.")
    
    # Modern Grid Layout using Columns + HTML Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🤖 Generative AI & RAG</h3>
            <p style="color:#b0bec5; font-size: 0.95rem;">
                Architecting intelligent search systems that understand context, not just keywords.
            </p>
            <br>
            <span class="tech-tag">LangChain</span>
            <span class="tech-tag">Pinecone/Chroma</span>
            <span class="tech-tag">LlamaIndex</span>
            <span class="tech-tag">OpenAI API</span>
            <span class="tech-tag">Prompt Eng.</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card">
            <h3>📊 Deep Learning & Data</h3>
            <p style="color:#b0bec5; font-size: 0.95rem;">
                Building custom neural networks for predictive analysis and computer vision.
            </p>
            <br>
            <span class="tech-tag">PyTorch</span>
            <span class="tech-tag">TensorFlow</span>
            <span class="tech-tag">Pandas</span>
            <span class="tech-tag">NumPy</span>
            <span class="tech-tag">Scikit-Learn</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>🌩️ Full-Stack Deployment</h3>
            <p style="color:#b0bec5; font-size: 0.95rem;">
                Turning Python scripts into global, accessible web applications.
            </p>
            <br>
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">FastAPI</span>
            <span class="tech-tag">Firebase</span>
            <span class="tech-tag">Docker</span>
            <span class="tech-tag">Git/CI-CD</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive Skill Meter
        st.markdown("#### Proficiency Metrics")
        skill_df = pd.DataFrame({
            "Skill": ["RAG Architecture", "Python", "Streamlit", "Deep Learning"],
            "Level": [95, 90, 95, 85]
        })
        # Custom bar chart color
        fig_skills = px.bar(skill_df, x="Level", y="Skill", orientation='h', 
                           range_x=[0,100], text="Level")
        fig_skills.update_traces(marker_color='#00C9FF', textposition='inside')
        fig_skills.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#fff',
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False),
            margin=dict(l=0, r=0, t=0, b=0),
            height=200
        )
        st.plotly_chart(fig_skills, use_container_width=True)

# --- PROJECTS SECTION ---
elif page == "Projects":
    st.title("Project Showcase 🚀")
    
    # Project 1
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#00C9FF;">📄 PDF Chatbot RAG System</h3>
            <span style="background:#2ecc71; color:black; padding:2px 8px; border-radius:4px; font-size:0.8rem; font-weight:bold;">LIVE</span>
        </div>
        <p style="margin-top:10px; color:#e0e0e0;">
            A production-ready RAG application that turns static documents into interactive knowledge bases. 
            Uses vector embeddings to reduce hallucinations and ensure answers are grounded in the source text.
        </p>
        <div style="margin-top:15px;">
            <span class="tech-tag">Streamlit</span>
            <span class="tech-tag">Vector DB</span>
            <span class="tech-tag">LLM Integration</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns([1, 4])
    with col_p1:
        st.link_button("🚀 Launch App", "https://pdf-chatbot-rag-system-batuhanyilmaz.streamlit.app")
    
    # Project 2
    st.markdown("""
    <div class="glass-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#00C9FF;">🌐 Deep Learning Portfolio Hub</h3>
            <span style="background:#2ecc71; color:black; padding:2px 8px; border-radius:4px; font-size:0.8rem; font-weight:bold;">LIVE</span>
        </div>
        <p style="margin-top:10px; color:#e0e0e0;">
            A central repository for deep learning experiments, technical documentation, and research notes. 
            Hosted on Firebase for high availability and scalability.
        </p>
        <div style="margin-top:15px;">
            <span class="tech-tag">Firebase</span>
            <span class="tech-tag">Web Dev</span>
            <span class="tech-tag">Research</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_p3, col_p4 = st.columns([1, 4])
    with col_p3:
        st.link_button("🌐 Visit Site", "https://deeplearningwithbatuhanyilmaz.web.app")

# --- CONTACT SECTION ---
elif page == "Contact":
    st.title("Let's Build Something Great 🤝")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h4>Contact Info</h4>
            <p>📧 <b>Email:</b> ybatu42@gmail.com</p>
            <p>📱 <b>Phone:</b> +90 551 706 52 03</p>
            <p>📍 <b>Location:</b> Çanakkale, Türkiye</p>
            <br>
            <p style="font-style:italic; color:#a0aec0;">
                "Open to AI Engineering roles and RAG consulting opportunities."
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("#### Send a Quick Message")
        with st.form("contact_form"):
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            
            if submit:
                st.success("Message sent! I'll get back to you shortly.")
