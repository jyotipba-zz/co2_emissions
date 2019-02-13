import pandas as pd
def fetch_data():
    population_url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    co2_emission_url = "http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv"


def get_co2_data(country):
    data = pd.read_csv("./static/carbon.csv",  skiprows=4)
    data = data.drop(["Country Code","Indicator Name","Indicator Code"] , axis = 1)
    carbon_emission = data.loc[data["Country Name"] == country].drop(["Country Name"], axis =1)
    year = carbon_emission.columns.tolist()
    carbon_emission = list(carbon_emission.iloc[0])

    return carbon_emission, year 
