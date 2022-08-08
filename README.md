### Ver versiones

- `python --version`, muestra la version instalada en window

- `pip3 --version`, muestra la version de pip

- `pipenv --version`, muestra la version de pipenv

#### Instalacion pipenv

- En modo administrador, `pip install pipenv`, se hace una sola vez, quedará instalado de manera global en el sistema

- En mac se utiliza `sudo pip3 install pipenv`, pedira contraseña


#### Instalacio entorno virtual

- para instalar el entorno `pipenv --python=3.10`

- Para activar el entorno dentro del proyecto `pipenv shell`

- Para salir del entorno virtual, se utiliza `exit`

### Instalacion de frameworsks

- Se utiliza `pipenv install nombreFramework`
- En caso de usa una librería no instalada el error sera 'No module named 'nombreLibreria'' 
- Las librerias instaladas se podrán ver en el archivo Pipfile.

### Correr el proyecto

- se utiliza `python nombreArchivoPrincipal.py`
- por defecto arranca un servidor o entorno de desarrollo
- para terminar o salir del modo servidor, se utiliza `CTRL + c`
- es importante activar el modo debug en el documento para ver errores `(debug=True)`

### Observaciones

- 

