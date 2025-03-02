import requests # type: ignore
import pandas as pd # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Carga las variables del archivo .env
load_dotenv()

# Obtiene la clave API desde la variable de entorno
API_KEY = os.getenv("SERPAPI_KEY")
if not API_KEY:
    raise ValueError("No se encontró la clave API. Configura la variable 'SERPAPI_KEY' en un archivo .env o como variable de entorno.")

# Lista global para almacenar todos los empleos
all_jobs = []

def search_jobs(query, location):
    """Función para buscar empleos y agregar los resultados a la lista global."""
    url = f"https://serpapi.com/search.json?engine=google_jobs&q={query}&location={location}&api_key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP erróneos
        
        data = response.json()
        jobs = data.get("jobs_results", [])
        
        if jobs:
            for job in jobs:
                title = job.get("title", "No disponible")
                company = job.get("company_name", "No disponible")
                location = job.get("location", "No disponible")
                via = job.get("via", "No disponible")
                description = job.get("description", "No disponible")
                
                # Acceso seguro a enlaces relacionados
                related_links = job.get("related_links", [])
                job_url = related_links[0].get("link", "No disponible") if related_links else "No disponible"
                
                all_jobs.append({
                    "Título": title,
                    "Empresa": company,
                    "Ubicación": location,
                    "Publicado en": via,
                    "Descripción": description,
                    "Enlace": job_url
                })
            print(f"Se encontraron {len(jobs)} empleos para '{query}' en '{location}'.")
            print(f"Total acumulado: {len(all_jobs)} empleos.")
        else:
            print(f"No se encontraron empleos para '{query}' en '{location}'.")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud HTTP: {e}")
    except ValueError as e:
        print(f"Error al procesar datos JSON: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def save_to_csv():
    """Función para guardar todos los empleos acumulados en un CSV."""
    if all_jobs:
        try:
            df = pd.DataFrame(all_jobs)
            df.to_csv("empleos_resultados.csv", index=False, encoding="utf-8")
            print("Los resultados se han guardado en 'empleos_resultados.csv'.")
        except Exception as e:
            print(f"Error al guardar CSV: {e}")
    else:
        print("No hay empleos para guardar.")

# Bucle principal
while True:
    # Pedir parámetros al usuario
    query = input("Ingresa el tipo de empleo (o 'salir' para terminar): ")
    if query.lower() == "salir":
        break
    
    location = input("Ingresa la ubicación (ejemplo: 'San Francisco, CA'): ")
    
    # Realizar la búsqueda
    search_jobs(query, location)
    
    # Preguntar qué hacer después
    action = input("¿Qué quieres hacer? (buscar otro / guardar csv / salir): ").lower()
    if action == "guardar csv":
        save_to_csv()
        break
    elif action == "salir":
        break
    # Si dice "buscar otro" o cualquier otra cosa, el bucle continúa

# Si sale sin guardar, preguntar si quiere el CSV
if all_jobs and input("¿Quieres guardar los resultados en un CSV? (sí/no): ").lower() == "sí":
    save_to_csv()