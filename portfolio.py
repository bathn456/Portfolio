import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Engineer Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLING ---
# Injecting some CSS to handle styling constraints and make it look modern
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
    
    /* Custom headers */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #4DB6AC;
    }

    /* Sub-headers for branding */
    .brand-tagline {
        font-size: 1.2em;
        font-style: italic;
        color: #b0bec5;
        margin-bottom: 20px;
    }
    
    /* Project cards style */
    .project-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #374151;
        margin-bottom: 20px;
    }
    
    /* Skill badges */
    .skill-badge {
        display: inline-block;
        padding: 5px 10px;
        margin: 5px;
        background-color: #4DB6AC;
        color: black;
        border-radius: 15px;
        font-size: 0.9em;
        font-weight: bold;
    }

    /* Testimonial Box */
    .testimonial {
        background-color: #1f2937;
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #4DB6AC;
        margin-bottom: 10px;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://api.dicebear.com/9.x/notionists/svg?seed=Felix", width=150) # Placeholder avatar
    st.title("Alex Dev")
    st.write("AI Architect & Strategist") # Branding change: Stronger title
    
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigate",
        ["Brand Story", "Skills & Stack", "Projects & Demos", "Experience & Talks", "Contact"]
    )
    
    st.markdown("---")
    st.write("### 🌐 Digital Presence")
    st.link_button("📝 Read my Tech Blog", "https://medium.com")
    st.link_button("🐦 Follow on X/Twitter", "https://twitter.com")
    st.link_button("💼 LinkedIn Profile", "https://linkedin.com")
    
    st.markdown("---")
    st.caption("© 2025 Alex Dev. All Rights Reserved.")

# --- HOME SECTION (Rebranded to Brand Story) ---
if page == "Brand Story":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Turning Data into Decisions 🚀")
        st.markdown('<p class="brand-tagline">I don\'t just train models; I engineer business intelligence.</p>', unsafe_allow_html=True)
        
        st.markdown("""
        ### My Mission
        In a world flooded with data, clarity is the ultimate currency. My work sits at the intersection of **Advanced Machine Learning** and **Pragmatic Engineering**. 
        
        I help companies move from *"We have an AI idea"* to *"We have a deployed, scalable solution."*
        
        **What I bring to the table:**
        * 🎯 **Strategic Vision:** Understanding the 'Why' before the 'How'.
        * ⚡ **Rapid Prototyping:** Moving from paper to production-grade MVP fast.
        * 🔧 **Scalable MLOps:** Building systems that survive the real world.
        """)
        
        st.info("📢 **Newest Article:** 'Why 90% of LLM Projects Fail in Production' - [Read Now](#)")

    with col2:
        # Social Proof / Testimonials
        st.write("### Trusted By")
        st.markdown("""
        <div class="testimonial">
        "Alex completely transformed our recommendation engine. Revenue is up 15%."
        <br><br>- <b>CTO, RetailTech Inc.</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="testimonial">
        "One of the few engineers who understands both the math and the business logic."
        <br><br>- <b>Product Lead, FinCorp</b>
        </div>
        """, unsafe_allow_html=True)

# --- SKILLS SECTION ---
elif page == "Skills & Stack":
    st.title("Technical Arsenal 🛠️")
    
    tab1, tab2, tab3 = st.tabs(["Core Skills", "Toolbox", "Soft Skills"])
    
    with tab1:
        st.subheader("Proficiency Levels")
        
        # Radar Chart for Core AI Skills
        categories = ['Python', 'PyTorch/TF', 'NLP', 'Computer Vision', 'SQL', 'MLOps', 'Data Viz']
        values = [9, 8, 9, 7, 8, 6, 7]
        
        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Proficiency',
            line_color='#4DB6AC'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 10]
                )),
            showlegend=False,
            margin=dict(l=40, r=40, t=40, b=40),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Libraries & Frameworks")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("#### Machine Learning")
            st.markdown("""
            <div style='line-height: 2.5;'>
            <span class='skill-badge'>PyTorch</span>
            <span class='skill-badge'>TensorFlow</span>
            <span class='skill-badge'>Scikit-learn</span>
            <span class='skill-badge'>HuggingFace</span>
            <span class='skill-badge'>LangChain</span>
            </div>
            """, unsafe_allow_html=True)
            
        with col_b:
            st.markdown("#### Deployment & Cloud")
            st.markdown("""
            <div style='line-height: 2.5;'>
            <span class='skill-badge'>Docker</span>
            <span class='skill-badge'>Kubernetes</span>
            <span class='skill-badge'>AWS SageMaker</span>
            <span class='skill-badge'>FastAPI</span>
            <span class='skill-badge'>MLflow</span>
            </div>
            """, unsafe_allow_html=True)
            
    with tab3:
        st.write("### Collaboration & Methodology")
        st.success("Agile Development")
        st.info("Technical Writing & Documentation")
        st.warning("Cross-functional Team Leadership")

