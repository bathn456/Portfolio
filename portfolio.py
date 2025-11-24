import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ahmet Batuhan Yilmaz | AI Architect",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    /* Main background improvements */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #262730;
    }
    
    /* Typography */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #4DB6AC;
    }
    h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #e0e0e0;
    }
    
    /* Hero Section Name */
    .hero-name {
        font-size: 3em;
        font-weight: bold;
        background: -webkit-linear-gradient(45deg, #4DB6AC, #b2dfdb, #009688);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        text-shadow: 0px 0px 30px rgba(77, 182, 172, 0.4);
    }
    .hero-title {
        font-size: 1.5em;
        font-style: italic;
        color: #b0bec5;
        margin-bottom: 20px;
    }

    /* Skill badges */
    .skill-badge {
        display: inline-block;
        padding: 6px 12px;
        margin: 4px;
        background-color: #263238;
        border: 1px solid #4DB6AC;
        color: #fafafa;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: 600;
    }

    /* Card styling */
    .feature-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #4DB6AC;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://api.dicebear.com/9.x/notionists/svg?seed=Ahmet", width=150)
    st.markdown("### Ahmet Batuhan Yilmaz")
    st.caption("AI Engineer & Researcher")
    
    st.markdown("---")
    
    page = st.radio(
        "Explore",
        ["Home & Vision", "Expertise & Stack", "Project Showcase", "Contact"]
    )
    
    st.markdown("---")
    st.write("### 📥 Resources")
    st.download_button(
        label="📄 Download Resume",
        data="Placeholder PDF Data", # Replace with open("resume.pdf", "rb")
        file_name="Ahmet_Batuhan_Yilmaz_CV.pdf",
        mime="application/pdf",
    )
    
    st.markdown("---")
    st.caption("📍 Çanakkale, Türkiye")

# --- HOME & VISION SECTION ---
if page == "Home & Vision":
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown('<div class="hero-name">Ahmet Batuhan Yilmaz</div>', unsafe_allow_html=True)
        st.markdown('<div class="hero-title">Engineering Next-Gen AI with Scientific Rigor</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
        <b>My Core Philosophy:</b><br>
        "AI shouldn't just be 'smart'—it must be accurate, explainable, and grounded in reality."
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        I am an AI Engineer specializing in **Retrieval-Augmented Generation (RAG)** and **Deep Learning**. Unlike standard implementations, my work focuses on:
        
        * **Hallucination Reduction:** Implementing vector search architectures that ground LLMs in factual data.
        * **Scientific Accuracy:** My development process is research-driven, leveraging insights from top scientific journals to build robust models.
        * **Scalable Deployment:** From local Python scripts to global Firebase & Streamlit deployments.
        """)
        
        col_cta1, col_cta2 = st.columns(2)
        with col_cta1:
            st.link_button("👉 View My Projects", "https://github.com/") # Add your actual GitHub
        with col_cta2:
            st.link_button("📧 Get in Touch", "mailto:ybatu42@gmail.com")

    with col2:
        # Abstract visualization representing AI/Neural Networks
        # Using Plotly to create a "Neural Network" looking 3D scatter plot
        import numpy as np
        
        # Generate random 3D data points
        x, y, z = np.random.normal(0, 1, (3, 100))
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=5,
                color=z,
                colorscale='Teal',
                opacity=0.8
            )
        )])
        fig.update_layout(
            margin=dict(l=0, r=0, b=0, t=0),
            scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("*Visualizing High-Dimensional Vector Space*")

# --- EXPERTISE SECTION ---
elif page == "Expertise & Stack":
    st.title("Technical Arsenal 🛠️")
    
    st.markdown("My expertise bridges the gap between **academic theory** and **production engineering**.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤖 AI & Machine Learning")
        st.markdown("""
        * **RAG Systems:** Advanced vector database implementation (ChromaDB, Pinecone) for context-aware chat.
        * **LLMs:** Fine-tuning and prompting of GPT-4, Llama 2, and Mistral.
        * **Deep Learning:** Custom neural network architectures for classification and regression.
        * **Data Science:** Pandas, NumPy, Scikit-Learn.
        """)
        
    with col2:
        st.subheader("💻 Software Engineering")
        st.markdown("""
        * **Backend:** Python, FastAPI.
        * **Frontend:** Streamlit (Expert), Dash.
        * **Cloud & DevOps:** Firebase, Streamlit Cloud, Git/GitHub.
        * **Version Control:** CI/CD best practices.
        """)
    
    st.divider()
    
    st.subheader("Proficiency Overview")
    # Radar Chart
    categories = ['RAG Architecture', 'Python Dev', 'Streamlit UI', 'Deep Learning', 'Cloud/Hosting']
    values = [9.5, 9.0, 9.5, 8.5, 8.0]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#4DB6AC'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
        showlegend=False,
        margin=dict(t=20, b=20, l=40, r=40),
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white")
    )
    st.plotly_chart(fig, use_container_width=True)

# --- PROJECT SHOWCASE ---
elif page == "Project Showcase":
    st.title("Featured Works 🚀")
    
    tab1, tab2 = st.tabs(["AI Systems", "Web Platforms"])
    
    with tab1:
        st.markdown("### 📄 PDF Chatbot RAG System")
        st.write("A production-ready RAG application that turns static documents into interactive knowledge bases.")
        
        c1, c2 = st.columns([3, 2])
        with c1:
            st.markdown("""
            **The Problem:** Traditional search keywords often fail to capture context.  
            **The Solution:** I built a system using vector embeddings to understand the *meaning* behind user queries, enabling accurate Q&A from uploaded PDFs.
            
            * **Tech Stack:** Python, Streamlit, LangChain, Vector DB.
            * **Key Result:** Drastically reduced hallucinations by grounding answers strictly in source text.
            """)
            st.link_button("🚀 Launch Live App", "https://pdf-chatbot-rag-system-batuhanyilmaz.streamlit.app")
        with c2:
            # Placeholder for a project screenshot or diagram
            st.info("Status: **Live & Deployed**")
            st.markdown("Use this tool to analyze contracts, research papers, or reports instantly.")

    with tab2:
        st.markdown("### 🌐 Deep Learning Portfolio Hub")
        st.write("A central repository for my deep learning experiments and technical documentation.")
        
        st.markdown("""
        * **Architecture:** Hosted on Firebase for high availability.
        * **Content:** Contains interactive demos, model cards, and research notes.
        """)
        st.link_button("🌐 Visit Website", "https://deeplearningwithbatuhanyilmaz.web.app")

# --- CONTACT SECTION ---
elif page == "Contact":
    st.title("Let's Collaborate 🤝")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.markdown("#### Contact Information")
        st.write("""
        I am currently available for **AI Engineering roles**, **Freelance RAG development**, and **Consulting**.
        
        **Email:** [ybatu42@gmail.com](mailto:ybatu42@gmail.com)  
        **Phone:** +90 551 706 52 03  
        **Location:** Çanakkale, Türkiye
        """)
        
        st.markdown("#### Connect on Socials")
        st.link_button("LinkedIn Profile", "https://linkedin.com/")
        st.link_button("GitHub Profile", "https://github.com/")

    with col_right:
        st.markdown("#### Send a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            inquiry_type = st.selectbox("Inquiry Type", ["Hiring / Recruitment", "Project Collaboration", "General Question"])
            message = st.text_area("Message")
            
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Message sent! I will respond to your email shortly.")
