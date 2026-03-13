
import streamlit as st
import matplotlib.pyplot as plt

from modules.pdf_extractor import extract_text_from_pdf
from modules.image_extractor import extract_text_from_image
from modules.lab_analyzer import extract_lab_values
from modules.risk_calculator import analyze_labs, risk_level, reference_ranges
from modules.gemini_analyzer import generate_medical_summary
from modules.ai_lab_analyzer import extract_labs_with_ai
from modules.report_classifier import detect_report_type
from modules.radiology_analyzer import simplify_radiology
from modules.doctor_recommender import recommend_doctor
from modules.chatbot import ask_medical_chatbot

def show_main_header():
    st.markdown(
        '<p class="hero-title">Smart Medical Report Interpreter</p>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="hero-sub">Simplifying Clinical Reports for Better Health Understanding</p>',
        unsafe_allow_html=True
    )


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Smart Medical Report Interpreter",
    page_icon="🩺",
    layout="wide"
)

# ------------------------------------------------
# ADVANCED STYLING
# ------------------------------------------------

st.markdown("""
<style>

/* Remove Streamlit default padding */

.block-container {
padding-top: 3rem;
padding-bottom: 0rem;
padding-left: 3rem;
padding-right: 3rem;
}

/* Full page background */

.stApp {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
min-height:100vh;
}

/* HERO TITLE */
            
.hero-title{
font-size:60px !important;
font-weight:900 !important;
text-align:center !important;
margin-top:10px;
margin-bottom:20px;
color:#EAF6FF;
letter-spacing:1px;
line-height:1.05;
}

.hero-sub{
text-align:center;
font-size:24px;
margin-bottom:60px;
color:#cfe8ff;
}

/* SECTION HEADINGS */

.section{
font-size:34px;
font-weight:700;
margin-top:60px;
margin-bottom:20px;
color:#EAF6FF;
border-left:4px solid #38bdf8;
padding-left:10px;
}

/* NAV BUTTONS */

div.stButton > button{
background:transparent;
border:1px solid #6ab7ff;
color:white;
border-radius:25px;
height:36px;
width:150px;
transition:0.3s;
font-weight:500;
margin-top:5px;
}

div.stButton > button:hover{
background:#1f4e79;
box-shadow:0 0 14px #4fc3f7;
transform:scale(1.05);
}

/* GLASS CARDS */

.card{
background: rgba(255,255,255,0.08);
padding:35px;
border-radius:18px;
backdrop-filter: blur(12px);
box-shadow:0 6px 30px rgba(0,0,0,0.35);
text-align:center;
transition:0.3s;
}

.card:hover{
transform:translateY(-6px);
box-shadow:0 10px 40px rgba(0,0,0,0.45);
}

/* METRIC CARDS */

.metric-card{
background: rgba(255,255,255,0.10);
padding:25px;
border-radius:16px;
backdrop-filter: blur(10px);
box-shadow:0 8px 30px rgba(0,0,0,0.4);
text-align:center;
transition:0.3s;
}

.metric-card:hover{
transform:scale(1.04);
box-shadow:0 10px 35px rgba(0,0,0,0.6);
}
/* center main container */

.main{
max-width:1400px;
margin:auto;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# NAVBAR
# ------------------------------------------------

st.write("")
st.write("")
nav_space, nav1, nav2, nav3, nav4, nav5 = st.columns([6,1,1,1,1,1])

with nav1:
    if st.button("Home"):
        st.session_state.page="home"

with nav2:
    if st.button("Upload"):
        st.session_state.page="upload"

with nav3:
    if st.button("Dashboard"):
        st.session_state.page="dashboard"

with nav4:
    if st.button("Chatbot"):
        st.session_state.page="chatbot"

with nav5:
    if st.button("About"):
        st.session_state.page="about"

if "page" not in st.session_state:
    st.session_state.page="home"

page = st.session_state.page

# ------------------------------------------------
# HOME
# ------------------------------------------------

if page=="home":

    show_main_header()

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><h3>📄 Upload Reports</h3><p>Upload PDF or image medical reports</p></div>',unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>🧪 Lab Analysis</h3><p>Automatic detection of lab values</p></div>',unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>🤖 AI Explanation</h3><p>Simplified medical interpretations</p></div>',unsafe_allow_html=True)

    st.write("")

    col4,col5,col6 = st.columns(3)

    with col4:
        st.markdown('<div class="card"><h3>📊 Health Dashboard</h3></div>',unsafe_allow_html=True)

    with col5:
        st.markdown('<div class="card"><h3>👨‍⚕️ Doctor Recommendation</h3></div>',unsafe_allow_html=True)

    with col6:
        st.markdown('<div class="card"><h3>📈 Clinical Visualization</h3></div>',unsafe_allow_html=True)

    st.write("")

    if st.button("Start Analysis"):
        st.session_state.page="upload"
        st.rerun()


# ------------------------------------------------
# UPLOAD PAGE
# ------------------------------------------------

elif page=="upload":

    show_main_header()

    uploaded_file = st.file_uploader(
        "Upload PDF or Image",
        type=["pdf","png","jpg","jpeg"]
    )

    if uploaded_file:

        st.success("Report uploaded successfully")

        if "pdf" in uploaded_file.type:
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_image(uploaded_file)

        report_type = detect_report_type(text)

        st.info(f"Detected Report Type: {report_type}")

        if "radiology" in report_type.lower():

            result = simplify_radiology(text)
            st.write(result)

        else:

            labs = extract_lab_values(text)

            if len(labs)<3:
                labs = extract_labs_with_ai(text)

            findings,score = analyze_labs(labs)

            level = risk_level(score)

            doctor = recommend_doctor(findings)

            if level=="Low":
                urgency="Routine"
            elif level=="Medium":
                urgency="Consult Soon"
            else:
                urgency="Immediate"

            st.session_state.labs=labs
            st.session_state.findings=findings
            st.session_state.score=score
            st.session_state.level=level
            st.session_state.doctor=doctor
            st.session_state.urgency=urgency

            if st.button("View Dashboard"):
                st.session_state.page="dashboard"
                st.rerun()


# ------------------------------------------------
# DASHBOARD
# ------------------------------------------------

elif page=="dashboard":

    show_main_header()

    if "labs" not in st.session_state:
        st.warning("Upload a medical report first")

    else:

        labs = st.session_state.labs
        findings = st.session_state.findings
        score = st.session_state.score
        level = st.session_state.level
        doctor = st.session_state.doctor
        urgency = st.session_state.urgency


        # -----------------------------
        # METRIC CARDS
        # -----------------------------

        c1,c2,c3,c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
            <h4>Risk Level</h4>
            <h2 style='color:#4ade80'>{level}</h2>
            </div>
            """,unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
            <h4>Risk Score</h4>
            <h2 style='color:#38bdf8'>{score}</h2>
            </div>
            """,unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
            <h4>Recommended Doctor</h4>
            <h2 style='color:#60a5fa'>{doctor}</h2>
            </div>
            """,unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric-card">
            <h4>Urgency</h4>
            <h2 style='color:#f59e0b'>{urgency}</h2>
            </div>
            """,unsafe_allow_html=True)


        st.markdown("<div class='section'>Clinical Indicators</div>", unsafe_allow_html=True)


        # -----------------------------
        # CLINICAL VISUALIZATION
        # -----------------------------

        for lab in labs[:6]:

            test = lab.get("test")
            value = lab.get("value")

            if test in reference_ranges:

                low, high = reference_ranges[test]

                fig, ax = plt.subplots(figsize=(8,1.6))

                ax.barh(0, low)
                ax.barh(0, high-low, left=low)
                ax.barh(0, high, left=high)

                ax.scatter(value,0,s=250)

                ax.set_title(test)
                ax.set_yticks([])
                ax.set_xlabel("Reference Range")

                st.pyplot(fig)


        st.markdown("<div class='section'>Key Findings</div>", unsafe_allow_html=True)


        # -----------------------------
        # FINDINGS SECTION
        # -----------------------------

        for test,status,icon in findings:

            if status=="Normal":
                st.success(f"{test} : Normal")

            elif status=="Low":
                st.warning(f"{test} : Low")

            else:
                st.error(f"{test} : High")


        st.markdown("<div class='section'>Medical Explanation</div>", unsafe_allow_html=True)


        # -----------------------------
        # AI MEDICAL SUMMARY
        # -----------------------------

        try:

            summary = generate_medical_summary(str(labs))

            st.markdown(f"""
            <div class="card">
            {summary}
            </div>
            """, unsafe_allow_html=True)

        except:

            st.info("Medical explanation unavailable")


# ------------------------------------------------
# CHATBOT PAGE
# ------------------------------------------------

elif page=="chatbot":

    show_main_header()

    if "labs" not in st.session_state:

        st.warning("Upload a report first")

    else:

        # question = st.text_input("Ask a question about your report")
        question = st.text_input(
            "",
            placeholder="Ask a question about your report..."
        )

        if st.button("Ask AI"):

            answer = ask_medical_chatbot(question, st.session_state.labs)

            st.success(answer)


# ------------------------------------------------
# ABOUT PAGE
# ------------------------------------------------

elif page=="about":

    show_main_header()

    st.write("• AI system for interpreting clinical reports")
    st.write("• Extracts lab values automatically")
    st.write("• Detects abnormal health indicators")
    st.write("• Generates simplified medical explanations")
    st.write("• Recommends doctor consultation")


st.markdown("---")
st.caption("Educational AI system for medical report understanding")