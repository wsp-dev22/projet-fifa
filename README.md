# Projet FIFA – Analyse des joueurs

## Description
Analyse des joueurs de FIFA à partir d’un dataset public.  
Objectifs :
- Identifier les top 10 joueurs par note globale.
- Calculer les moyennes par poste, club et pays.
- Visualiser les données avec des graphiques (bar chart, scatter, heatmap).
- Extraire des insights sur les joueurs, clubs et nations.

## Dataset
- Source : [SoFIFA](https://sofifa.com/)  
- Colonnes principales :
  - `Name`, `Country`, `Position`, `Age`, `Overall_Rating`, `Potential`, `Team`, `Value € M`, `Wage € K`, `Total_Stats`

## Analyse réalisée

### Top 10 joueurs
- Les 10 meilleurs joueurs du dataset selon la note globale.

### Moyennes
- Moyenne par poste, club et pays.
- Top 10 clubs et pays sont affichés pour plus de clarté.

### Graphiques

![Distribution des notes](images/histogram_notes.png)  
*Distribution des notes globales des joueurs FIFA.*

![Note moyenne par poste](images/bar_position.png)  
*Note moyenne par poste.*

![Top 10 clubs par note moyenne](images/bar_top10_clubs.png)  
*Top 10 clubs par note moyenne.*

![Note globale vs Potentiel](images/scatter_rating_potential.png)  
*Note globale vs potentiel des joueurs.*

![Note globale vs Valeur (€M)](images/scatter_rating_value.png)  
*Note globale vs valeur marchande.*

![Heatmap poste x top 10 clubs](images/heatmap_poste_club.png)  
*Note moyenne par poste et par club (top 10 clubs).*

![Top 10 pays par note moyenne](images/bar_top10_pays.png)  
*Top 10 pays par note moyenne.*

### Insights
- Les attaquants ont en moyenne une note plus élevée que les défenseurs.  
- Les clubs et pays ont des notes globales très variables.  
- La majorité des joueurs se situe entre 65 et 75 en note globale.  
- Certains joueurs ont un potentiel très élevé malgré une note actuelle moyenne.

## Scripts
- `analyse_fifa.py` → script d’analyse et génération des graphiques.  
- `fifa.csv` → dataset des joueurs.
- `images/` → Dossier contenant tous les graphiques générés par le script :  
  - `histogram_notes.png` : Distribution des notes globales des joueurs.  
  - `bar_position.png` : Note moyenne par poste.  
  - `bar_top10_clubs.png` : Top 10 clubs par note moyenne.  
  - `scatter_rating_potential.png` : Note globale vs potentiel.  
  - `scatter_rating_value.png` : Note globale vs valeur (€M).  
  - `heatmap_poste_club.png` : Heatmap des notes moyennes par poste et top 10 clubs.  
  - `bar_top10_pays.png` : Top 10 pays par note moyenne.
