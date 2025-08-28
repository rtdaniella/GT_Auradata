import streamlit as st

def show_guide_utilisateur():
    # CSS pour le style
    st.markdown("""
        <style>
            .stApp {
                margin-top: 0;
                padding: 0;
                background-color: #f9f9f9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }

            .guide-title {
                color: #006633;
                font-size: 30px;
                font-weight: bold;
                margin-bottom: 15px;
                text-align: center;
            }
            .stTabs [data-baseweb="tab"] {
                font-size: 20px !important;
                font-weight: 600 !important;
                padding: 10px 20px !important;
                font-size: 30px !important;
            }

            .guide-subtitle {
                color: #004d00;
                font-size: 24px;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 10px;
            }

            .guide-step-container {
                background-color: #ffffff;
                padding: 15px;
                border-radius: 12px;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
                margin-bottom: 15px;
                font-size: 16px;
                display: flex;
                align-items: flex-start;
            }

            .guide-step-number {
                display: inline-block;
                width: 35px;
                height: 35px;
                line-height: 35px;
                text-align: center;
                background-color: #006633;
                color: white;
                border-radius: 50%;
                font-weight: bold;
                margin-right: 15px;
                flex-shrink: 0;
            }

            .guide-step-text {
                flex-grow: 1;
            }
            .block-container {
                padding-top: 1.5rem !important;
                margin-top: 0 !important;
            }
                    
            .main .block-container {
                margin-top: 0rem !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="guide-title">Guide d’utilisation de l’application</div>', unsafe_allow_html=True)

    # Tabs utilisateur / admin
    tab1, tab2 = st.tabs(["Utilisateur", "Admin / RH"])

    # ------------------ UTILISATEUR ------------------
    with tab1:
        st.markdown('<div class="guide-subtitle">I. Demande d’absence</div>', unsafe_allow_html=True)
        steps = [
            "Aller dans le menu latéral et cliquer sur <b>'Demande d’absence'</b>.",
            "Remplir le formulaire et ajouter un justificatif si nécessaire (ex: arrêt maladie).",
            "Soumettre la demande et attendre la validation."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">II. Feuille de temps</div>', unsafe_allow_html=True)
        steps = [
            "Aller dans <b>'Feuille de temps'</b> > <b>'Saisie feuille de temps'</b>.",
            "Choisir le mois et l’année (le mois en cours est affiché par défaut).",
            "Remplir les jours travaillés (1 ou 0.5) et enregistrer la feuille.",
            "Modifier ou soumettre la feuille pour validation si nécessaire."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">III. Gestion de projets</div>', unsafe_allow_html=True)
        steps = [
            "Choisir le mois et remplir le tableau semaine par semaine selon les heures travaillées.",
            "Enregistrer et exporter en Excel si nécessaire.",
            "Visualiser la répartition des heures via le graphique."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">IV. Historique</div>', unsafe_allow_html=True)
        steps = [
            "Consulter toutes vos demandes et feuilles soumises.",
            "Filtrer par année et statut, exporter en Excel et voir les motifs de refus."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

    # ------------------ ADMIN / RH ------------------
    with tab2:
        st.markdown('<div class="guide-subtitle">I. Administration</div>', unsafe_allow_html=True)
        steps = [
            "Onglet <b>'Utilisateurs'</b> : ajouter ou modifier un utilisateur, importer un fichier Excel, activer/désactiver un compte.",
            "Onglet <b>'Projets'</b> : ajouter ou modifier un projet, affichage des projets dans le tableau.",
            "Onglet <b>'Attributions des projets'</b> : ajouter/modifier les attributions, affichage dans le tableau.",
            "Onglet <b>'Définition CP & RTT'</b> : saisir ou modifier les nombres annuels."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">II. Validation des absences</div>', unsafe_allow_html=True)
        steps = [
            "Onglet <b>'Demandes en attente'</b> : valider ou rejeter les demandes, saisir les motifs de refus si nécessaire.",
            "Onglet <b>'Historique'</b> : consulter toutes les demandes, filtrer et exporter."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">III. Validation des feuilles de temps</div>', unsafe_allow_html=True)
        steps = [
            "Onglet <b>'Feuilles en attente'</b> : valider ou rejeter les feuilles.",
            "Onglet <b>'Validation heures'</b> : modifier ou filtrer les heures saisies.",
            "Onglet <b>'Historique'</b> : consulter toutes les feuilles avec leur statut et filtres."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="guide-subtitle">IV. Dashboard</div>', unsafe_allow_html=True)
        steps = [
            "Onglet <b>'Temps de travail'</b> : KPIs et analyses des heures travaillées.",
            "Onglet <b>'Absence'</b> : KPIs avec sous-onglets <b>'Absence de la semaine'</b> et <b>'Analyse avancée'</b>.",
            "Onglet <b>'Projets'</b> : KPIs, suivi de l’avancement et analyses détaillées."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"""
                <div class="guide-step-container">
                    <span class="guide-step-number">{i}</span>
                    <span class="guide-step-text">{step}</span>
                </div>
            """, unsafe_allow_html=True)
