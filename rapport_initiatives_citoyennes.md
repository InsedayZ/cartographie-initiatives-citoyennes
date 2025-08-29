# Cartographie Interactive des Initiatives Citoyennes Urbaines et de leur Impact

## Rapport d'Analyse - Data Visualisation & Storytelling

---

## 1. Introduction

### Contexte du Projet

Ce projet s'inscrit dans une démarche d'analyse des initiatives citoyennes en se basant sur le jeu de données et les graphiques fournis. L'engagement citoyen dans les espaces urbains représente un enjeu majeur de notre époque, où les habitants cherchent à reprendre possession de leur environnement quotidien à travers des initiatives locales et participatives.

Les initiatives citoyennes urbaines constituent un phénomène en pleine expansion, reflétant une volonté croissante des citoyens de s'impliquer activement dans l'amélioration de leur cadre de vie. Ces actions, qu'elles soient artistiques, environnementales ou sociales, témoignent d'une transformation profonde des modes de participation démocratique et d'appropriation de l'espace public.

### Objectif du Rapport

L'objectif de ce rapport est de présenter une analyse exploratoire des initiatives citoyennes urbaines à travers des données fictives, en utilisant les outils modernes de data visualisation et de storytelling. Cette analyse vise à :

- Identifier les patterns et tendances dans les initiatives citoyennes urbaines
- Analyser la répartition géographique et temporelle de ces initiatives
- Évaluer l'impact social et environnemental perçu de ces actions
- Proposer des insights data-driven pour orienter les politiques publiques

### Nature du Projet

Il s'agit d'un **"proof of concept"** démontrant mes compétences en data visualisation et storytelling. Ce projet illustre ma capacité à :

- Analyser des jeux de données complexes
- Créer des visualisations interactives et engageantes
- Développer des applications web de data visualisation
- Interpréter les données dans un contexte sociologique et urbain
- Communiquer des insights de manière claire et accessible

---

## 2. Méthodologie et Jeu de Données

### Source des Données

Les données utilisées dans cette analyse sont **fictives** et ont été créées spécifiquement pour ce projet de démonstration. Elles simulent un recensement d'initiatives citoyennes urbaines dans 10 grandes villes françaises sur la période 2020-2024.

### Structure du Dataset

Le jeu de données `data_fictives_augmentees.csv` contient **100 initiatives** décrites par **19 variables** :

**Variables d'identification :**
- `ID_Initiative` : Identifiant unique
- `Nom_Initiative` : Nom descriptif de l'initiative

**Variables de catégorisation :**
- `Type_Initiative` : 6 types (Fresque Murale, Jardin Partagé, Composteur, Boîte à Livres, Repair Café, Événement de Quartier)
- `Statut` : État d'avancement (Réussi, En cours, Abandonné)

**Variables géographiques :**
- `Localisation_Ville` : 10 villes françaises
- `Localisation_Quartier` : Quartiers spécifiques
- `Coordonnees_Latitude` / `Coordonnees_Longitude` : Géolocalisation précise

**Variables temporelles :**
- `Date_Lancement` : Date de début de l'initiative
- `Année` : Année de lancement

**Variables d'impact :**
- `Impact_Social_Perçu` : Évaluation qualitative (Faible, Moyen, Fort, Très Fort)
- `Impact_Environnemental_Perçu` : Évaluation qualitative (Faible, Moyen, Fort, Très Fort)

**Variables complémentaires :**
- `Nb_Participants_Estime` : Nombre de participants
- `Budget` : Budget alloué (uniforme à 150 000€)
- `Mots_Cles_Associes` : Tags descriptifs
- `Source_Info` : Source de l'information

### Processus d'Obtention des Données

Dans un contexte réel, ce type de données pourrait être obtenu par :

1. **Collecte institutionnelle** : Partenariats avec les mairies et collectivités locales
2. **Crowdsourcing** : Plateforme participative de recensement citoyen
3. **Veille numérique** : Monitoring des réseaux sociaux et sites web associatifs
4. **Enquêtes terrain** : Investigations directes dans les quartiers
5. **APIs ouvertes** : Exploitation des données publiques disponibles

---

## 3. Outil de Visualisation Développé

### Architecture Technique

L'application de visualisation a été développée avec **Streamlit**, un framework Python permettant de créer rapidement des applications web interactives pour la data science. Cette solution offre :

- **Simplicité de développement** : Code Python pur, sans HTML/CSS/JavaScript
- **Interactivité native** : Widgets et filtres intégrés
- **Visualisations avancées** : Intégration Plotly et Folium
- **Déploiement facile** : Application web accessible via navigateur

### Fonctionnalités Implémentées

L'application propose plusieurs niveaux d'analyse :

