import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configuration pour l'affichage français
plt.rcParams['font.family'] = 'DejaVu Sans'

# Chargement des données
df = pd.read_csv('data_fictives_augmentees.csv')

print("=== ANALYSE EXPLORATOIRE DES DONNÉES ===\n")

# Informations générales
print("1. INFORMATIONS GÉNÉRALES")
print(f"Nombre de lignes: {len(df)}")
print(f"Nombre de colonnes: {len(df.columns)}")
print(f"Colonnes: {list(df.columns)}")
print()

# Types de données
print("2. TYPES DE DONNÉES")
print(df.dtypes)
print()

# Valeurs manquantes
print("3. VALEURS MANQUANTES")
print(df.isnull().sum())
print()

# Statistiques descriptives pour les colonnes numériques
print("4. STATISTIQUES DESCRIPTIVES")
numeric_cols = df.select_dtypes(include=[np.number]).columns
print(df[numeric_cols].describe())
print()

# Analyse des colonnes catégorielles
print("5. ANALYSE DES VARIABLES CATÉGORIELLES")

print("\nTypes d'initiatives:")
print(df['Type_Initiative'].value_counts())

print("\nVilles:")
print(df['Localisation_Ville'].value_counts())

print("\nQuartiers (top 10):")
print(df['Localisation_Quartier'].value_counts().head(10))

print("\nStatuts:")
print(df['Statut'].value_counts())

print("\nImpact Social:")
print(df['Impact_Social_Perçu'].value_counts())

print("\nImpact Environnemental:")
print(df['Impact_Environnemental_Perçu'].value_counts())

print("\nAnnées:")
print(df['Année'].value_counts().sort_index())

# Conversion de la date
df['Date_Lancement'] = pd.to_datetime(df['Date_Lancement'])
print(f"\nPériode couverte: {df['Date_Lancement'].min()} à {df['Date_Lancement'].max()}")

# Analyse des coordonnées
print("\n6. ANALYSE GÉOGRAPHIQUE")
print(f"Latitude min/max: {df['Coordonnees_Latitude'].min():.4f} / {df['Coordonnees_Latitude'].max():.4f}")
print(f"Longitude min/max: {df['Coordonnees_Longitude'].min():.4f} / {df['Coordonnees_Longitude'].max():.4f}")

# Vérification des coordonnées lat/lon supplémentaires
if 'lat' in df.columns and 'lon' in df.columns:
    print(f"Lat (colonne lat) min/max: {df['lat'].min():.4f} / {df['lat'].max():.4f}")
    print(f"Lon (colonne lon) min/max: {df['lon'].min():.4f} / {df['lon'].max():.4f}")

print("\n=== ANALYSE TERMINÉE ===")

