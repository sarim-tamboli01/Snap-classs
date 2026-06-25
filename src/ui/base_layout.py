import streamlit as st


_DIALOG_TOAST_TEXT_CSS = """
    /* Dialog inner panel (not the dimmed overlay) */
    [data-testid="stDialog"] {
        background: transparent !important;
        box-shadow: none !important;
    }

    [data-testid="stDialog"] div[role="dialog"] {
        background-color: #FFFFFF !important;
        color: #1e293b !important;
        border-radius: 1rem !important;
        box-shadow: 0 20px 60px rgba(30, 41, 59, 0.18) !important;
    }

    /* All dialog text: upload photos, voice attendance, etc. */
    [data-testid="stDialog"] div[role="dialog"] p,
    [data-testid="stDialog"] div[role="dialog"] span,
    [data-testid="stDialog"] div[role="dialog"] label,
    [data-testid="stDialog"] div[role="dialog"] h1,
    [data-testid="stDialog"] div[role="dialog"] h2,
    [data-testid="stDialog"] div[role="dialog"] h3,
    [data-testid="stDialog"] div[role="dialog"] h4,
    [data-testid="stDialog"] div[role="dialog"] li,
    [data-testid="stDialog"] div[role="dialog"] small,
    [data-testid="stDialog"] [data-testid="stMarkdownContainer"],
    [data-testid="stDialog"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stDialog"] [data-testid="stMarkdownContainer"] span,
    [data-testid="stDialog"] [data-testid="stMarkdownContainer"] li,
    [data-testid="stDialog"] [data-testid="stWidgetLabel"] p,
    [data-testid="stDialog"] [data-testid="stWidgetLabel"] label,
    [data-testid="stDialog"] [data-testid="stWidgetLabel"] span,
    [data-testid="stDialog"] [data-testid="stFileUploader"] label,
    [data-testid="stDialog"] [data-testid="stFileUploader"] p,
    [data-testid="stDialog"] [data-testid="stFileUploader"] span,
    [data-testid="stDialog"] [data-testid="stFileUploader"] small,
    [data-testid="stDialog"] [data-testid="stFileUploader"] section,
    [data-testid="stDialog"] [data-testid="stCameraInput"] label,
    [data-testid="stDialog"] [data-testid="stCameraInput"] p,
    [data-testid="stDialog"] [data-testid="stCameraInput"] span,
    [data-testid="stDialog"] [data-testid="stAudioInput"] label,
    [data-testid="stDialog"] [data-testid="stAudioInput"] p,
    [data-testid="stDialog"] [data-testid="stAudioInput"] span,
    [data-testid="stDialog"] [data-testid="stSpinner"] p,
    [data-testid="stDialog"] [data-testid="stSpinner"] span,
    [data-testid="stDialog"] [data-testid="stText"],
    [data-testid="stDialog"] [data-testid="stAlert"] p,
    [data-testid="stDialog"] [data-testid="stAlert"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stDialog"] [data-testid="stFileUploader"] *:not(button):not(button *),
    [data-testid="stDialog"] [data-testid="stCameraInput"] *:not(button):not(button *),
    [data-testid="stDialog"] [data-testid="stAudioInput"] *:not(button):not(button *) {
        color: #1e293b !important;
    }

    /* Dialog title bar */
    [data-testid="stDialog"] div[role="dialog"] > div:first-child,
    [data-testid="stDialog"] div[role="dialog"] > div:first-child *:not(button):not(button *) {
        color: #1e293b !important;
    }

    /* Dialog buttons (portaled outside .stApp) */
    [data-testid="stDialog"] button[kind="primary"],
    [data-testid="stDialog"] button[kind="primary"] p,
    [data-testid="stDialog"] button[kind="primary"] span {
        background-color: #5865F2 !important;
        color: #FFFFFF !important;
    }

    [data-testid="stDialog"] button[kind="secondary"],
    [data-testid="stDialog"] button[kind="secondary"] p,
    [data-testid="stDialog"] button[kind="secondary"] span {
        background-color: #EB459E !important;
        color: #FFFFFF !important;
    }

    [data-testid="stDialog"] button[kind="tertiary"],
    [data-testid="stDialog"] button[kind="tertiary"] p,
    [data-testid="stDialog"] button[kind="tertiary"] span {
        background-color: #FFFFFF !important;
        color: #1e293b !important;
        border-color: #c7cce8 !important;
    }

    /* Toast notifications */
    [data-testid="stToast"] {
        background-color: #FFFFFF !important;
        color: #1e293b !important;
    }

    [data-testid="stToast"] p,
    [data-testid="stToast"] span,
    [data-testid="stToast"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stToast"] [data-testid="stMarkdownContainer"] span {
        color: #1e293b !important;
    }

    [data-testid="stToastViewButton"] {
        color: #5865F2 !important;
    }
"""