1. **Dashboard de synthèse** : Métriques clés et insights principaux
2. **Filtres interactifs** : Sélection par ville, type d'initiative et statut
3. **Visualisations multiples** : Graphiques en barres, courbes temporelles, heatmaps
4. **Cartographie interactive** : Géolocalisation des initiatives avec pop-ups informatifs
5. **Analyses croisées** : Corrélations entre variables d'impact

---


## 4. Analyse et Visualisations

### 4.1 Vue d'Ensemble du Dashboard

![Dashboard Overview](https://cartographie-initiatives-citoyennes.streamlit.app)

**Figure 1 : Interface principale de l'application de visualisation**

L'interface principale présente un dashboard épuré avec des métriques clés immédiatement visibles. La sidebar à gauche propose des filtres interactifs permettant une exploration personnalisée des données.

**Métriques Clés Identifiées :**
- **100 initiatives** recensées au total
- **63% de taux de réussite** - un indicateur encourageant de l'efficacité des initiatives citoyennes
- **10 villes couvertes** - représentant un échantillon diversifié du territoire français
- **6 types d'initiatives** - couvrant un large spectre d'actions citoyennes

### 4.2 Répartition des Types d'Initiatives

**Description de la Visualisation :**
La Figure 1 montre un graphique en barres horizontales présentant la distribution des six types d'initiatives. Les barres sont triées par ordre décroissant et incluent les pourcentages pour faciliter la lecture.

**Interprétation des Résultats :**

Les **Fresques Murales Participatives** dominent le paysage avec 22% des initiatives, révélant un fort engouement pour l'art urbain et l'expression créative collective. Cette prédominance s'explique par plusieurs facteurs :

- **Accessibilité** : Peu de compétences techniques requises
- **Visibilité** : Impact immédiat et durable dans l'espace public
- **Fédération** : Capacité à rassembler des profils diversifiés
- **Expression** : Réponse au besoin d'appropriation créative de l'espace urbain

Les **Jardins Partagés** (19%) et **Composteurs de Quartier** (18%) occupent une place significative, témoignant de la montée des préoccupations environnementales et du désir de reconnexion avec la nature en milieu urbain.

Les **Boîtes à Livres** (18%) illustrent l'importance accordée à la culture accessible et au partage de connaissances, s'inscrivant dans une logique d'économie circulaire culturelle.

### 4.3 Évolution Temporelle des Initiatives

**Description de la Visualisation :**
Deux graphiques complémentaires analysent la dimension temporelle : une courbe d'évolution annuelle et un diagramme circulaire de répartition saisonnière.

**Interprétation des Résultats :**

**Tendance Annuelle (2020-2024) :**
- **Croissance continue** : De 18 initiatives en 2021 à 26 en 2024
- **Accélération récente** : Pic d'activité en 2024 avec 26 initiatives
- **Résilience** : Maintien de la dynamique malgré les contraintes sanitaires

Cette progression témoigne d'un **engouement grandissant** pour l'engagement citoyen local, possiblement amplifié par :
- La prise de conscience écologique post-COVID
- Le besoin de lien social après les confinements
- L'émergence de nouveaux outils numériques facilitant l'organisation

**Répartition Saisonnière :**
- **Printemps** (28%) : Saison privilégiée, coïncidant avec le renouveau naturel
- **Automne** (26%) : Période de rentrée et de nouveaux projets
- **Été** (25%) : Profite des vacances et du temps libre
- **Hiver** (21%) : Période moins favorable mais non négligeable

### 4.4 Analyse Géographique

**Description de la Visualisation :**
Deux graphiques en barres horizontales présentent le classement des villes et quartiers les plus actifs.

**Interprétation des Résultats :**

**Dynamisme Urbain :**
- **Lyon** (14 initiatives) émerge comme la ville la plus dynamique
- **Bordeaux** et **Montpellier** (13 chacune) suivent de près
- **Lille** (12) et **Paris** (10) complètent le top 5

Cette hiérarchie révèle des **écosystèmes urbains favorables** caractérisés par :
- Des politiques municipales encourageantes
- Une densité associative importante
- Des espaces publics propices aux initiatives
- Une culture participative développée

**Concentration Quartiers :**
Certains quartiers comme **Vieux Lyon**, **Neudorf** et **Capucins** (6 initiatives chacun) concentrent l'activité, suggérant :
- Des **effets de cluster** : les initiatives s'attirent mutuellement
- Des **territoires catalyseurs** : conditions locales particulièrement favorables
- Des **réseaux d'acteurs** : communautés engagées et organisées

### 4.5 Analyse des Impacts

**Description de la Visualisation :**
Une heatmap de corrélation croise les impacts sociaux et environnementaux, tandis qu'un graphique en barres présente les taux de réussite par type d'initiative.

**Interprétation des Résultats :**

**Corrélation Impact Social vs Environnemental :**
La matrice révèle des **synergies intéressantes** :
- Les initiatives à fort impact social tendent vers un impact environnemental élevé
- Peu d'initiatives présentent un impact faible sur les deux dimensions
- Les **jardins partagés** et **composteurs** excellent sur les deux aspects

**Taux de Réussite par Type :**
- **Boîtes à Livres** (83.3%) : Simplicité de mise en œuvre et maintenance
- **Fresques Murales** (81.8%) : Projets bien délimités dans le temps
- **Événements de Quartier** (72.7%) : Animation ponctuelle moins complexe
- **Jardins Partagés** (36.8%) : Projets plus complexes nécessitant un suivi long terme

Ces variations suggèrent des **facteurs de succès spécifiques** :
- **Complexité organisationnelle** : Plus elle est faible, plus le taux de réussite est élevé
- **Durée d'engagement** : Les projets ponctuels réussissent mieux que les projets permanents
- **Compétences requises** : Les initiatives techniques sont plus risquées

### 4.6 Cartographie Interactive

**Description de la Visualisation :**
Une carte interactive de la France localise précisément chaque initiative avec des marqueurs colorés par type et des icônes indiquant le statut.

**Interprétation des Résultats :**

La cartographie révèle :
- **Concentration métropolitaine** : Focus sur les grandes agglomérations
- **Diversité géographique** : Couverture de différentes régions françaises
- **Clusters locaux** : Regroupements d'initiatives dans certaines zones
- **Accessibilité de l'information** : Pop-ups détaillés pour chaque initiative

Cette visualisation permet une **approche territoriale** de l'analyse, essentielle pour :
- Identifier les zones d'intervention prioritaires
- Comprendre les dynamiques locales
- Adapter les politiques aux spécificités territoriales

---


## 5. Insights Clés et Storytelling

### 5.1 Narrative Principale : L'Émergence d'une Citoyenneté Active

Les données révèlent une **transformation profonde** de l'engagement citoyen urbain. Nous assistons à l'émergence d'une nouvelle forme de participation démocratique, caractérisée par :

**L'Art comme Vecteur d'Appropriation :**
La prédominance des fresques murales participatives (22%) illustre le rôle central de l'expression artistique dans la reconquête de l'espace public. Ces initiatives transcendent les clivages sociaux et offrent un langage universel pour l'engagement citoyen.

**L'Écologie comme Moteur de Mobilisation :**
Avec 37% des initiatives (jardins partagés + composteurs), l'environnement constitue le second pilier de l'engagement. Cette tendance reflète l'urgence climatique et le besoin de solutions concrètes à l'échelle locale.

**La Culture comme Bien Commun :**
Les boîtes à livres (18%) témoignent d'une volonté de démocratisation culturelle et de création de liens sociaux autour du partage de connaissances.

### 5.2 Patterns Comportementaux Identifiés

**Saisonnalité de l'Engagement :**
Le pic printanier (28%) révèle une corrélation entre cycles naturels et dynamiques citoyennes. Cette saisonnalité suggère des stratégies de communication et d'accompagnement adaptées aux rythmes urbains.

**Géographie de l'Innovation Sociale :**
La concentration dans certaines métropoles (Lyon, Bordeaux, Montpellier) et quartiers spécifiques révèle l'existence d'**écosystèmes favorables** qu'il convient d'étudier et de reproduire.

**Facteurs de Réussite Différenciés :**
Les variations de taux de réussite selon les types d'initiatives (36.8% à 83.3%) soulignent l'importance d'adapter l'accompagnement aux spécificités de chaque projet.

---

## 6. Recommandations Stratégiques

### 6.1 Pour les Collectivités Locales

**Capitaliser sur les Succès :**
- Développer des **programmes d'accompagnement spécialisés** pour les boîtes à livres et fresques murales (taux de réussite > 80%)
- Créer des **kits méthodologiques** reproductibles pour faciliter l'essaimage

**Soutenir les Initiatives Complexes :**
- Renforcer l'accompagnement des jardins partagés par des **formations techniques** et un **suivi long terme**
- Développer des **partenariats avec les associations spécialisées** en permaculture urbaine

**Optimiser la Couverture Territoriale :**
- Identifier et reproduire les **facteurs de succès** des quartiers les plus dynamiques
- Développer des **stratégies d'essaimage** vers les territoires moins couverts

### 6.2 Pour les Porteurs de Projets

**Timing Optimal :**
- Privilégier les **lancements printaniers** pour maximiser l'engagement
- Anticiper les **cycles saisonniers** dans la planification des activités

**Approche Collaborative :**
- Rechercher les **synergies entre impacts** social et environnemental
- Développer des **projets hybrides** combinant plusieurs dimensions

**Stratégie de Pérennisation :**
- Adapter la **complexité organisationnelle** aux ressources disponibles
- Prévoir des **mécanismes de transition** pour les projets à long terme

### 6.3 Pour les Chercheurs et Analystes

**Approfondissement des Analyses :**
- Étudier les **corrélations entre budget et impact** (données uniformes dans ce dataset)
- Analyser les **réseaux d'acteurs** et effets de cluster géographiques
- Investiguer les **facteurs socio-économiques** influençant la réussite

**Méthodologie d'Évaluation :**
- Développer des **indicateurs quantitatifs d'impact** complémentaires aux évaluations qualitatives
- Créer des **outils de suivi longitudinal** pour mesurer la pérennité des initiatives

---

## 7. Limites et Perspectives

### 7.1 Limites de l'Analyse Actuelle

**Nature Fictive des Données :**
Cette analyse repose sur des données simulées qui, bien que réalistes, ne reflètent pas la complexité du terrain réel. Une validation empirique serait nécessaire.

**Uniformité Budgétaire :**
Le budget uniforme de 150 000€ par initiative limite l'analyse de l'efficience économique et des modèles de financement.

**Période d'Observation :**
La fenêtre temporelle 2020-2024 ne permet pas d'analyser les cycles longs et les effets de génération dans l'engagement citoyen.

### 7.2 Perspectives d'Amélioration

**Enrichissement des Données :**
- Intégrer des **variables socio-économiques** (revenus, éducation, âge des participants)
- Ajouter des **métriques d'impact quantifiées** (m² d'espaces créés, kg de déchets traités, etc.)
- Inclure des **données de coût réel** et sources de financement

