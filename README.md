# 🎬 Recomendador de Películas con TMDB

Este programa está diseñado para ayudarnos a decidir qué película ver en el cine con nuestras amistades. Utiliza la API de [TMDB (The Movie Database)](https://www.themoviedb.org/) para obtener información actualizada sobre películas, recomendaciones, tendencias y géneros.

## 📋 Funcionalidades

El programa ofrece un menú interactivo con las siguientes opciones:

1. **Buscar código de película según su nombre**  
   Permite introducir el nombre de una película y obtener su ID correspondiente en TMDB.

2. **Buscar información de una película según su código (ID)**  
   Dado el ID de una película, muestra los siguientes datos:
   - Título
   - Géneros
   - Argumento
   - Duración
   - Otros detalles relevantes
   - Enlace a su página en **IMDb**

3. **Recomendaciones basadas en una película**  
   A partir de una película concreta, se muestran recomendaciones similares según TMDB.

4. **Películas trending (tendencias)**  
   Permite ver las 5 películas más populares del día o de la semana.  
   - Se puede filtrar por género o ver todas sin filtro.

5. **Mostrar géneros disponibles**  
   Lista todos los géneros de películas disponibles en TMDB, con su respectivo ID.

## 🔐 Seguridad de la API Key

Por razones de seguridad, **la clave de la API de TMDB no estara incluida directamente en el código fuente**. En su lugar, debe almacenarse como una **variable de entorno del sistema** con el nombre: "TMDB_API_KEY"

