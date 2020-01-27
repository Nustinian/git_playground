import pandas as pd
from geopy.geocoders import Nominatim

def has_volcano_column(filename):
  csv = pd.read_csv(filename)
  if pd.np.isin("Volcano", csv.columns) or pd.np.isin("volcano", csv.columns):
    return True
  else:
    return False

def v_or_V(volcanoes):
  if pd.np.isin("Volcano", volcanoes.columns):
    return "Volcano"
  else:
    return "volcano"

def append_to_csv(filename):
  nom = Nominatim(scheme = "http", user_agent = "my-application")
  volcanoes = pd.read_csv(filename)
  column = v_or_V(volcanoes)
  volcanoes["Latitude"] = volcanoes[column].apply(lambda x: nom.geocode(x).latitude if x != None else None)
  volcanoes["Longitude"] = volcanoes[column].apply(lambda x: nom.geocode(x).longitude if x != None else None)
  volcanoes.to_csv("results_" + filename, index=None)
  return volcanoes.to_html(index=None, classes="output", justify="center")