**Analyses Avancées :**
- Développer des **modèles prédictifs** de réussite des initiatives
- Implémenter des **analyses de réseaux** pour comprendre les dynamiques collaboratives
- Créer des **tableaux de bord temps réel** pour le pilotage des politiques publiques

**Dimension Participative :**
- Intégrer les **retours d'expérience** des porteurs de projets
- Développer des **outils de co-création** avec les citoyens
- Créer une **plateforme collaborative** de partage d'expériences

---

## 8. Conclusion

### 8.1 Apports de cette Analyse

Ce projet démontre la **puissance du storytelling data-driven** pour éclairer les enjeux sociétaux contemporains. L'application développée illustre comment les outils modernes de visualisation peuvent transformer des données brutes en insights actionnables pour les décideurs publics et les acteurs de terrain.

### 8.2 Compétences Démontrées

Cette réalisation met en évidence plusieurs compétences clés :

**Techniques :**
- Maîtrise des outils de data science (Python, Pandas, Plotly, Streamlit)
- Développement d'applications web interactives
- Création de visualisations engageantes et informatives

**Analytiques :**
- Analyse exploratoire de données complexes
- Identification de patterns et corrélations significatives
- Interprétation contextuelle des résultats

**Communication :**
- Storytelling efficace avec les données
- Adaptation du discours aux différents publics
- Synthèse d'insights actionnables

