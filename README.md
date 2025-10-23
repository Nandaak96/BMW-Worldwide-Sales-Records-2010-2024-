# Analyse mondiale des ventes BMW (2010–2024)

## 📌 **Contexte**
BMW  est l’un des constructeurs automobiles les plus emblématiques au monde, reconnu pour ses modèles premium et son positionnement haut de gamme.
L’objectif de ce projet est d’analyser les ventes mondiales de BMW sur la période 2010 à 2024, afin d’identifier les tendances clés en matière de modèles, de motorisations et de zones géographiques.

Ce projet s’inscrit dans une démarche analytique complète, mêlant :

    🐍 Préparation et transformation des données avec Python (VS Code)
    📊 Exploration et visualisation interactive avec Power BI
    📂 Documentation structurée sur GitHub (dans une logique de portfolio).

## 🎯 **Objectifs du projet**

- Analyser l’évolution des ventes BMW dans le monde entre 2010 et 2024.
- Identifier les modèles les plus vendus par année et par région.
- Étudier la répartition des ventes selon :

    - le type de transmission (manuelle vs automatique),
    - le type de carburant,
    - la couleur des véhicules.

- Mettre en évidence les tendances de motorisation (essence, diesel, hybride, électrique).
- Développer un dashboard Power BI interactif pour visualiser les résultats de manière intuitive.
- Documenter le process complet pour une réutilisation future ou une extension du projet.

## 🧾 **Description du dataset**

Source : [Kaggle — BMW Worldwide Sales Records 2010–2024](https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024)

Nombre de lignes : 50 000

Période couverte : 2010 à 2024

Format : CSV

Dictionnaire des variables :


| Variable (EN)             | Description                  
|---------------------------|-----------------------------
| `Model`                   | Nom du modèle BMW             
| `Year`                    | Année de vente                
| `Region`                  | Zone géographique           
| `Color`                   | Couleur de la voiture        
| `Fuel_Type`               | Type de carburant            
| `Transmission`            | Type de transmission         
| `Engine_Size_L`           | Cylindrée en litres           
| `Mileage_KM`              | Kilométrage                    
| `Price_USD`               | Prix en dollars US            
| `Sales_Volume`            | Volume de ventes              
| `Sales_Classification`    | Classification des ventes    

A noter: Toutes les variables et les modalités ont été traduites en français pendant le traitement

## 🧰 **Stack technique utilisée**

|Outil                          |Rôle
|-------------------------------|-----------------------------
|Python (Pandas, Numpy, matplotlib, seaborn, plotly) |Nettoyage, transformation, traduction et exploration des données
|VS Code	                    |Environnement de développement
|Power BI	                    |Visualisation interactive et storytelling des insights
|Git & GitHub	                |Versioning, documentation et diffusion en portfolio
|Markdown	                    |Documentation structurée (README)

## 📊 **Quelques insights clés**

Top 5 des modèles les plus vendus mondialement

Montée en puissance des motorisations hybrides et électriques

Recul progressif du diesel dans certaines régions

Régions clés en volume : Europe, Amérique du Nord, Asie

Couleurs les plus populaires selon les segments

Tendance à la généralisation de la transmission automatique

## 📌 **Perspectives d’amélioration pour une version 2 du projet axée Machine Learning**

- Ajout d’une analyse prédictive sur les ventes futures par modèle 
- Création d’un pipeline automatisé (Python ou Azure Data Factory → Power BI Refresh)