import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

#  Préparer le dossier images 
if not os.path.exists("images"):
    os.makedirs("images")

#  Charger le dataset 
df = pd.read_csv("fifa.csv")

# Supprimer les colonnes inutiles
df = df.drop(columns=["Unnamed: 0","photo_link","country_flag_img_link"])

#  Aperçu des données 
print("Aperçu du dataset :")
print(df.head())

#  Top 10 joueurs par note globale 
top_players = df.sort_values(by="Overall_Rating", ascending=False)
print("\nTop 10 joueurs par note globale :")
print(top_players[['Name','Team','Overall_Rating','Potential']].head(10))

#  Moyennes par poste, club, pays 
avg_by_position = df.groupby("Position")["Overall_Rating"].mean()
avg_by_team = df.groupby("Team")["Overall_Rating"].mean()
avg_by_country = df.groupby("Country")["Overall_Rating"].mean()

#  Graphiques de base 

# 1 Histogramme notes globales
plt.figure()
plt.hist(df["Overall_Rating"], bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution des notes des joueurs FIFA")
plt.xlabel("Note globale")
plt.ylabel("Nombre de joueurs")
plt.tight_layout()
plt.savefig("images/histogram_notes.png")
plt.show()

# 2 Bar chart moyenne par poste
plt.figure()
avg_by_position.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title("Note moyenne par poste")
plt.ylabel("Note globale")
plt.xlabel("Poste")
plt.tight_layout()
plt.savefig("images/bar_position.png")
plt.show()

# 3 Bar chart top 10 clubs par note moyenne
plt.figure(figsize=(10,5))
top10_clubs = avg_by_team.sort_values(ascending=False).head(10)
top10_clubs.plot(kind='bar', color='orange', edgecolor='black')
plt.title("Top 10 clubs par note moyenne")
plt.ylabel("Note globale")
plt.xlabel("Club")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("images/bar_top10_clubs.png")
plt.show()

# 4 Scatter plot note globale vs potentiel
plt.figure()
plt.scatter(df["Overall_Rating"], df["Potential"], alpha=0.5, c='purple')
plt.title("Note globale vs Potentiel")
plt.xlabel("Note globale")
plt.ylabel("Potentiel")
plt.tight_layout()
plt.savefig("images/scatter_rating_potential.png")
plt.show()

# 5 Scatter plot note globale vs valeur (€M)
plt.figure()
plt.scatter(df["Overall_Rating"], df["Value € M"], alpha=0.5, c="green")
plt.title("Note globale vs Valeur (€M)")
plt.xlabel("Note globale")
plt.ylabel("Valeur (€M)")
plt.tight_layout()
plt.savefig("images/scatter_rating_value.png")
plt.show()

# 6 Heatmap poste x club (top 10 clubs)
heatmap_data = df[df['Team'].isin(top10_clubs.index)].pivot_table(values="Overall_Rating", index="Position", columns="Team", aggfunc="mean")
plt.figure(figsize=(12,6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu")
plt.title("Note moyenne par poste et top 10 clubs")
plt.tight_layout()
plt.savefig("images/heatmap_poste_club.png")
plt.show()

# 7 Top 10 pays par note moyenne
plt.figure(figsize=(8,5))
top10_countries = avg_by_country.sort_values(ascending=False).head(10)
top10_countries.plot(kind="bar", color="lightcoral", edgecolor="black")
plt.title("Top 10 pays par note moyenne")
plt.ylabel("Note globale")
plt.xlabel("Pays")
plt.tight_layout()
plt.savefig("images/bar_top10_pays.png")
plt.show()

print("\n✅ Script terminé")
