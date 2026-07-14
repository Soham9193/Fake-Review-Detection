import streamlit as st

st.set_page_config(
    page_title="Fake Review Detection",
    page_icon="🛒",
    layout="wide"
)

# ==========================
# Custom CSS
# ==========================

st.markdown("""
<style>

.big-title{
    font-size:46px;
    font-weight:700;
    color:white;
}

.sub-title{
    font-size:22px;
    color:#4da3ff;
    font-weight:600;
}

.desc{
    color:#B8BCC8;
    font-size:17px;
}

.metric-box{
    background-color:#1d2330;
    border-radius:15px;
    padding:20px;
    text-align:center;
    border:1px solid #31394b;
}

.metric-title{
    color:#9aa4b3;
    font-size:15px;
}

.metric-value{
    font-size:28px;
    font-weight:bold;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# Hero Section
# ==========================

st.markdown(
"""
<div class='big-title'>
🛒 Fake Product Review Detection System
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='sub-title'>
Detect Fake Product Reviews using Machine Learning
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class='desc'>
Analyze individual reviews or entire CSV files using an NLP-based Machine Learning model.
Generate interactive analytics, confidence scores and downloadable reports in seconds.
</div>
""",
unsafe_allow_html=True
)

st.write("")
st.divider()

# ==========================
# Statistics
# ==========================

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Accuracy</div>
        <div class="metric-value">73.48%</div>
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Algorithm</div>
        <div class="metric-value">Logistic Regression</div>
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Vectorizer</div>
        <div class="metric-value">TF-IDF</div>
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-title">Dataset</div>
        <div class="metric-value">Amazon Reviews</div>
    </div>
    """,unsafe_allow_html=True)

st.divider()

# ======================================================
# FEATURE MODULES
# ======================================================

st.markdown(
"""
<h2 style='text-align:center;'>
🚀 Application Modules
</h2>
""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")

# ------------------ Card 1 ------------------

with col1:

    st.markdown("""
    <div style="
        background:#1d2330;
        padding:25px;
        border-radius:15px;
        border-left:6px solid #00C853;
        margin-bottom:20px;
    ">
    <h3>✍️ Single Review Prediction</h3>

    Predict whether an individual review is
    <b>Genuine</b> or <b>Fake</b> instantly.

    <br><br>

    ✅ Instant Prediction<br>
    ✅ Confidence Score<br>
    ✅ Cleaned Review
    </div>
    """, unsafe_allow_html=True)

# ------------------ Card 2 ------------------

with col2:

    st.markdown("""
    <div style="
        background:#1d2330;
        padding:25px;
        border-radius:15px;
        border-left:6px solid #2979FF;
        margin-bottom:20px;
    ">
    <h3>📂 Bulk CSV Prediction</h3>

    Upload a CSV containing hundreds of
    product reviews.

    <br><br>

    ✅ Batch Prediction<br>
    ✅ CSV Download<br>
    ✅ Progress Tracking
    </div>
    """, unsafe_allow_html=True)

# ------------------ Second Row ------------------

col3, col4 = st.columns(2, gap="large")

with col3:

    st.markdown("""
    <div style="
        background:#1d2330;
        padding:25px;
        border-radius:15px;
        border-left:6px solid #AA00FF;
        margin-bottom:20px;
    ">
    <h3>📊 Analytics Dashboard</h3>

    Visualize prediction results with
    interactive charts.

    <br><br>

    ✅ Pie Chart<br>
    ✅ Word Cloud<br>
    ✅ Confidence Analysis
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div style="
        background:#1d2330;
        padding:25px;
        border-radius:15px;
        border-left:6px solid #FF6D00;
        margin-bottom:20px;
    ">
    <h3>🕘 Prediction History</h3>

    View previously generated
    prediction results.

    <br><br>

    ✅ Latest Results<br>
    ✅ Download CSV<br>
    ✅ Prediction Summary
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================================================
# WORKFLOW & SYSTEM STATUS
# ======================================================

left, right = st.columns([2, 1], gap="large")

# ---------------- Workflow ----------------

with left:

    st.subheader("⚙️ How It Works")

    st.markdown(
    """
<div style="
background:#1d2330;
padding:25px;
border-radius:15px;
text-align:center;
font-size:22px;
">

📝 Review

⬇️

🧹 Cleaning

⬇️

📚 TF-IDF

⬇️

🤖 ML Model

⬇️

✅ Prediction

</div>
""",
    unsafe_allow_html=True
    )

# ---------------- Status ----------------

with right:

    st.subheader("🟢 System Status")

    st.success("Model Loaded")

    st.success("Application Ready")

    st.success("Prediction Module Ready")

    st.success("Analytics Ready")

    st.info("Dataset: Amazon Reviews")

st.divider()

# ======================================================
# PROJECT INFORMATION
# ======================================================

st.subheader("ℹ️ Project Information")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Version", "1.0")

with c2:
    st.metric("Language", "Python")

with c3:
    st.metric("Framework", "Streamlit")

st.divider()

st.caption(
    "🛒 Fake Product Review Detection System | Built using Python, Streamlit, Scikit-learn and NLP"
)