### 8.3 Impact Potentiel

Dans un contexte réel, ce type d'analyse pourrait contribuer à :
- **Optimiser les politiques publiques** de soutien à l'engagement citoyen
- **Améliorer l'efficacité** des programmes d'accompagnement
- **Favoriser l'essaimage** des initiatives réussies
- **Renforcer la démocratie participative** par une meilleure compréhension des dynamiques citoyennes

---

## 9. Annexes Techniques

### 9.1 Architecture de l'Application

**Stack Technique :**
- **Backend** : Python 3.11, Streamlit 1.49.0
- **Visualisations** : Plotly Express, Folium
- **Data Processing** : Pandas, NumPy
- **Déploiement** : Application web accessible via navigateur

**Fonctionnalités Implémentées :**
- Dashboard interactif avec métriques temps réel
- Filtres dynamiques (ville, type, statut)
- Graphiques interactifs (zoom, pan, export)
- Cartographie avec géolocalisation précise
- Interface responsive et épurée

### 9.2 Reproductibilité

**Code Source :**
L'intégralité du code est documentée et structurée pour faciliter la maintenance et l'évolution. Les bonnes pratiques de développement sont respectées (fonctions modulaires, commentaires, gestion d'erreurs).

**Données :**
Le dataset est fourni au format CSV standard, facilement importable dans tout environnement d'analyse de données.

**Documentation :**
Ce rapport constitue une documentation complète permettant la reproduction et l'adaptation de l'analyse à d'autres contextes.

---

**Traduction les données en insights data-driven**   
**Outils : Python, Streamlit, Plotly, Folium**  
**Nathan.Z**