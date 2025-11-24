import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ahmet Batuhan Yilmaz | AI Architect",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM "NEO-CYBERPUNK" STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Space+Grotesk:wght@300;600;700&display=swap');

    /* 1. Global Background - The "Matrix" Void */
    .stApp {
        background-color: #050505;
        background-image: 
            linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        color: #e0e0e0;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* 2. Sidebar - Stealth Mode */
    section[data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 1px solid #1f1f1f;
    }
    
    /* 3. Typography - Engineered */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .mono-font {
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* 4. Hero Name - Glitch Effect Style */
    .hero-name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4rem;
        font-weight: 800;
        color: #fff;
        text-shadow: 2px 2px 0px #bc13fe;
        line-height: 1.1;
        margin-bottom: 15px;
    }
    
    .hero-subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        color: #00ff41; /* Toxic Green */
        border-left: 4px solid #bc13fe; /* Cyber Purple */
        padding-left: 20px;
        margin-bottom: 30px;
    }
    
    /* 5. Cyber Cards - High Contrast Borders */
    .cyber-card {
        background: #0a0a0a;
        border: 1px solid #333;
        border-left: 4px solid #00ff41;
        padding: 25px;
        margin-bottom: 25px;
        position: relative;
        transition: all 0.2s ease-in-out;
    }
    
    .cyber-card:hover {
        border-color: #bc13fe;
        box-shadow: 0 0 15px rgba(188, 19, 254, 0.2);
        transform: translateX(5px);
    }
    
    /* Corner Accents for Cards */
    .cyber-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 10px;
        height: 10px;
        border-top: 2px solid #fff;
        border-right: 2px solid #fff;
    }

    /* 6. Skill Terminal Tags */
    .tech-tag {
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        padding: 4px 10px;
        margin: 0 6px 8px 0;
        background: #111;
        border: 1px solid #00ff41;
        color: #00ff41;
        font-size: 0.8rem;
    }
    
    /* Buttons Override */
    div.stButton > button {
        background-color: #000;
        color: #00ff41;
        border: 1px solid #00ff41;
        border-radius: 0;
        font-family: 'JetBrains Mono', monospace;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #00ff41;
        color: #000;
        box-shadow: 0 0 10px #00ff41;
    }
    
    /* Remove default top padding */
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://api.dicebear.com/9.x/notionists/svg?seed=Ahmet", width=120)
    st.markdown("### AHMET B. YILMAZ")
    st.markdown("<span style='color:#00ff41; font-family:JetBrains Mono'>AI_ARCHITECT</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "SYSTEM_NAV",
        ["// HOME", "// EXPERTISE", "// PROJECTS", "// CONTACT"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.link_button("GIT_HUB", "https://github.com/")
    with col_s2:
        st.link_button("LINKED_IN", "https://linkedin.com/")
        
    st.caption("SYS.VER.2025.1")

# --- HOME SECTION ---
if page == "// HOME":
    # 2-Column Hero Layout
    col_hero_text, col_hero_img = st.columns([1.5, 1])
    
    with col_hero_text:
        st.markdown('<div class="hero-name">ENGINEERING<br>INTELLIGENCE.</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="hero-subtitle">
        > INITIALIZING RAG_SYSTEMS...<br>
        > OPTIMIZING LLM_VECTORS...<br>
        > ELIMINATING HALLUCINATIONS...<br><br>
        I build high-precision AI architectures grounded in scientific rigor.
        </div>
        """, unsafe_allow_html=True)
        
        # Call to Actions
        c1, c2 = st.columns([1, 1.5])
        with c1:
            st.button("INIT_PROJECTS 🚀")
        with c2:
            st.download_button("DOWNLOAD_DATA [CV] 💾", "Placeholder Data", "Ahmet_Yilmaz_CV.pdf")
            
        st.markdown("---")
        
        # Quick Stats in Cyber Cards
        st.markdown("""
        <div class="cyber-card">
            <h4 class="mono-font" style="margin:0; color:#bc13fe;">// CORE_DIRECTIVE</h4>
            <p style="margin:0; color:#a0aec0; font-size:0.9rem; margin-top: 10px;">
                Retrieval-Augmented Generation • Vector Search • Deep Learning Research
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_hero_img:
        # Cyber Wireframe Visualization
        # Creating a digital terrain mesh
        x = np.linspace(-5, 5, 40)
        y = np.linspace(-5, 5, 40)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        fig = go.Figure(data=[go.Surface(
            z=Z, x=X, y=Y,
            colorscale='Electric', # Neon colors
            showscale=False,
            contours = {
                "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
                "y": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05, "color":"white"},
                "z": {"show": False}
            }
        )])
        
        fig.update_layout(
            scene=dict(
                xaxis=dict(visible=False, backgroundcolor="rgba(0,0,0,0)"),
                yaxis=dict(visible=False, backgroundcolor="rgba(0,0,0,0)"),
                zaxis=dict(visible=False, backgroundcolor="rgba(0,0,0,0)"),
                bgcolor='rgba(0,0,0,0)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=0, r=0, t=0, b=0),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

# --- EXPERTISE SECTION ---
elif page == "// EXPERTISE":
    st.title("TECHNICAL_ARSENAL ⚔️")
    st.markdown("<span class='mono-font'>BRIDGING ACADEMIC THEORY <-> PRODUCTION SCALING</span>", unsafe_allow_html=True)
    st.write("") # Spacer
    
    # Grid Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="cyber-card">
            <h3 class="mono-font" style="color:#00ff41;">01. GEN_AI & RAG</h3>
            <p style="color:#e0e0e0;">
                Architecting context-aware search systems.
            </p>
            <div style="margin-top:15px;">
                <span class="tech-tag">LANGCHAIN</span>
                <span class="tech-tag">PINECONE</span>
                <span class="tech-tag">OPENAI API</span>
                <span class="tech-tag">LLAMA_INDEX</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cyber-card">
            <h3 class="mono-font" style="color:#bc13fe;">02. DEEP LEARNING</h3>
            <p style="color:#e0e0e0;">
                Custom neural networks for predictive analysis.
            </p>
            <div style="margin-top:15px;">
                <span class="tech-tag">PYTORCH</span>
                <span class="tech-tag">TENSORFLOW</span>
                <span class="tech-tag">NUMPY</span>
                <span class="tech-tag">SCIKIT-LEARN</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="cyber-card">
            <h3 class="mono-font" style="color:#fff;">03. FULL_STACK</h3>
            <p style="color:#e0e0e0;">
                Deploying Python logic to global endpoints.
            </p>
            <div style="margin-top:15px;">
                <span class="tech-tag">STREAMLIT</span>
                <span class="tech-tag">FASTAPI</span>
                <span class="tech-tag">DOCKER</span>
                <span class="tech-tag">FIREBASE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Techy Bar Chart
        st.markdown("<h4 class='mono-font'>// SKILL_METRICS_LOADED</h4>", unsafe_allow_html=True)
        skill_df = pd.DataFrame({
            "MODULE": ["RAG_ARCH", "PYTHON", "STREAMLIT", "NN_MODELS"],
            "LEVEL": [98, 92, 95, 88]
        })
        
        fig_skills = px.bar(skill_df, x="LEVEL", y="MODULE", orientation='h', 
                           range_x=[0,100], text="LEVEL")
        fig_skills.update_traces(marker_color='#bc13fe', textfont_family='JetBrains Mono')
        fig_skills.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='#00ff41',
            font_family='JetBrains Mono',
            xaxis=dict(showgrid=True, gridcolor='#333'),
            yaxis=dict(showgrid=False),
            margin=dict(l=0, r=0, t=0, b=0),
            height=200
        )
        st.plotly_chart(fig_skills, use_container_width=True)

# --- PROJECTS SECTION ---
elif page == "// PROJECTS":
    st.title("PROJECT_DATABASE 📂")
    
    # Project 1
    st.markdown("""
    <div class="cyber-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#00ff41;">> PDF_CHATBOT_RAG</h3>
            <span style="background:#00ff41; color:black; padding:2px 8px; font-family:'JetBrains Mono'; font-weight:bold;">STATUS: ONLINE</span>
        </div>
        <p style="margin-top:10px; color:#e0e0e0; font-family:'JetBrains Mono'; font-size: 0.9rem;">
            SYSTEM_DESC: Production-ready RAG application turning static docs into interactive knowledge bases.<br>
            OBJECTIVE: Reduce hallucinations via vector embeddings.
        </p>
        <div style="margin-top:15px;">
            <span class="tech-tag">STREAMLIT</span>
            <span class="tech-tag">VECTOR_DB</span>
            <span class="tech-tag">LLM_INTEGRATION</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns([1, 4])
    with col_p1:
        st.link_button("EXECUTE_APP [>>]", "https://pdf-chatbot-rag-system-batuhanyilmaz.streamlit.app")
    
    # Project 2
    st.markdown("""
    <div class="cyber-card" style="border-left: 4px solid #bc13fe;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <h3 style="margin:0; color:#bc13fe;">> DL_PORTFOLIO_HUB</h3>
            <span style="background:#bc13fe; color:white; padding:2px 8px; font-family:'JetBrains Mono'; font-weight:bold;">STATUS: ONLINE</span>
        </div>
        <p style="margin-top:10px; color:#e0e0e0; font-family:'JetBrains Mono'; font-size: 0.9rem;">
            SYSTEM_DESC: Central repository for deep learning experiments and docs.<br>
            HOSTING: Firebase high-availability cluster.
        </p>
        <div style="margin-top:15px;">
            <span class="tech-tag">FIREBASE</span>
            <span class="tech-tag">WEB_DEV</span>
            <span class="tech-tag">RESEARCH</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_p3, col_p4 = st.columns([1, 4])
    with col_p3:
        st.link_button("ACCESS_HUB [>>]", "https://deeplearningwithbatuhanyilmaz.web.app")

# --- CONTACT SECTION ---
elif page == "// CONTACT":
    st.title("ESTABLISH_UPLINK 📡")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="cyber-card">
            <h4 class="mono-font">COMMS_CHANNEL</h4>
            <p>📧 <b>EMAIL:</b> ybatu42@gmail.com</p>
            <p>📱 <b>PHONE:</b> +90 551 706 52 03</p>
            <p>📍 <b>LOC:</b> Çanakkale, Türkiye</p>
            <br>
            <p style="color:#00ff41; font-family:'JetBrains Mono';">
                "Ready for new AI directives and RAG consulting."
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("<h4 class='mono-font'>SEND_TRANSMISSION</h4>", unsafe_allow_html=True)
        with st.form("contact_form"):
            name = st.text_input("USER_ID")
            email = st.text_input("RETURN_ADDRESS")
            message = st.text_area("DATA_PACKET")
            submit = st.form_submit_button("TRANSMIT")
            
            if submit:
                st.success("TRANSMISSION_RECEIVED. STAND BY FOR RESPONSE.")
