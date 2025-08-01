import streamlit as st
from datetime import datetime
import base64

# Page configuration
st.set_page_config(
    page_title="Sai Yashwanth Dasari - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
/* Import classy poster fonts */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Lato&display=swap');

.stApp {
    background-color: #1B1B1B;
    color: #F4F4F4;
    font-family: 'Lato', sans-serif;
}

/* Header like a movie poster */
.main-header {
    text-align: center;
    padding: 2rem 0;
    background: #1B1B1B;
    color: #D4AF37;
    font-family: 'Cinzel', serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    border-bottom: 3px solid #D4AF37;
    padding-top: 20px !important;
}

/* Section headers */
.section-header {
    color: #D4AF37;
    font-family: 'Cinzel', serif;
    font-size: 1.6rem;
    letter-spacing: 1px;
    border-bottom: 1px solid #D4AF37;
    padding-bottom: 0.4rem;
    margin-bottom: 1.5rem;
}

/* Cards */
.profile-section, .experience-card, .project-card {
    background: #2A2A2A;
    border: 1px solid #D4AF37;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0px 0px 15px rgba(212,175,55,0.15);
    margin-bottom: 1.5rem;
}

/* Skill badges */
.skill-badge {
    background: linear-gradient(145deg, #D4AF37, #BFA14A);
    color: #1B1B1B;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    display: inline-block;
    margin: 0.2rem;
}

/* Links/Buttons */
.demo-button {
    background: linear-gradient(145deg, #3a3a3a, #2a2a2a); /* Soft dark base */
    color: #f5d67b !important; /* Soft warm gold text */
    padding: 0.7rem 1.4rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    letter-spacing: 1px;
    border: 1px solid #c2a14a; /* Subtle golden border */
    box-shadow: 0 2px 6px rgba(0,0,0,0.4);
    transition: all 0.3s ease;
}

.demo-button:hover {
    background: linear-gradient(145deg, #4a4a4a, #3a3a3a); /* Slightly lighter on hover */
    box-shadow: 0 4px 10px rgba(0,0,0,0.5), 0 0 6px rgba(194,161,74,0.6);
    transform: translateY(-2px);
}


/* Contact info */
.contact-info {
    background: #2A2A2A;
    padding: 1rem;
    border-radius: 6px;
    border: 1px solid #D4AF37;
}

/* Tabs style */
.stTabs [role="tablist"] {
    border-bottom: 2px solid #D4AF37;
}
.stTabs [role="tab"] {
    color: #F4F4F4;
}
</style>
""", unsafe_allow_html=True)



# Header Section
st.markdown("""
<div class="main-header">
    <h1>🚀 Sai Yashwanth Dasari</h1>
    <h3>AI/ML Engineer & Full-Stack Developer</h3>
    <p>Building intelligent solutions with cutting-edge technology</p>

    
</div>
""", unsafe_allow_html=True)

# Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 About", "💼 Experience", "🚀 Projects", "🛠️ Skills", "📞 Contact"])

with tab1:
    st.markdown('<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;"><h2 style="margin: 0; color: #1E90FF;">About Me</h2> <a href="https://drive.google.com/file/d/1Trf_k8mF0WYgBJ1jvhW01mrXcbepQ0hi/view" target="_blank" style="font-size: 0.8rem; color: #FFD700; text-decoration: none; border: 1px solid #FFD700; padding: 4px 10px; border-radius: 4px;transition: all 0.3s ease;">Resume</a></h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <h4 style="color: #667eea; "></h4>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                I’m a final-year B.Tech student in <strong>Artificial Intelligence and Machine Learning</strong> (2025) 
                with a strong focus on <strong>Backend Development</strong>. I enjoy building reliable, scalable web 
                applications and REST APIs using <strong>Python, Django, FastAPI</strong>, and <strong>PostgreSQL</strong>.  
                I also explore <strong>AI/ML</strong> to add intelligent features like recommendations and automation 
                into backend systems.
            </p>
            
        <h4 style="color: #667eea; margin-top: 2rem;">🎯 What I Do</h4>
            <ul style="font-size: 1.1rem; line-height: 1.8;">
                <li><strong>Backend Development:</strong> REST APIs, authentication systems, and database design using Django/FastAPI</li>
                <li><strong>Database Management:</strong> PostgreSQL, MySQL, and query optimization</li>
                <li><strong>API Integration:</strong> Connecting services and building robust data pipelines</li>
                <li><strong>AI/ML for Backend:</strong> Implementing intelligent automation and recommendation features</li>
            </ul>

        <h4 style="color: #667eea; margin-top: 2rem;">💡 Why Me</h4>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                I’m looking for a <strong>backend-focused internship</strong> where I can apply my skills, 
                learn from real-world projects, and contribute to building systems that are 
                <strong>clean, efficient, and scalable</strong>.  
                My mix of backend expertise and AI/ML exposure allows me to approach problems 
                with both <strong>engineering precision</strong> and <strong>innovative thinking</strong>.
            </p>
        
        """, unsafe_allow_html=True)


    
    with col2:
        st.markdown("""
        <div class="profile-section" style="background-color: #1B1B1B; padding: 1rem; border-radius: 8px; color: white;">
            <h4 style="color: #D4AF37; text-align: center;">📊 Quick Stats</h4>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0;">
                <strong>CGPA:</strong> 7.88/10
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0;">
                <strong>Projects:</strong> 8+
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0;">
                <strong>Experience:</strong> 1+ Years
            </p>
            <p style="font-size: 1.1rem; line-height: 1.8; margin: 0;">
                <strong>LeetCode:</strong> 200+
            </p>
        </div>
    """, unsafe_allow_html=True)


with tab2:
    st.markdown('<h2 class="section-header">Professional Experience</h2>', unsafe_allow_html=True)
    
    # Software Engineer Intern
    st.markdown("""
    <div class="experience-card">
        <h3 style="color: #667eea;">Software Engineer Intern</h3>
        <h4 style="color: #6c757d;">Workcohol • Remote • Dec 2024 – Jan 2025</h4>
        <ul style="margin-top: 1rem;">
            <li>Developed comprehensive survey management platform using <strong>Django framework</strong></li>
            <li>Built RESTful APIs for survey form creation, response collection, and data analytics</li>
            <li>Implemented user authentication system and role-based access control</li>
            <li>Designed optimized database models for complex survey structures</li>
            <li>Created admin panel with intuitive UI and real-time data visualization</li>
        </ul>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Django</span>
            <span class="skill-badge">PostgreSQL</span>
            <span class="skill-badge">REST API</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Deep Learning Research Intern
    st.markdown("""
    <div class="experience-card">
        <h3 style="color: #667eea;">Deep Learning Research Intern</h3>
        <h4 style="color: #6c757d;">University of Hyderabad • Hyderabad, India • Sep 2023 – Jan 2024</h4>
        <ul style="margin-top: 1rem;">
            <li>Developed deep learning models for automatic annotation of <strong>Telugu movie songs</strong></li>
            <li>Implemented <strong>Generative Adversarial Networks (GANs)</strong> for audio pattern recognition</li>
            <li>Conducted research on traditional Raaga elements extraction from regional music datasets</li>
            <li><strong>Co-authored research paper</strong> accepted at IHCI 2023 conference</li>
            <li>Utilized PyTorch, Google's Magenta, and audio processing libraries</li>
        </ul>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">PyTorch</span>
            <span class="skill-badge">GANs</span>
            <span class="skill-badge">Audio Processing</span>
            <span class="skill-badge">Research</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Machine Learning Intern
    st.markdown("""
    <div class="experience-card">
        <h3 style="color: #667eea;">Machine Learning Intern</h3>
        <h4 style="color: #6c757d;">LBITS • Hyderabad, India • Nov 2022 – Jan 2023</h4>
        <ul style="margin-top: 1rem;">
            <li>Developed full-stack web application for <strong>stock market trend prediction</strong></li>
            <li>Achieved <strong>72% accuracy</strong> using KNN algorithm implementation</li>
            <li>Designed responsive frontend interface improving user interaction efficiency</li>
            <li>Built end-to-end ML pipeline from data preprocessing to model deployment</li>
        </ul>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">Python</span>
            <span class="skill-badge">Flask</span>
            <span class="skill-badge">MySQL</span>
            <span class="skill-badge">KNN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown('<h2 class="section-header">Featured Projects</h2>', unsafe_allow_html=True)
    
    # Medical AI Chatbot
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #667eea;">🏥 Medical AI Chatbot</h3>
        <p><strong>Technologies:</strong> Python, Streamlit, LangChain, RAG, Vector DB</p>
        <p style="line-height: 1.6;">
            Built an intelligent medical chatbot using <strong>Retrieval-Augmented Generation (RAG)</strong> architecture. 
            The system integrates LangChain framework with vector databases for accurate medical knowledge retrieval 
            and provides natural language medical consultations.
        </p>
        <ul>
            <li>Implemented advanced RAG architecture for medical knowledge retrieval</li>
            <li>Integrated multiple LLM APIs for natural language understanding</li>
            <li>Deployed production-ready application on Streamlit Cloud</li>
            <li>Achieved high accuracy in medical response generation</li>
        </ul>
        <a href="https://altibbemedical.streamlit.app/" target="_blank" class="demo-button">🌐 Live Demo</a>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">RAG</span>
            <span class="skill-badge">LangChain</span>
            <span class="skill-badge">Vector DB</span>
            <span class="skill-badge">Streamlit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Multi-Modal AI Chatbot
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #667eea;">🤖 Multi-Modal AI Chatbot</h3>
        <p><strong>Technologies:</strong> Flask, API Integration, JavaScript</p>
        <p style="line-height: 1.6;">
            Developed an advanced AI chatbot that handles both <strong>text and image inputs</strong> with 75% accuracy. 
            The system processes multimodal data in real-time using multiple APIs and provides intelligent responses 
            across different input formats.
        </p>
        <ul>
            <li>Integrated Cohere API for natural language understanding</li>
            <li>Implemented Imagga API for advanced image recognition</li>
            <li>Created middleware for real-time multimodal data processing</li>
            <li>Developed responsive UI with modern JavaScript</li>
        </ul>
        <a href="https://projectz-8x7k.onrender.com/" target="_blank" class="demo-button">🌐 Live Demo</a>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">Flask</span>
            <span class="skill-badge">API Integration</span>
            <span class="skill-badge">Multimodal AI</span>
            <span class="skill-badge">JavaScript</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Survey Forms Builder
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #667eea;">📋 Survey Forms Builder</h3>
        <p><strong>Technologies:</strong> Django, Django REST Framework, PostgreSQL</p>
        <p style="line-height: 1.6;">
            Developed an enterprise-grade survey management platform during Workcohol internship. 
            The system features scalable RESTful APIs, complex database relationships, and comprehensive 
            admin panel with role-based access control.
        </p>
        <ul>
            <li>Built scalable RESTful APIs with Django REST Framework</li>
            <li>Implemented complex database relationships for dynamic survey structures</li>
            <li>Created comprehensive admin panel with data analytics dashboard</li>
            <li>Designed role-based access control and user management system</li>
        </ul>
        <a href="https://github.com/Saiyashwanth7/Survey-form-builder" target="_blank" class="demo-button">📁 GitHub</a>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">Django</span>
            <span class="skill-badge">REST API</span>
            <span class="skill-badge">PostgreSQL</span>
            <span class="skill-badge">Admin Panel</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Deco-AR
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #667eea;">🏡 Deco-AR: AR Interior Designer</h3>
        <p><strong>Technologies:</strong> Unity, AR Foundation, C#, Mobile Development</p>
        <p style="line-height: 1.6;">
            Developed a cross-platform AR application for furniture visualization with <strong>95% positional accuracy</strong>. 
            The app features advanced plane detection, surface tracking using SLAM algorithms, and intuitive 
            user interface with real-time customization capabilities.
        </p>
        <ul>
            <li>Implemented SLAM algorithms for realistic object placement</li>
            <li>Created intuitive UI with furniture catalog and rotation controls</li>
            <li>Ensured 99% feature parity across iOS and Android platforms</li>
            <li>Optimized performance for smooth AR experience</li>
        </ul>
        <a href="https://drive.google.com/file/d/1lNwQ1RU8ALzyM7A1JkIkcvTP1KBn7QQ1/view" target="_blank" class="demo-button">DecoAR</a>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">Unity</span>
            <span class="skill-badge">AR Foundation</span>
            <span class="skill-badge">C#</span>
            <span class="skill-badge">SLAM</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # FastAPI Library Management
    st.markdown("""
    <div class="project-card">
        <h3 style="color: #667eea;">📚 FastAPI Library Management System</h3>
        <p><strong>Technologies:</strong> FastAPI, Python, Pydantic, REST API</p>
        <p style="line-height: 1.6;">
            Built a comprehensive RESTful API using FastAPI with complete CRUD operations. 
            The system features advanced Pydantic models, efficient filtering, and production-ready 
            API design with proper error handling and validation.
        </p>
        <ul>
            <li>Implemented advanced Pydantic models with field validation</li>
            <li>Built efficient filtering and search endpoints</li>
            <li>Designed production-ready API with proper HTTP status codes</li>
            <li>Created comprehensive exception management system</li>
        </ul>
        <a href="https://github.com/Saiyashwanth7" target="_blank" class="demo-button">📁 GitHub</a>
        <div style="margin-top: 1rem;">
            <span class="skill-badge">FastAPI</span>
            <span class="skill-badge">Pydantic</span>
            <span class="skill-badge">REST API</span>
            <span class="skill-badge">Python</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
<h4 style='color: #D4AF37;'>🔧 Backend Development</h4>
<div style="margin-bottom: 2rem;">
    <span class="skill-badge">Django</span>
    <span class="skill-badge">FastAPI</span>
    <span class="skill-badge">Flask</span>
    <span class="skill-badge">RESTful APIs</span>
    <span class="skill-badge">Async Programming</span>
</div>
<h4 style="color: #667eea;">🗄️ Databases</h4>
            <div style="margin-bottom: 2rem;">
                <span class="skill-badge">MySQL</span>
                <span class="skill-badge">PostgreSQL</span>
                <span class="skill-badge">MongoDB</span>
                <span class="skill-badge">Database Design</span>
                <span class="skill-badge">Query Optimization</span>
            </div>
<h4 style="color: #667eea;">🛠️ Tools & Platforms</h4>
<div>
    <span class="skill-badge">Git/GitHub</span>
    <span class="skill-badge">Docker (Learning)</span>
    <span class="skill-badge">Cloud Deployment</span>
    <span class="skill-badge">Unity</span>
    <span class="skill-badge">AR Foundation</span>
</div>

""", unsafe_allow_html=True)

        st.markdown("""
        
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h4 style="color: #667eea;">🎨 Frontend & Integration</h4>
            <div style="margin-bottom: 2rem;">
                <span class="skill-badge">Streamlit</span>
                <span class="skill-badge">HTML/CSS</span>
                <span class="skill-badge">API Integration</span>
                <span class="skill-badge">Responsive Design</span>
            </div>
            
        <h4 style="color: #667eea;">🗄️ Databases</h4>
            <div style="margin-bottom: 2rem;">
                <span class="skill-badge">MySQL</span>
                <span class="skill-badge">PostgreSQL</span>
                <span class="skill-badge">MongoDB</span>
                <span class="skill-badge">Database Design</span>
                <span class="skill-badge">Query Optimization</span>
            </div>
            
        """, unsafe_allow_html=True)
    
    #st.markdown("""
    #<div class="profile-section" style="margin-top: 2rem;">
    #    <h4 style="color: #667eea;">🎯 Specializations</h4>
    #    <div style="text-align: center;">
    #   <span class="skill-badge" style="font-size: 1rem; padding: 0.7rem 1.5rem;">Natural Language Processing</span>
    #        <span class="skill-badge" style="font-size: 1rem; padding: 0.7rem 1.5rem;">Computer Vision</span>
    #        <span class="skill-badge" style="font-size: 1rem; padding: 0.7rem 1.5rem;">Mobile AR Development</span>
    #        <span class="skill-badge" style="font-size: 1rem; padding: 0.7rem 1.5rem;">Full-Stack Development</span>
    #    </div>
    #</div>
    #""", unsafe_allow_html=True)
    
with tab5:
    st.markdown('<h2 class="section-header">Get In Touch</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <h4 style="color: #667eea; text-align: center;">📞 Contact Information</h4>
            <div class="contact-info">
                <p><strong>📧 Email:</strong> saiyashwanthdasari@gmail.com</p>
                <p><strong>📱 Phone:</strong> +91 9701149281</p>
                <p><strong>📍 Location:</strong> Hyderabad, India</p>
            </div>
            
        <h4 style="color: #667eea; text-align: center; margin-top: 2rem;">🌐 Social Links</h4>
            <div style="text-align: center; margin-top: 1rem;">
                <a href="https://www.linkedin.com/in/sai-yashwanth-dasari-bb381b252/" target="_blank" class="demo-button">
                    💼 LinkedIn
                </a>
                <a href="https://github.com/Saiyashwanth7" target="_blank" class="demo-button">
                    🐱 GitHub
                </a>
                <a href="#" target="_blank" class="demo-button">
                    🧠 LeetCode
                </a>
            </div>
        
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <h4 style="color: #667eea; text-align: center;">🚀 Featured Demos</h4>
        <div style="text-align: center;">
            <a href="https://altibbemedical.streamlit.app/" target="_blank" class="demo-button">
                🏥 Medical AI Chatbot
                </a>
                <a href="https://projectz-8x7k.onrender.com/" target="_blank" class="demo-button">
                    🤖 Multimodal Chatbot
                </a>
            </div>
            
        <h4 style="color: #667eea; text-align: center; margin-top: 2rem;">🎓 Education</h4>
            <div class="contact-info">
                <p><strong>J.B. Institute of Engineering and Technology</strong></p>
                <p>B.Tech in AI & Machine Learning</p>
                <p>CGPA: 7.88/10.0 (2021-2025)</p>
                <p>Hyderabad, India</p>
            </div>
        
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="profile-section" style="margin-top: 2rem;">
        <h4 style="color: #667eea; text-align: center;">🏆 Achievements & Activities</h4>
        <div style="text-align: center;">
            <p style="font-size: 1.1rem; line-height: 1.8;">
                ✅ <strong>200+ DSA Problems</strong> solved on LeetCode and coding platforms<br>
                ✅ <strong>Active participant</strong> in multiple hackathons and coding competitions<br>
                ✅ <strong>Research Publication</strong> - Authored paper accepted at IHCI 2023 (Couldn't publish the camers ready copy)<br>
                ✅ <strong>Open Source Contributor</strong> - Regular contributions to Python web development projects<br>
                ✅ <strong>Production Deployments</strong> - Multiple live applications serving users
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="
    text-align: center; 
    margin-top: 3rem; 
    padding: 2rem; 
    background: #111; 
    border-top: 1px solid #D4AF37;
    color: #fff;
">
    <p style="margin: 0; font-size: 1.1rem; color: #D4AF37;">
        🚀 <strong>Ready to build something amazing together?</strong>
    </p>
    <p style="margin-top: 0.5rem; font-size: 1rem; color: #ccc;">
        Let's connect and discuss your next project!
    </p>
</div>
""", unsafe_allow_html=True)
