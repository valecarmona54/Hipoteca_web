## LENGUAJES DE PROGRAMACIÓN Y CÓDIGO LIMPIO 2024-1

### POR:
- Rostin Santiago Alzate Montoya
- Miguel Ayala Parra

## Proyecto mejorado por:
    -Valentina Carmona 
    -David Zabala

# Calculadora de Hipoteca Inversa

## Descripción
Esta aplicación web calcula la hipoteca inversa en tres modalidades diferentes: Temporal, Vitalicia y Única.
Ademas permite la gestion de usuarios

## Hipoteca inversa temporal: 
En este tipo de hipoteca, el prestamista proporciona pagos periódicos al prestatario durante un período de tiempo específico. Durante este tiempo, el prestatario no tiene que hacer pagos de hipoteca. Al final del período acordado, el prestatario debe pagar el saldo total de la hipoteca o vender la propiedad para saldar la deuda. Esta modalidad es útil para personas que necesitan ingresos adicionales durante un período específico.

## Hipoteca inversa vitalicia: 
En este caso, el prestatario recibe pagos periódicos durante toda su vida, siempre y cuando permanezca en la propiedad como su residencia principal. No hay plazo de tiempo específico para el pago. La deuda total, incluidos los intereses acumulados, se paga cuando el prestatario vende la propiedad, se muda a otro lugar permanentemente o fallece. Esta modalidad es ideal para personas mayores que buscan una fuente de ingresos sostenida en el tiempo.

## Hipoteca inversa única: 
Esta modalidad implica un solo desembolso de dinero por parte del prestamista al prestatario en lugar de pagos periódicos. La cantidad se calcula en función del valor de la propiedad, la edad del prestatario y otros factores. No hay pagos posteriores ni acumulación de intereses. La deuda se paga cuando el prestatario vende la propiedad, se muda permanentemente o fallece.

# Estructura del Proyecto anterior

- Carpeta E4: Contiene archivos esenciales para la configuración y ejecución del proyecto.
    - requirements.txt: Archivo con las dependencias necesarias.
    - runserver.py: Script para ejecutar el servidor de la aplicación.
    - secret.cfg: Archivo de configuración con las credenciales de la base de datos.
    - Carpeta MVC_HIPOTECA_INVERSA_4: Contiene la lógica de negocio, modelos, vistas y controladores de la aplicación.
        - __init__.py: Inicializador del paquete.
        - views.py: Controladores y rutas de la aplicación.
        - Carpeta logic: Contiene la lógica de negocio de la aplicación.
            - __init__.py: Inicializador de lógica de negocio.
            - Calculations.py: Funciones para calcular la hipoteca inversa en diferentes modalidades.
        - Carpeta model: Contiene los modelos de datos de la aplicación.
            - __init__.py: Inicializador de modelos.
            - database_manager.py: Gestión de la base de datos.
            - model_reverse_mortage.py: Modelo de hipoteca inversa.
            - model_user.py: Modelo de usuario.
        - Carpeta static: Contiene archivos estáticos como CSS, fuentes y scripts.
            - Carpeta content: Contiene archivos CSS para estilos de la interfaz.
            - Carpeta fonts: Contiene archivos de fuentes para estilos de la interfaz.
            - Carpeta scripts: Contiene archivos JavaScript para funcionamientos de la interfaz.
        - Carpeta templates: Contiene las vistas HTML.
            - calculations_user.html: Vista para mostrar los cálculos de hipotecas del usuario.
            - index.html: Vista principal de la aplicación.
            - index_login.html: Vista principal después de iniciar sesión.
            - layout.html: Plantilla base para las vistas.
            - layout_login.html: Plantilla base para las vistas después de iniciar sesión.
            - lifetime.html: Vista para cálculos de hipoteca vitalicia.
            - login.html: Vista para iniciar sesión.
            - register.html: Vista para registrar nuevos usuarios.
            - temporary.html: Vista para cálculos de hipoteca temporal.
            - unique.html: Vista para cálculos de hipoteca única.
            - update_user.html: Vista para actualizar datos del usuario.
        - Carpeta test: Contiene las pruebas unitarias.
            - __init__.py: Inicializador de pruebas.
            - test.py: Pruebas unitarias para la aplicación.


