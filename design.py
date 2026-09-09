import streamlit as st


def setup_page():
    st.set_page_config(
        page_title="Premier League Analytics",
        page_icon="⚽",
        layout="wide"
    )

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(125, 70, 190, 0.20),
                transparent 38%
            ),
            #08080d;

        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1rem;
        padding-bottom: 4rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* HERO */

    .hero {
        position: relative;
        text-align: center;

        padding: 80px 20px 95px;

        animation: heroEnter 1s ease-out;
    }


    /* Glow behind hero */

    .hero::before {
        content: "";

        position: absolute;

        width: 500px;
        height: 500px;

        left: 50%;
        top: 0;

        transform: translateX(-50%);

        background: rgba(130, 65, 210, 0.12);

        filter: blur(100px);

        pointer-events: none;
    }


    /* Football / logo placeholder */

    .hero-mark {
        position: relative;

        width: 105px;
        height: 105px;

        margin: 0 auto 30px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        background:
            radial-gradient(
                circle at 35% 30%,
                rgba(180, 130, 255, 0.35),
                rgba(100, 50, 160, 0.08)
            );

        border: 1px solid rgba(180, 120, 255, 0.35);

        box-shadow:
            0 0 50px rgba(140, 70, 220, 0.25),
            inset 0 0 30px rgba(150, 80, 230, 0.12);

        font-size: 45px;

        animation: floatingMark 4s ease-in-out infinite;
    }


    /* Main heading */

    .hero-title {
        position: relative;

        margin: 0;

        font-size: clamp(3.5rem, 8vw, 6rem);

        font-weight: 800;

        letter-spacing: -0.065em;

        line-height: 0.95;

        background:
            linear-gradient(
                135deg,
                #ffffff 15%,
                #e4d6ff 55%,
                #a467ff 100%
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    /* Subtitle */

    .hero-subtitle {
        position: relative;

        margin-top: 24px;

        color: #a9a9b5;

        font-size: 1.15rem;

        font-weight: 400;

        letter-spacing: 0.01em;
    }


    /* Small technology label */

    .hero-tag {
        position: relative;

        display: inline-block;

        margin-top: 28px;

        padding: 9px 18px;

        border-radius: 999px;

        border: 1px solid rgba(170, 110, 240, 0.3);

        background: rgba(120, 70, 180, 0.08);

        color: #c8a9ff;

        font-size: 0.72rem;

        font-weight: 600;

        letter-spacing: 0.12em;
    }


    /* Animations */

    @keyframes heroEnter {

        from {
            opacity: 0;
            transform: translateY(25px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }

    }


    @keyframes floatingMark {

        0%, 100% {
            transform: translateY(0);
        }

        50% {
            transform: translateY(-8px);
        }

    }

    </style>
    """, unsafe_allow_html=True)

def hero():

    # Football visual
    st.markdown(
        """
        <div style="
            width:105px;
            height:105px;
            margin:80px auto 30px auto;
            border-radius:50%;
            display:flex;
            align-items:center;
            justify-content:center;
            background:rgba(120,70,180,0.15);
            border:1px solid rgba(180,120,255,0.35);
            box-shadow:0 0 50px rgba(140,70,220,0.25);
            font-size:45px;
        ">
            ⚽
        </div>
        """,
        unsafe_allow_html=True
    )

    # Hero text
    st.markdown(
        "<h1 style='text-align:center; font-size:64px; font-weight:800; color:white;'>Premier League</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; color:#c8a9ff; font-size:12px; letter-spacing:2px;'>MACHINE LEARNING · MATCH INTELLIGENCE</p>",
        unsafe_allow_html=True
    )

    #Predictor

def predictor_header():
    st.markdown(
        "<p style='text-align:center; color:#c8a9ff; "
        "font-size:12px; font-weight:700; letter-spacing:2px;'>"
        "AI MATCH PREDICTOR</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h2 style='text-align:center; color:white;'>"
        "Match Analysis</h2>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; color:#888894;'>"
        "Compare team performance and predict the outcome.</p>",
        unsafe_allow_html=True
    )