def style_background_home():

    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(160deg, #5865F2 0%, #4752C4 100%) !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #FFFFFF !important;
                padding: 2.5rem !important;
                border-radius: 1.25rem !important;
                box-shadow: 0 8px 32px rgba(30, 41, 59, 0.12) !important;
                border: 1px solid rgba(255, 255, 255, 0.6) !important;
            }

            .stApp,
            .stApp [data-testid="stMarkdownContainer"] p,
            .stApp [data-testid="stHeader"] h1,
            .stApp [data-testid="stHeader"] h2 {
                color: #FFFFFF !important;
            }

            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2,
            .stApp div[data-testid="stColumn"] h3,
            .stApp div[data-testid="stColumn"] p,
            .stApp div[data-testid="stColumn"] [data-testid="stHeader"] h1,
            .stApp div[data-testid="stColumn"] [data-testid="stHeader"] h2,
            .stApp div[data-testid="stColumn"] [data-testid="stMarkdownContainer"] p {
                color: #1e293b !important;
            }

            /* Home column buttons keep readable labels */
            .stApp div[data-testid="stColumn"] .stButton > button[kind="primary"] p,
            .stApp div[data-testid="stColumn"] .stButton > button[kind="primary"] span,
            .stApp div[data-testid="stColumn"] button[kind="primary"] p,
            .stApp div[data-testid="stColumn"] button[kind="primary"] span {
                color: #FFFFFF !important;
            }
        </style>
        """
        , unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }

            .stApp input,
            .stApp textarea,
            .stApp [data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                border: 1px solid #c7cce8 !important;
                border-radius: 0.5rem !important;
            }

            [data-testid="stDialog"] {
                background: transparent !important;
            }

            .stApp,
            .stApp [data-testid="stAppViewContainer"] {
                color: #1e293b !important;
            }

            .stApp [data-testid="stHeader"] h1,
            .stApp [data-testid="stHeader"] h2,
            .stApp [data-testid="stHeader"] h3,
            .stApp [data-testid="stMarkdownContainer"] p,
            .stApp [data-testid="stMarkdownContainer"] li,
            .stApp [data-testid="stWidgetLabel"] p,
            .stApp [data-testid="stText"],
            .stApp .stCaption,
            .stApp input,
            .stApp textarea,
            .stApp [data-baseweb="select"] > div,
            [data-testid="stDialog"] p,
            [data-testid="stDialog"] h1,
            [data-testid="stDialog"] h2,
            [data-testid="stDialog"] h3,
            [data-testid="stDialog"] [data-testid="stMarkdownContainer"] p,
            [data-testid="stDataFrame"] {
                color: #1e293b !important;
            }

            /* Buttons must not inherit dashboard text color */
            .stApp .stButton > button[kind="primary"],
            .stApp .stButton > button[kind="primary"] p,
            .stApp .stButton > button[kind="primary"] span,
            .stApp button[kind="primary"],
            .stApp button[kind="primary"] p,
            .stApp button[kind="primary"] span {
                color: #FFFFFF !important;
            }

            .stApp .stButton > button[kind="secondary"],
            .stApp .stButton > button[kind="secondary"] p,
            .stApp .stButton > button[kind="secondary"] span,
            .stApp button[kind="secondary"],
            .stApp button[kind="secondary"] p,
            .stApp button[kind="secondary"] span {
                color: #FFFFFF !important;
            }

            .stApp .stButton > button[kind="tertiary"],
            .stApp .stButton > button[kind="tertiary"] p,
            .stApp .stButton > button[kind="tertiary"] span,
            .stApp button[kind="tertiary"],
            .stApp button[kind="tertiary"] p,
            .stApp button[kind="tertiary"] span {
                color: #1e293b !important;
            }

            .stApp .stCaption {
                color: #64748b !important;
            }

            """ + _DIALOG_TOAST_TEXT_CSS + """
        </style>
        """
        , unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        :root {
            --sc-primary: #5865F2;
            --sc-primary-hover: #4752C4;
            --sc-secondary: #EB459E;
            --sc-secondary-hover: #d63d8c;
            --sc-danger: #DC2626;
            --sc-danger-hover: #B91C1C;
            --sc-text: #1e293b;
            --sc-text-muted: #64748b;
            --sc-white: #FFFFFF;
            --sc-border: #c7cce8;
            --sc-radius: 0.75rem;
        }

        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 2rem !important;
            max-width: 1100px !important;
        }

        /* ── Typography ── */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            letter-spacing: -0.02em !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 1 !important;
            margin-bottom: 0.25rem !important;
            letter-spacing: -0.01em !important;
        }

        h3, h4 {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
        }

        p, li, label {
            font-family: 'Outfit', sans-serif !important;
            line-height: 1.6 !important;
        }

        /* Alerts: keep Streamlit colors readable */
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] [data-testid="stMarkdownContainer"] p {
            color: inherit !important;
        }

        /* ── Buttons: shared shell ── */
        .stApp .stButton > button,
        .stApp [data-testid="stButton"] > button,
        .stApp button[kind],
        .stApp [data-testid="stBaseButton-primary"],
        .stApp [data-testid="stBaseButton-secondary"],
        .stApp [data-testid="stBaseButton-tertiary"],
        .stApp [data-testid="baseButton-primary"],
        .stApp [data-testid="baseButton-secondary"],
        .stApp [data-testid="baseButton-tertiary"] {
            border-radius: var(--sc-radius) !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            padding: 0.6rem 1.25rem !important;
            border: 2px solid transparent !important;
            transition: background-color 0.2s ease, color 0.2s ease,
                        border-color 0.2s ease, box-shadow 0.2s ease,
                        transform 0.15s ease !important;
            letter-spacing: 0.01em !important;
        }

        /* ── Primary ── */
        .stApp .stButton > button[kind="primary"],
        .stApp [data-testid="stButton"] > button[kind="primary"],
        .stApp button[kind="primary"],
        .stApp [data-testid="stBaseButton-primary"],
        .stApp [data-testid="baseButton-primary"] {
            background-color: var(--sc-primary) !important;
            color: var(--sc-white) !important;
            border-color: var(--sc-primary) !important;
            box-shadow: 0 2px 8px rgba(88, 101, 242, 0.35) !important;
        }

        .stApp .stButton > button[kind="primary"] p,
        .stApp .stButton > button[kind="primary"] span,
        .stApp .stButton > button[kind="primary"] div,
        .stApp button[kind="primary"] p,
        .stApp button[kind="primary"] span,
        .stApp button[kind="primary"] div,
        .stApp [data-testid="stBaseButton-primary"] p,
        .stApp [data-testid="stBaseButton-primary"] span,
        .stApp [data-testid="baseButton-primary"] p,
        .stApp [data-testid="baseButton-primary"] span {
            color: var(--sc-white) !important;
        }

        .stApp .stButton > button[kind="primary"]:hover,
        .stApp button[kind="primary"]:hover,
        .stApp [data-testid="stBaseButton-primary"]:hover,
        .stApp [data-testid="baseButton-primary"]:hover {
            background-color: var(--sc-primary-hover) !important;
            border-color: var(--sc-primary-hover) !important;
            box-shadow: 0 4px 14px rgba(88, 101, 242, 0.45) !important;
            transform: translateY(-1px) !important;
        }

        /* ── Secondary ── */
        .stApp .stButton > button[kind="secondary"],
        .stApp [data-testid="stButton"] > button[kind="secondary"],
        .stApp button[kind="secondary"],
        .stApp [data-testid="stBaseButton-secondary"],
        .stApp [data-testid="baseButton-secondary"] {
            background-color: var(--sc-secondary) !important;
            color: var(--sc-white) !important;
            border-color: var(--sc-secondary) !important;
            box-shadow: 0 2px 8px rgba(235, 69, 158, 0.3) !important;
        }

        .stApp .stButton > button[kind="secondary"] p,
        .stApp .stButton > button[kind="secondary"] span,
        .stApp .stButton > button[kind="secondary"] div,
        .stApp button[kind="secondary"] p,
        .stApp button[kind="secondary"] span,
        .stApp button[kind="secondary"] div,
        .stApp [data-testid="stBaseButton-secondary"] p,
        .stApp [data-testid="stBaseButton-secondary"] span,
        .stApp [data-testid="baseButton-secondary"] p,
        .stApp [data-testid="baseButton-secondary"] span {
            color: var(--sc-white) !important;
        }

        .stApp .stButton > button[kind="secondary"]:hover,
        .stApp button[kind="secondary"]:hover,
        .stApp [data-testid="stBaseButton-secondary"]:hover,
        .stApp [data-testid="baseButton-secondary"]:hover {
            background-color: var(--sc-secondary-hover) !important;
            border-color: var(--sc-secondary-hover) !important;
            box-shadow: 0 4px 14px rgba(235, 69, 158, 0.4) !important;
            transform: translateY(-1px) !important;
        }

        /* ── Tertiary: neutral ghost (tabs, unenroll, clear) ── */
        .stApp .stButton > button[kind="tertiary"],
        .stApp [data-testid="stButton"] > button[kind="tertiary"],
        .stApp button[kind="tertiary"],
        .stApp [data-testid="stBaseButton-tertiary"],
        .stApp [data-testid="baseButton-tertiary"] {
            background-color: var(--sc-white) !important;
            color: var(--sc-text) !important;
            border-color: var(--sc-border) !important;
            box-shadow: none !important;
        }

        .stApp .stButton > button[kind="tertiary"] p,
        .stApp .stButton > button[kind="tertiary"] span,
        .stApp .stButton > button[kind="tertiary"] div,
        .stApp button[kind="tertiary"] p,
        .stApp button[kind="tertiary"] span,
        .stApp button[kind="tertiary"] div,
        .stApp [data-testid="stBaseButton-tertiary"] p,
        .stApp [data-testid="stBaseButton-tertiary"] span,
        .stApp [data-testid="baseButton-tertiary"] p,
        .stApp [data-testid="baseButton-tertiary"] span {
            color: var(--sc-text) !important;
        }

        .stApp .stButton > button[kind="tertiary"]:hover,
        .stApp button[kind="tertiary"]:hover,
        .stApp [data-testid="stBaseButton-tertiary"]:hover,
        .stApp [data-testid="baseButton-tertiary"]:hover {
            background-color: #f8fafc !important;
            border-color: var(--sc-primary) !important;
            color: var(--sc-primary) !important;
            box-shadow: 0 2px 8px rgba(88, 101, 242, 0.15) !important;
            transform: translateY(-1px) !important;
        }

        .stApp .stButton > button[kind="tertiary"]:hover p,
        .stApp .stButton > button[kind="tertiary"]:hover span,
        .stApp .stButton > button[kind="tertiary"]:hover div,
        .stApp button[kind="tertiary"]:hover p,
        .stApp button[kind="tertiary"]:hover span,
        .stApp [data-testid="stBaseButton-tertiary"]:hover p,
        .stApp [data-testid="stBaseButton-tertiary"]:hover span,
        .stApp [data-testid="baseButton-tertiary"]:hover p,
        .stApp [data-testid="baseButton-tertiary"]:hover span {
            color: var(--sc-primary) !important;
        }

        /* Dialog buttons inherit same rules */
        [data-testid="stDialog"] .stButton > button[kind="primary"] p,
        [data-testid="stDialog"] .stButton > button[kind="primary"] span,
        [data-testid="stDialog"] button[kind="primary"] p,
        [data-testid="stDialog"] button[kind="primary"] span {
            color: var(--sc-white) !important;
        }

        [data-testid="stDialog"] .stButton > button[kind="secondary"] p,
        [data-testid="stDialog"] .stButton > button[kind="secondary"] span,
        [data-testid="stDialog"] button[kind="secondary"] p,
        [data-testid="stDialog"] button[kind="secondary"] span {
            color: var(--sc-white) !important;
        }

        [data-testid="stDialog"] .stButton > button[kind="tertiary"] p,
        [data-testid="stDialog"] .stButton > button[kind="tertiary"] span,
        [data-testid="stDialog"] button[kind="tertiary"] p,
        [data-testid="stDialog"] button[kind="tertiary"] span {
            color: var(--sc-text) !important;
        }

        /* Material icons inside buttons follow button text color */
        .stApp button[kind="primary"] [data-testid="stIconMaterial"],
        .stApp button[kind="secondary"] [data-testid="stIconMaterial"],
        .stApp .stButton > button[kind="primary"] [data-testid="stIconMaterial"],
        .stApp .stButton > button[kind="secondary"] [data-testid="stIconMaterial"] {
            color: var(--sc-white) !important;
        }

        .stApp button[kind="tertiary"] [data-testid="stIconMaterial"],
        .stApp .stButton > button[kind="tertiary"] [data-testid="stIconMaterial"] {
            color: var(--sc-text) !important;
        }

        .stApp button[kind="tertiary"]:hover [data-testid="stIconMaterial"],
        .stApp .stButton > button[kind="tertiary"]:hover [data-testid="stIconMaterial"] {
            color: var(--sc-primary) !important;
        }

        """ + _DIALOG_TOAST_TEXT_CSS + """
        </style>
        """
        , unsafe_allow_html=True)
