# regions_geojson_builder.py
import io, zipfile, requests, os, geopandas as gpd

NE_URL = "https://naturalearth.s3.amazonaws.com/50m_cultural/ne_50m_admin_0_countries.zip"
LOCAL_ZIP = "ne_50m_admin_0_countries.zip"

print("Téléchargement des frontières (Natural Earth)…")
r = requests.get(NE_URL, timeout=60)
r.raise_for_status()
with open(LOCAL_ZIP, "wb") as f:
    f.write(r.content)

print("Chargement du shapefile depuis la ZIP locale…")
# Deux syntaxes possibles selon versions ; la 1ère marche le plus souvent :
# 1) chemin de la zip seule
try:
    gdf = gpd.read_file(f"zip://{LOCAL_ZIP}")
except Exception:
    # 2) chemin explicite vers le shapefile dans la zip
    gdf = gpd.read_file(f"zip://{LOCAL_ZIP}!ne_50m_admin_0_countries.shp")

# Natural Earth: on s’assure d’avoir les colonnes utiles
if "NAME_EN" not in gdf.columns and "NAME" in gdf.columns:
    gdf["NAME_EN"] = gdf["NAME"]
else:
    gdf["NAME_EN"] = gdf["NAME_EN"].fillna(gdf.get("ADMIN", gdf.get("NAME", "")))

if "CONTINENT" not in gdf.columns:
    raise ValueError("Le champ CONTINENT est introuvable dans le shapefile Natural Earth.")

# --- définition des régions ---
middle_east = {
    "Saudi Arabia","United Arab Emirates","Oman","Yemen","Qatar","Bahrain","Kuwait",
    "Iraq","Iran","Israel","Jordan","Lebanon","Syria","Turkey","Palestine"
}

continent_map_fr = {
    "Africa": "Afrique",
    "Europe": "Europe",
    "Asia": "Asie",
    "North America": "Amérique du Nord",
    "South America": "Amérique du Sud",
    "Oceania": None,
    "Seven seas (open ocean)": None,
    "Antarctica": None
}

def region_fr(row):
    name = row["NAME_EN"]
    cont = row["CONTINENT"]
    if name in middle_east:
        return "Moyen-Orient"
    return continent_map_fr.get(cont, None)

gdf["Region_FR"] = gdf.apply(region_fr, axis=1)
gdf = gdf[gdf["Region_FR"].notna()].copy()

# (optionnel mais robuste) réparer des géométries avant dissolve
gdf["geometry"] = gdf.buffer(0)

print("Dissolution par région…")
regions = (
    gdf[["Region_FR", "geometry"]]
    .dissolve(by="Region_FR", as_index=False)
)

regions = regions[regions["Region_FR"].isin([
    "Asie","Afrique","Europe","Amérique du Nord","Amérique du Sud","Moyen-Orient"
])].copy()

regions = regions.rename(columns={"Region_FR": "name"})

out = "regions_bmw_sales.geojson"
regions.to_file(out, driver="GeoJSON", encoding="utf-8")
print(f"✔ Fichier créé : {os.path.abspath(out)}")
