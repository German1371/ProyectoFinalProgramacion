"""
------------------------------Proyecto final programación------------------------------
Pasos iniciales:
    1. Declarar la clave Api como variable de entorno del sistema.
        Comando en la terminal: setx TMDB_API_KEY "clave de producto".
    2. Instalar el módulo request si no está instalado.
Autor: Germán Cosano Torres
"""
import os
import requests

# Constante para la URL base
BASE_URL = "https://api.themoviedb.org/3"

class Menu:
    def __init__(self):
        self.api_key = os.getenv("TMDB_API_KEY")
        if not self.api_key:
            raise ValueError("ERROR: No se ha encontrado la variable de entorno 'TMDB_API_KEY'.")


    def show_menu(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Buscar código de película según su nombre")
            print("2. Buscar información de película según su código")
            print("3. Recomendar películas similares a una concreta")
            print("4. Ver películas trending por género")
            print("5. Mostrar géneros disponibles")
            print("0. Salir")

            option = input("Selecciona una opción: ")

            match option:
                case "1":
                    print("Has elegido buscar película por nombre.")
                    self.search_by_code_film()
                case "2":
                    print("Has elegido buscar información por código.")
                    self.search_info()
                case "3":
                    print("Has elegido ver películas recomendadas.")
                    self.recomendate()
                case "4":
                    print("Has elegido ver películas trending por género.")
                    self.trending_by_genre()
                case "5":
                    print("Has elegido mostrar géneros disponibles.")
                    self.show_genre()
                case "0":
                    print("Saliendo del programa...")
                case _:
                    print("Opción no válida.")
                    print("Por favor vuelva a elegir una opción")

    def search_by_code_film(self):
        nombre = input("Introduce el nombre de la película: ").strip()
        url = f"{BASE_URL}/search/movie"
        params = {
            "api_key": self.api_key,
            "language": "es-ES",
            "query": nombre
        }

        response = requests.get(url, params=params)
        data = response.json()
        results = data.get("results", [])
        if results:
            for movie in results[:5]:
                print(f"{movie['title']} (ID: {movie['id']})")
        else:
            print("No se encontraron resultados con ese ID.")

    def search_info(self):
        movie_id = input("Introduce el ID de la película: ").strip()
        url = f"{BASE_URL}/movie/{movie_id}"
        params = {
            "api_key": self.api_key,
            "language": "es-ES"
        }

        response = requests.get(url, params=params)
        if response.status_code != 200: # Dice si la petición fue exitosa(200) o fallo
            print("Error al obtener información de la película.")
            return# Este return hace que la función no devuelva nada asi no ejecuta el resto de la función
        movie = response.json()

        print(f"\nTítulo: {movie.get('title', 'Desconocido')}") # El segundo parametro sirve para coger un valor por defecto si no tuviera el valor del primer parametro
        print(f"Géneros: {', '.join([genre['name'] for genre in movie.get('genres', [])])}")# Bucle para recorrer todos los géneros que puede tener una película
        print(f"Argumento: {movie.get('overview', 'No disponible')}")
        print(f"Duración: {movie.get('runtime', 'Desconocida')} minutos")
        imdb_id = movie.get('imdb_id')
        if imdb_id:
            print(f"Enlace a IMDb: https://www.imdb.com/title/{imdb_id}")
        else:
            print("No se encontró enlace a IMDb.")

    def recomendate(self):
        movie_id = input("Introduce el ID de la película: ").strip()
        url = f"{BASE_URL}/movie/{movie_id}/recommendations"
        params = {
            "api_key": self.api_key,
            "language": "es-ES"
        }

        response = requests.get(url, params=params)
        data = response.json()
        recommendations = data.get("results", [])
        if recommendations:
            print("\nRecomendaciones:")
            for movie in recommendations[:5]:
                print(f"{movie['title']} (ID: {movie['id']})")
        else:
            print("No se encontraron recomendaciones con ese ID.")

    def trending_by_genre(self):
        filter_ = input("¿Quieres filtrar por género? (s/n): ").strip().lower()
        genre_id = None

        if filter_ == "s":
            self.show_genre()
            genre_id = int(input("Introduce el ID del género: ").strip())

        type_ = input("¿Trending del día o de la semana? (d/s): ").strip().lower()
        if type_ == "d":
            periodo = "day"
        elif type_ == "s":
            periodo = "week"
        else:
            print("Opción no válida. Por favor introduzca d o s")
            return

        url = f"{BASE_URL}/trending/movie/{periodo}"
        params = {
            "api_key": self.api_key,
            "language": "es-ES"
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error al obtener las películas trending.")
            return

        data = response.json()
        Films = data.get("results", [])

        if genre_id is not None:# Comprobación de que se introduzca un id
            filtered_films = []# Crea una nueva lista vacía para guardar solo las películas que coinciden.
            for movie in Films:
                genres = movie.get("genre_ids", [])
                if genre_id in genres:
                    filtered_films.append(movie)# Si está el género indicado en los géneros lo añade a la lista de filtrados
            Films = filtered_films

        if Films:
            print("\nPelículas trending:")
            for movie in Films[:5]:
                print(f"{movie['title']} (ID: {movie['id']})")
        else:
            print("No se encontraron películas trending para ese género.")

    def show_genre(self):
        url = f"{BASE_URL}/genre/movie/list"
        params = {
            "api_key": self.api_key,
            "language": "es-ES"
        }

        response = requests.get(url, params=params)
        data = response.json()
        genre = data.get("genres", [])
        if genre:
            print("\nGéneros disponibles:")
            for genre in genre:
                print(f"{genre['id']}: {genre['name']}")
        else:
            print("No se pudieron obtener los géneros.")

# Ejecutar el programa
if __name__ == "__main__":
    menu = Menu()
    menu.show_menu()
