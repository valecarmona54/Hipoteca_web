## LENGUAJES DE PROGRAMACIÓN Y CÓDIGO LIMPIO 2024-1

### POR:
- Rostin Santiago Alzate Montoya
- Miguel Ayala Parra

# Calculadora de Hipoteca Inversa

## Descripción
Esta aplicación web calcula la hipoteca inversa en tres modalidades diferentes: Temporal, Vitalicia y Única.
Ademas permite la gestion de usuarios

# Estructura del Proyecto

- Carpeta `E4`: Contiene archivos esenciales para la configuración y ejecución del proyecto.
    - `requirements.txt`: Archivo con las dependencias necesarias.
    - `runserver.py`: Script para ejecutar el servidor de la aplicación.
    - `secret.cfg`: Archivo de configuración con las credenciales de la base de datos.
    - Carpeta `MVC_HIPOTECA_INVERSA_4`: Contiene la lógica de negocio, modelos, vistas y controladores de la aplicación.
        - `__init__.py`: Inicializador del paquete.
        - `views.py`: Controladores y rutas de la aplicación.
        - Carpeta `logic`: Contiene la lógica de negocio de la aplicación.
            - `__init__.py`: Inicializador de lógica de negocio.
            - `Calculations.py`: Funciones para calcular la hipoteca inversa en diferentes modalidades.
        - Carpeta `model`: Contiene los modelos de datos de la aplicación.
            - `__init__.py`: Inicializador de modelos.
            - `database_manager.py`: Gestión de la base de datos.
            - `model_reverse_mortage.py`: Modelo de hipoteca inversa.
            - `model_user.py`: Modelo de usuario.
        - Carpeta `static`: Contiene archivos estáticos como CSS, fuentes y scripts.
            - Carpeta `content`: Contiene archivos CSS para estilos de la interfaz.
            - Carpeta `fonts`: Contiene archivos de fuentes para estilos de la interfaz.
            - Carpeta `scripts`: Contiene archivos JavaScript para funcionamientos de la interfaz.
        - Carpeta `templates`: Contiene las vistas HTML.
            - `calculations_user.html`: Vista para mostrar los cálculos de hipotecas del usuario.
            - `index.html`: Vista principal de la aplicación.
            - `index_login.html`: Vista principal después de iniciar sesión.
            - `layout.html`: Plantilla base para las vistas.
            - `layout_login.html`: Plantilla base para las vistas después de iniciar sesión.
            - `lifetime.html`: Vista para cálculos de hipoteca vitalicia.
            - `login.html`: Vista para iniciar sesión.
            - `register.html`: Vista para registrar nuevos usuarios.
            - `temporary.html`: Vista para cálculos de hipoteca temporal.
            - `unique.html`: Vista para cálculos de hipoteca única.
            - `update_user.html`: Vista para actualizar datos del usuario.
        - Carpeta `test`: Contiene las pruebas unitarias.
            - `__init__.py`: Inicializador de pruebas.
            - `test.py`: Pruebas unitarias para la aplicación.
# Instrucciones de Instalación y Ejecución

## 1. Clonar o descargar el repositorio

Primero, clona o descarga el repositorio de GitHub y navega al directorio del proyecto:

## 2. Crear y activar un entorno virtual(Para Windows)

```
python -m venv venv
venv\Scripts\activate
```

## 3. Instalar las dependencias
instala las dependencias necesarias utilizando el archivo 'requirements.txt'

```
pip install -r E4/requirements.txt
```

## 4. Configurar la Base de Datos
Edite el archivo 'secret.cfg', con las credenciales de su base de datos
- En caso de error considera eliminar las comillas a las variables y dejarlas sin ellas
- Si sigue teneindo errores por favor considere cambair en la linea 18 del archivo database_manager.py, a lo siguiente:
```
        config.read(r'Ruta directa y completa hasta el archivo secret.cfg, incluyendolo')
```

## 5. Ejecutar la aplicacion
Iniciar el servidor de la aplicacion ejecutando el siguiente comando

```
python E4/runserver.py
```

Abre tu navegador y ve a la URL 'http://localhost:5555/' para acceder a la aplicación.

## 6. Para ejecutar las pruebas unitarias:
- Accede usando cd hasta llegar a la carpeta test (cd E4, cd MVC_HIPOTECA_INVERSA_4, cd test), cuando estes aqui ejecuta lo siguiente:

```
python test.py
```

### Advetencia
- Este proyecto requiere una conexion estable y activa a internet para funcinar correctamente
- Se probo en otros entornos y en algunos la aplicacion sacaba error debido a que el compilador tenia diferente configuración, esto ya es algo que se me sale de las manos, pero que normalmente es muy breve de solucionar
