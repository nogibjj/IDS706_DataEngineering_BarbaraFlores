import pandas as pd
import matplotlib.pyplot as plt
import requests

from main import exploring_data, aggregated_stats, pie_plot, bar_plot_skills, hist_plot



def check_github_file_existence(owner, repo, path):
    """
    Verifica si un archivo existe en un repositorio público de GitHub.

    :param owner: El nombre del propietario del repositorio.
    :param repo: El nombre del repositorio.
    :param path: La ruta del archivo que deseas verificar.
    :return: True si el archivo existe, False en caso contrario.
    """
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    response = requests.get(url)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        raise Exception(f"Error al verificar la existencia del archivo: {response.status_code}")

# Ejemplo de uso para el archivo específico que mencionaste

if __name__ == "__main__":
    owner = "nogibjj"
    repo = "IDS706_DataEngineering_BarbaraFlores_Miniproject3"
    path1 = "total_applicants.png"
    assert check_github_file_existence(owner, repo, path1)
    path2 = "aggregated_stats.png"
    assert check_github_file_existence(owner, repo, path2)
    path3 = "involvement.png"
    assert check_github_file_existence(owner, repo, path3)