# Estructura del Proyecto mejorado
- Carpeta Hipoteca_web: Contiene archivos esenciales para la configuración y ejecución del proyecto.
    - requirements.txt: Archivo con las dependencias necesarias.
    - runserver.py: Script para ejecutar el servidor de la aplicación.
    - secret.cfg: Archivo de configuración con las credenciales de la base de datos.
    - Carpeta src: Contiene la lógica de negocio, modelos, vistas y controladores de la aplicación.
        - carpeta controller: Contiene los modelos de datos de la aplicación.
            - __init__.py: Inicializador.
            - database_manager.py: Gestión de la base de datos.
            - model_reverse_mortage.py: Modelo de hipoteca inversa.
            - model_user.py: Modelo de usuario.
        - Carpeta model: Contiene la lógica de negocio de la aplicación.
            - __init__.py: Inicializador de lógica de negocio.
            - Calculations.py: Funciones para calcular la hipoteca inversa en diferentes modalidades.
        - Carpeta view_web: Contiene la lógica de negocio de la aplicación.
            - __init__.py: Inicializador.
            - views.py: Controladores y rutas de la aplicación.
        - Carpeta static: Contiene archivos estáticos como CSS, fuentes y scripts.
            - Carpeta content: Contiene archivos CSS para estilos de la interfaz.
            - Carpeta fonts: Contiene archivos de fuentes para estilos de la interfaz.
            - Carpeta scripts: Contiene archivos JavaScript para funcionamientos de la interfaz.
        - Carpeta templates: Contiene las vistas HTML.
            - calculations_user.html: Vista para mostrar los cálculos de hipotecas del usuario.
            - index.html: Vista principal de la aplicación.
            - index_login.html: Vista principal después de iniciar sesión.
            - layout.html: Plantilla base para las vistas.
            - layout_login.html: Plantilla base para las vistas después de iniciar sesión.
            - lifetime.html: Vista para cálculos de hipoteca vitalicia.
            - login.html: Vista para iniciar sesión.
            - register.html: Vista para registrar nuevos usuarios.
            - temporary.html: Vista para cálculos de hipoteca temporal.
            - unique.html: Vista para cálculos de hipoteca única.
            - update_user.html: Vista para actualizar datos del usuario.
    - Carpeta test: Contiene las pruebas unitarias.
        - __init__.py: Inicializador de pruebas.
        - test.py: Pruebas unitarias para la aplicación.

# Instrucciones de Instalación y Ejecución

## 1. Clonar o descargar el repositorio

Primero, clona o descarga el repositorio de GitHub y navega al directorio del proyecto:

## 2. Crear y activar un entorno virtual(Para Windows)


python -m venv venv
venv\Scripts\activate


## 3. Instalar las dependencias
instala las dependencias necesarias utilizando el archivo 'requirements.txt'


pip install -r E4/requirements.txt


## 4. Configurar la Base de Datos
Edite el archivo 'secret.cfg', con las credenciales de su base de datos
- En caso de error considera eliminar las comillas a las variables y dejarlas sin ellas
- Si sigue teneindo errores por favor considere cambair en la linea 18 del archivo database_manager.py, a lo siguiente:

        config.read(r'Ruta directa y completa hasta el archivo secret.cfg, incluyendolo')


## 5. Ejecutar la aplicacion
Iniciar el servidor de la aplicacion ejecutando el siguiente comando


python E4/runserver.py


Abre tu navegador y ve a la URL 'http://localhost:5555/' para acceder a la aplicación.

## 6. Para ejecutar las pruebas unitarias:
- Accede usando cd hasta llegar a la carpeta test (cd E4, cd MVC_HIPOTECA_INVERSA_4, cd test), cuando estes aqui ejecuta lo siguiente:


python test.py


### Advetencia
- Este proyecto requiere una conexion estable y activa a internet para funcinar correctamente
- Se probo en otros entornos y en algunos la aplicacion sacaba error debido a que el compilador tenia diferente configuración, esto ya es algo que se me sale de las manos, pero que normalmente es muy breve de solucionar

# Instrucciones de Instalación y Ejecución del proyecto mejorado
## 1. Clonar o descargar el repositorio

Primero, clona o descarga el repositorio de GitHub y navega al directorio del proyecto:

Configuracion Base de datos
1.	Debes ingresar a la pagina Neon. Neon.Tech
2.	Te registrar/logea, una vez registrado debes crear un proyecto, el titulo del proyecto a tu preferencia y el nombre de la base de datos puede porle: "Calculadora hipoteca" y le das es crear proyecto.
3.	Una vez creado el proyecto y la base de datos te dirijes a la opcion Dashboard.
4.	Desplegas el menu donde dice Connection string, alli seleccionas la opcion de Parameters only.
5.	Copias todo lo que se encuentra en el campo de texto y te dirijes donde tienes el repositorio abierto.
6.	En la carpeta del hipoteca_web una carpeta llamada secret.cfg
7.	En este archivo debes pegar los parametros que copias en el Neon de tu base de datos.
8.	Asegúrese de tener Flask y las dependencias necesarias instaladas, de no tenerla instalada con el comando pip instanll Flask, lo instalas.
- En caso de error considera eliminar las comillas a las variables y dejarlas sin ellas
- Si sigue teneindo errores por favor considere cambair en la linea 18 del archivo database_manager.py, a lo siguiente:

        config.read(r'Ruta directa y completa hasta el archivo secret.cfg, incluyendolo')


## 2. Crear y activar un entorno virtual(Para Windows)


python -m venv venv
venv\Scripts\activate


## 3. Instalar las dependencias
instala las dependencias necesarias utilizando el archivo 'requirements.txt'


pip install -r requirements.txt


## 4. Configurar la Base de Datos
Edite el archivo 'secret.cfg', con las credenciales de su base de datos
- En caso de error considera eliminar las comillas a las variables y dejarlas sin ellas

## 5. Ejecutar la aplicacion
Iniciar el servidor de la aplicacion ejecutando el siguiente comando


python runserver.py


Abre tu navegador y ve a la URL 'http://localhost:5555/' para acceder a la aplicación.