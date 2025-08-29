import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Cartographie des Initiatives Citoyennes Urbaines",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #A23B72;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E86AB;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #A23B72;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Chargement et préparation des données"""
    df = pd.read_csv('data_fictives_augmentees.csv')
    df['Date_Lancement'] = pd.to_datetime(df['Date_Lancement'])
    df['Mois_Lancement'] = df['Date_Lancement'].dt.month
    df['Saison'] = df['Mois_Lancement'].map({
        12: 'Hiver', 1: 'Hiver', 2: 'Hiver',
        3: 'Printemps', 4: 'Printemps', 5: 'Printemps',
        6: 'Été', 7: 'Été', 8: 'Été',
        9: 'Automne', 10: 'Automne', 11: 'Automne'
    })
    return df

def create_overview_metrics(df):
    """Création des métriques de vue d'ensemble"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Initiatives", len(df))
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        success_rate = (df['Statut'] == 'Réussi').mean() * 100
        st.metric("Taux de Réussite", f"{success_rate:.0f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Villes Couvertes", df['Localisation_Ville'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Types d'Initiatives", df['Type_Initiative'].nunique())
        st.markdown('</div>', unsafe_allow_html=True)

def create_type_distribution(df):
    """Graphique de répartition des types d'initiatives"""
    type_counts = df['Type_Initiative'].value_counts()
    percentages = (type_counts / len(df) * 100).round(1)
    
    fig = px.bar(
        x=type_counts.values,
        y=type_counts.index,
        orientation='h',
        title="Répartition des Types d'Initiatives",
        labels={'x': 'Nombre d\'initiatives', 'y': 'Type d\'initiative'},
        color=type_counts.values,
        color_continuous_scale='viridis'
    )
    
    # Ajout des pourcentages
    for i, (count, pct) in enumerate(zip(type_counts.values, percentages.values)):
        fig.add_annotation(
            x=count + 0.5,
            y=i,
            text=f"{pct}%",
            showarrow=False,
            font=dict(size=12, color="black")
        )
    
    fig.update_layout(
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig

def create_temporal_analysis(df):
    """Analyse temporelle des initiatives"""
    # Évolution par année
    yearly_counts = df['Année'].value_counts().sort_index()
    
    fig_yearly = px.line(
        x=yearly_counts.index,
        y=yearly_counts.values,
        title="Évolution du Nombre d'Initiatives par Année",
        labels={'x': 'Année', 'y': 'Nombre d\'initiatives'},
        markers=True
    )
    
    fig_yearly.update_traces(
        line=dict(color='#2E86AB', width=3),
        marker=dict(size=8, color='#A23B72')
    )
    
    fig_yearly.update_layout(height=400)
    
    # Répartition saisonnière
    season_counts = df['Saison'].value_counts()
    
    fig_season = px.pie(
        values=season_counts.values,
        names=season_counts.index,
        title="Répartition Saisonnière des Lancements",
        color_discrete_sequence=['#2E86AB', '#A23B72', '#F18F01', '#C73E1D']
    )
    
    fig_season.update_layout(height=400)
    
    return fig_yearly, fig_season

def create_geographic_analysis(df):
    """Analyse géographique"""
    # Top 10 des villes
    city_counts = df['Localisation_Ville'].value_counts().head(10)
    
    fig_cities = px.bar(
        x=city_counts.values,
        y=city_counts.index,
        orientation='h',
        title="Top 10 des Villes par Nombre d'Initiatives",
        labels={'x': 'Nombre d\'initiatives', 'y': 'Ville'},
        color=city_counts.values,
        color_continuous_scale='plasma'
    )
    
    fig_cities.update_layout(
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    # Top 10 des quartiers
    district_counts = df['Localisation_Quartier'].value_counts().head(10)
    
    fig_districts = px.bar(
        x=district_counts.values,
        y=district_counts.index,
        orientation='h',
        title="Top 10 des Quartiers par Nombre d'Initiatives",
        labels={'x': 'Nombre d\'initiatives', 'y': 'Quartier'},
        color=district_counts.values,
        color_continuous_scale='viridis'
    )
    
    fig_districts.update_layout(
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig_cities, fig_districts

def create_impact_analysis(df):
    """Analyse des impacts"""
    # Matrice de corrélation impact social vs environnemental
    impact_cross = pd.crosstab(df['Impact_Social_Perçu'], df['Impact_Environnemental_Perçu'])
    
    fig_heatmap = px.imshow(
        impact_cross.values,
        x=impact_cross.columns,
        y=impact_cross.index,
        title="Corrélation Impact Social vs Impact Environnemental",
        labels={'x': 'Impact Environnemental', 'y': 'Impact Social'},
        color_continuous_scale='RdYlBu_r',
        text_auto=True
    )
    
    fig_heatmap.update_layout(height=400)
    
    # Taux de réussite par type d'initiative
    success_by_type = df.groupby('Type_Initiative')['Statut'].apply(
        lambda x: (x == 'Réussi').mean() * 100
    ).sort_values(ascending=True)
    
    fig_success = px.bar(
        x=success_by_type.values,
        y=success_by_type.index,
        orientation='h',
        title="Taux de Réussite par Type d'Initiative",
        labels={'x': 'Taux de réussite (%)', 'y': 'Type d\'initiative'},
        color=success_by_type.values,
        color_continuous_scale='RdYlGn'
    )
    
    # Ajout des pourcentages
    for i, rate in enumerate(success_by_type.values):
        fig_success.add_annotation(
            x=rate + 1,
            y=i,
            text=f"{rate:.1f}%",
            showarrow=False,
            font=dict(size=12, color="black")
        )
    
    fig_success.update_layout(
        height=400,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'}
    )
    
    return fig_heatmap, fig_success

def create_interactive_map(df):
    """Création de la carte interactive"""
    # Utilisation des coordonnées originales pour la vraie géolocalisation
    m = folium.Map(
        location=[46.5, 2.5],  # Centre de la France
        zoom_start=6,
        tiles='OpenStreetMap'
    )
    
    # Couleurs par type d'initiative
    type_colors = {
        'Fresque Murale Participative': 'red',
        'Jardin Partagé': 'green',
        'Composteur de Quartier': 'brown',
        'Boîte à Livres': 'blue',
        'Repair Café': 'orange',
        'Événement de Quartier': 'purple'
    }
    
    # Ajout des marqueurs
    for _, row in df.iterrows():
        color = type_colors.get(row['Type_Initiative'], 'gray')
        
        # Icône selon le statut
        icon = 'check' if row['Statut'] == 'Réussi' else 'hourglass' if row['Statut'] == 'En cours' else 'remove'
        
        folium.Marker(
            location=[row['Coordonnees_Latitude'], row['Coordonnees_Longitude']],
            popup=folium.Popup(f"""
                <b>{row['Nom_Initiative']}</b><br>
                Type: {row['Type_Initiative']}<br>
                Ville: {row['Localisation_Ville']}<br>
                Quartier: {row['Localisation_Quartier']}<br>
                Statut: {row['Statut']}<br>
                Impact Social: {row['Impact_Social_Perçu']}<br>
                Impact Environnemental: {row['Impact_Environnemental_Perçu']}<br>
                Participants: {row['Nb_Participants_Estime']}<br>
                Date: {row['Date_Lancement'].strftime('%d/%m/%Y')}
            """, max_width=300),
            tooltip=row['Nom_Initiative'],
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(m)
    
    # Légende
    legend_html = '''
    <div style="position: fixed; 
                bottom: 50px; left: 50px; width: 200px; height: 180px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:14px; padding: 10px">
    <p><b>Types d'Initiatives</b></p>
    <p><i class="fa fa-circle" style="color:red"></i> Fresque Murale</p>
    <p><i class="fa fa-circle" style="color:green"></i> Jardin Partagé</p>
    <p><i class="fa fa-circle" style="color:brown"></i> Composteur</p>
    <p><i class="fa fa-circle" style="color:blue"></i> Boîte à Livres</p>
    <p><i class="fa fa-circle" style="color:orange"></i> Repair Café</p>
    <p><i class="fa fa-circle" style="color:purple"></i> Événement</p>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    return m

def main():
    """Fonction principale de l'application"""
    # En-tête
    st.markdown('<h1 class="main-header">🏙️ Cartographie Interactive des Initiatives Citoyennes Urbaines</h1>', unsafe_allow_html=True)
    
    # Chargement des données
    df = load_data()
    
    # Sidebar pour les filtres
    st.sidebar.header("🔍 Filtres")
    
    # Filtres
    selected_cities = st.sidebar.multiselect(
        "Sélectionner les villes",
        options=sorted(df['Localisation_Ville'].unique()),
        default=sorted(df['Localisation_Ville'].unique())
    )
    
    selected_types = st.sidebar.multiselect(
        "Sélectionner les types d'initiatives",
        options=sorted(df['Type_Initiative'].unique()),
        default=sorted(df['Type_Initiative'].unique())
    )
    
    selected_status = st.sidebar.multiselect(
        "Sélectionner les statuts",
        options=sorted(df['Statut'].unique()),
        default=sorted(df['Statut'].unique())
    )
    
    # Application des filtres
    filtered_df = df[
        (df['Localisation_Ville'].isin(selected_cities)) &
        (df['Type_Initiative'].isin(selected_types)) &
        (df['Statut'].isin(selected_status))
    ]
    
    # Métriques de vue d'ensemble
    st.markdown('<h2 class="section-header">📊 Vue d\'Ensemble</h2>', unsafe_allow_html=True)
    create_overview_metrics(filtered_df)
    
    # Insights clés
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.markdown(f"""
    **💡 Insights Clés:**
    - Les **Fresques Murales Participatives** représentent le type d'initiative le plus populaire
    - **Lyon** est la ville la plus active avec {df[df['Localisation_Ville'] == 'Lyon'].shape[0]} initiatives
    - Le taux de réussite global est de **{(df['Statut'] == 'Réussi').mean() * 100:.0f}%**
    - Une croissance continue est observée de 2021 à 2024
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Analyse des types d'initiatives
    st.markdown('<h2 class="section-header">🎨 Répartition des Types d\'Initiatives</h2>', unsafe_allow_html=True)
    fig_types = create_type_distribution(filtered_df)
    st.plotly_chart(fig_types, use_container_width=True)
    
    st.markdown("""
    **Interprétation:** Les fresques murales participatives dominent le paysage des initiatives citoyennes, 
    reflétant un fort intérêt pour l'art urbain et l'expression créative collective. Les jardins partagés 
    et composteurs de quartier montrent l'importance croissante des préoccupations environnementales.
    """)
    
    # Analyse temporelle
    st.markdown('<h2 class="section-header">📅 Évolution Temporelle</h2>', unsafe_allow_html=True)
    fig_yearly, fig_season = create_temporal_analysis(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_yearly, use_container_width=True)
    with col2:
        st.plotly_chart(fig_season, use_container_width=True)
    
    st.markdown("""
    **Interprétation:** La tendance croissante montre un engouement grandissant pour les initiatives citoyennes. 
    La répartition saisonnière révèle des préférences pour certaines périodes de lancement, 
    probablement liées aux conditions météorologiques et aux cycles urbains.
    """)
    
    # Analyse géographique
    st.markdown('<h2 class="section-header">🗺️ Répartition Géographique</h2>', unsafe_allow_html=True)
    fig_cities, fig_districts = create_geographic_analysis(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_cities, use_container_width=True)
    with col2:
        st.plotly_chart(fig_districts, use_container_width=True)
    
    st.markdown("""
    **Interprétation:** Lyon, Bordeaux et Montpellier émergent comme les villes les plus dynamiques. 
    Certains quartiers comme Vieux Lyon et Neudorf concentrent plusieurs initiatives, 
    suggérant des écosystèmes locaux favorables à l'engagement citoyen.
    """)
    
    # Analyse des impacts
    st.markdown('<h2 class="section-header">🎯 Analyse des Impacts</h2>', unsafe_allow_html=True)
    fig_heatmap, fig_success = create_impact_analysis(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_heatmap, use_container_width=True)
    with col2:
        st.plotly_chart(fig_success, use_container_width=True)
    
    st.markdown("""
    **Interprétation:** La corrélation entre impacts social et environnemental révèle des synergies intéressantes. 
    Les taux de réussite variables selon les types d'initiatives suggèrent des facteurs de succès spécifiques 
    à chaque catégorie d'action citoyenne.
    """)
    
    # Carte interactive
    st.markdown('<h2 class="section-header">🗺️ Cartographie Interactive</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    **Instructions:** Cliquez sur les marqueurs pour voir les détails de chaque initiative. 
    Les couleurs représentent les types d'initiatives, les icônes indiquent le statut.
    """)
    
    map_obj = create_interactive_map(filtered_df)
    st_folium(map_obj, width=700, height=500)
    
    # Conclusions
    st.markdown('<h2 class="section-header">🎯 Conclusions et Recommandations</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="insight-box">', unsafe_allow_html=True)
    st.markdown("""
    **🔍 Principales Observations:**
    
    1. **Diversité des Initiatives:** Six types d'initiatives couvrent un large spectre d'actions citoyennes
    2. **Dynamisme Urbain:** Concentration dans les grandes métropoles françaises
    3. **Tendance Positive:** Croissance continue du nombre d'initiatives
    4. **Taux de Réussite Élevé:** 63% des initiatives aboutissent avec succès
    
    **📈 Recommandations:**
    
    - **Capitaliser sur les Succès:** Reproduire les modèles d'initiatives les plus réussies
    - **Développer les Synergies:** Encourager les projets à double impact (social + environnemental)
    - **Soutenir les Quartiers Actifs:** Renforcer l'accompagnement dans les zones déjà dynamiques
    - **Étendre la Couverture:** Développer les initiatives dans les villes moins représentées
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem;">
        📊 Analyse réalisée sur des données fictives <br>
        🎯 Compétences en Data Visualisation et Storytelling
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

