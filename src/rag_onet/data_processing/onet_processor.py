from rag_onet.ingestion.onet_loader import (
    cargar_occupation_data,
    cargar_essential_skills,
)

def construir_onet_completo():
    ocupaciones = cargar_occupation_data()
    skills = cargar_essential_skills()

    onet_completo = ocupaciones.merge(
        skills,
        on="O*NET-SOC Code",
        suffixes=("_occupation", "_skill"),
    )

    return onet_completo

def seleccionar_columnas(datos):

    columnas = [
        "O*NET-SOC Code",
        "Title_occupation",
        "Description",
        "Element Name",
        "Scale Name",
        "Data Value",
    ]

    return datos[columnas]

def filtrar_importance(datos):
    datos_importance = datos[datos["Scale Name"] == "Importance"]

    return datos_importance

def ordenar_habilidades(datos):
    datos_ordenados = datos.sort_values(
        ["O*NET-SOC Code", "Data Value"],
        ascending=[True, False]
    )

    return datos_ordenados

def seleccionar_top_skills(datos, n=5):
    top_skills = datos.groupby("O*NET-SOC Code").head(n)

    return top_skills


resultado = construir_onet_completo()
resultado_limpio = seleccionar_columnas(resultado)
resultado_importance = filtrar_importance(resultado_limpio)
resultado_ordenado = ordenar_habilidades(resultado_importance)
resultado_top5 = seleccionar_top_skills(resultado_ordenado)

print(resultado_top5.head())
print(resultado_top5.shape)
