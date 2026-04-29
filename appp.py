import streamlit as st
from backend import predict_match, get_best_player

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="IPL Predictor",
    page_icon="🏏",
    layout="centered"
)

# =====================
# CUSTOM CSS
# =====================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

/* Main container */
.block-container {
    background: white;
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
}

/* Title */
h1 {
    text-align: center;
    color: #ffffff;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #eeeeee;
    margin-bottom: 20px;
}

/* Labels */
label {
    font-weight: 600 !important;
    color: #2c3e50 !important;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #ff7e5f, #feb47b);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    border: none;
    width: 100%;
}

/* Result cards */
.result-box {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================
st.title("🏏 IPL Match Predictor")

st.markdown(
    "<div class='subtitle'>Predict match outcomes & top player using Machine Learning</div>",
    unsafe_allow_html=True
)

# =====================
# INPUTS
# =====================
teams = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    "Delhi Capitals",
    "Sunrisers Hyderabad",
    "Punjab Kings",
    "Rajasthan Royals"
]

venues = [
    "Wankhede Stadium",
    "M Chinnaswamy Stadium",
    "Eden Gardens",
    "Feroz Shah Kotla",
    "Rajiv Gandhi International Stadium",
    "MA Chidambaram Stadium",
    "Punjab Cricket Association Stadium",
    "Sawai Mansingh Stadium",
    "Narendra Modi Stadium",
    "Brabourne Stadium",
    "DY Patil Stadium"
]

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Team 1", teams)

with col2:
    team2 = st.selectbox("Team 2", teams)

col3, col4 = st.columns(2)

with col3:
    toss_winner = st.selectbox("Toss Winner", teams)

with col4:
    toss_decision = st.selectbox("Toss Decision", ["bat", "field"])

# ✅ FIXED VENUE INPUT
venue = st.selectbox("Select Venue", venues)

st.markdown(" ")

# =====================
# BUTTON
# =====================
if st.button("Predict Match 🚀"):

    if team1 == team2:
        st.warning("⚠️ Please select two different teams")
    else:
        winner = predict_match(
            team1,
            team2,
            toss_winner,
            toss_decision,
            venue
        )

        # ✅ FIXED PLAYER LOGIC CALL
        player = get_best_player(team1, team2)

        # =====================
        # RESULTS
        # =====================
        st.markdown("### 🏆 Prediction Results")

        st.markdown(
            f"""
            <div class="result-box">
                <h3>🏆 Winner</h3>
                <h2 style="color:#2ecc71;">{winner}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-box">
                <h3>🌟 Player of the Match</h3>
                <h2 style="color:#e67e22;">{player}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