# --- PROJECTS SECTION ---
elif page == "Projects & Demos":
    st.title("Projects & Interactive Demos 🚀")
    
    st.markdown("Here you can see not just screenshots, but interactive versions of my work.")
    
    # Project 1: Interactive NLP Demo
    with st.expander("Project 1: Real-time Sentiment Analyzer (Interactive Demo)", expanded=True):
        st.write("""
        **Type:** NLP / Text Classification  
        **Tech:** Python, NLTK (Mocked for demo), Streamlit  
        **Description:** A simple demonstration of how an ML backend connects to a Streamlit frontend.
        """)
        
        user_input = st.text_area("Enter a movie review or tweet:", "The new AI model is incredibly fast and accurate! I love it.")
        
        if st.button("Analyze Sentiment"):
            # Mock Inference Logic for Demonstration
            # In a real app, you would load your pickle model or call an API here
            blob = user_input.lower()
            if any(word in blob for word in ["good", "great", "love", "fast", "accurate", "best"]):
                sentiment = "Positive"
                color = "green"
                score = 0.95
            elif any(word in blob for word in ["bad", "slow", "hate", "error", "bug"]):
                sentiment = "Negative"
                color = "red"
                score = 0.15
            else:
                sentiment = "Neutral"
                color = "gray"
                score = 0.50
                
            st.markdown(f"### Prediction: <span style='color:{color}'>{sentiment}</span> (Confidence: {score})", unsafe_allow_html=True)
            st.progress(score)
            st.json({
                "input_length": len(user_input),
                "timestamp": datetime.now().isoformat(),
                "model_version": "v1.2.0"
            })

    # Project 2: Data Visualization
    with st.expander("Project 2: Customer Churn Prediction Dashboard"):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("#### The Challenge")
            st.write("Predicting which customers are likely to cancel their subscription based on usage patterns.")
            st.markdown("#### The Solution")
            st.write("Built an XGBoost model with 92% AUC. Deployed via FastAPI and visualized insights here.")
        
        with col2:
            # Mock Data for Visualization
            df = pd.DataFrame({
                'Feature': ['Usage_Hours', 'Contract_Age', 'Support_Tickets', 'Monthly_Bill'],
                'Importance': [0.45, 0.25, 0.20, 0.10]
            })
            fig_bar = px.bar(df, x='Importance', y='Feature', orientation='h', title="Feature Importance")
            st.plotly_chart(fig_bar, use_container_width=True)

# --- EXPERIENCE SECTION ---
elif page == "Experience & Talks":
    st.title("Professional Impact 🏔️")
    
    tab_exp, tab_talks = st.tabs(["Work History", "Speaking & Writing"])
    
    # Helper function for Timeline
    def display_experience(role, company, period, description, tags):
        with st.container():
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"**{period}**")
            with col2:
                st.subheader(f"{role} @ {company}")
                st.write(description)
                st.markdown(f"*{' • '.join(tags)}*")
                st.divider()

    with tab_exp:
        display_experience(
            "Senior AI Engineer", 
            "TechNova Solutions", 
            "2023 - Present", 
            "Leading a team of 4 engineers to deploy LLM-based customer support agents. Reduced support ticket resolution time by 40%.",
            ["LLMs", "LangChain", "Azure", "Team Lead"]
        )
        
        display_experience(
            "Machine Learning Engineer", 
            "DataCorp", 
            "2021 - 2023", 
            "Developed computer vision pipelines for quality assurance in manufacturing. Optimized inference latency by 300% using TensorRT.",
            ["Computer Vision", "TensorRT", "YOLO", "Python"]
        )
        
    with tab_talks:
        st.subheader("Thought Leadership")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.image("https://images.unsplash.com/photo-1544531586-fde5298cdd40?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3", caption="PyCon 2024")
            st.markdown("**Speaker: Optimizing Transformers for Edge Devices**")
            st.write("PyCon 2024 - Main Stage")
            st.link_button("Watch Recording", "#")
            
        with col_b:
            st.image("https://images.unsplash.com/photo-1555421689-491a97ff2040?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3", caption="Medium Article")
            st.markdown("**Author: The Future of Agentic AI**")
            st.write("Published in 'Towards Data Science' (15k+ Views)")
            st.link_button("Read Article", "#")

# --- CONTACT SECTION ---
elif page == "Contact":
    st.title("Let's Build the Future 🚀")
    
    st.write("I am currently open to **Consulting** and **Speaking Opportunities**.")
    st.write("📍 San Francisco, CA")
    st.write("📧 alex.dev@example.com")