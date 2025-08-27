import streamlit as st
from streamlit_option_menu import option_menu
from login import show_login_page

st.set_page_config(page_title="GT Auradata", layout="wide")

# Supprimer la barre de défilement de la sidebar
st.markdown("""
    <style>
        /* Cacher le scroll dans la sidebar */
        [data-testid="stSidebar"] > div:first-child {
            overflow-y: hidden;
        }
            
        /* Appliquer un hover uniquement sur les éléments non vides */
        .nav-link:has(span:not(:empty)):hover {
            background-color: blue !important;
            cursor: pointer;
        }

        /* Ne rien faire sur les éléments vides (les séparateurs) */
        .nav-link:has(span:empty):hover {
            background-color: transparent !important;
            cursor: default;
        }
    </style>
""", unsafe_allow_html=True)


# Vérifie si l'utilisateur est connecté
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    show_login_page()

else:
    with st.sidebar:
        #st.image("assets/logo.png", width=150)
        col1, col2, col3 = st.columns([0.5, 2, 0.5])
        with col2:
            st.image("assets/logo.png", width=130)

        st.markdown("<div style='flex:1;></div>", unsafe_allow_html=True)
        selected = option_menu(
            "",
            ["Dashboard", "Feuille de temps", "Demande d'absence", "Validation absence", "Validation feuille","","","","","Administration", "Déconnexion"],
            icons=["bar-chart", "clock", "file-earmark-text", "check-circle", "check-square","\u200b","\u200b","\u200b","\u200b", "gear","box-arrow-right"],
            menu_icon="none",
            styles={
                "container": {
                    "background-color": "transparent",
                    "width":"230px",
                    "padding": "0px",
                    "margin": "0px",
                },
                "nav-link": {
                    "font-size": "14px",
                    "font-family": "Segoe UI",
                    "text-align": "left",
                    "padding": "10px",
                    "margin": "0px",
                    "color": "#333333",
                },
                "nav-link-selected": {
                    "background-color": "#080686",
                    "color": "white",
                    "font-weight": "bold",
                },
            }
        )

    if selected == "Dashboard":
        import dashboard
        dashboard.show_dashboard()

    elif selected == "Feuille de temps":
        import feuille_temps
        feuille_temps.show_feuille_temps()

    elif selected == "Demande d'absence":
        import demande_absence
        demande_absence.show_demande_absence()
    
    elif selected == "Validation absence":
        import validation_absence
        validation_absence.show_validation_absence()

    elif selected == "Validation feuille":
        import validation_feuille
        validation_feuille.show_validation_feuille()

    elif selected == "Administration":
        import admin
        admin.show_admin()

    elif selected == "Déconnexion":
        st.session_state.logged_in = False
        st.rerun()

