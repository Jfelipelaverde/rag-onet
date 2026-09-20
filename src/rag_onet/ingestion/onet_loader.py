import pandas as pd


def cargar_occupation_data():
    datos = pd.read_csv("data/raw/occupation_data.csv")
    return datos


def cargar_essential_skills():
    datos = pd.read_csv("data/raw/essential_skills.csv")
    return datos

def cargar_knowledge():
    datos = pd.read_csv("data/raw/knowledge.csv")
    return datos
