# Ambiente de desarrollo local de Odoo + Python + PostgreSQL


# Instalación de Softwares iniciales
1. Instalar Python: Odoo está desarrollado en Python, así que primero necesitas instalarlo. Descarga la última versión de Python desde su sitio oficial: https://www.python.org/downloads/. 

Asegúrate de marcar la opción "Add Python to PATH" durante la instalación (El asistente de instalación te preguntará para hacerlo por ti, requiere reinicio del sistema operativo).


2. Instalar PostgreSQL: Odoo utiliza PostgreSQL como su sistema de gestión de bases de datos. Puedes descargarlo desde el sitio oficial de PostgreSQL: https://www.postgresql.org/download/. 

Durante la instalación, recuerda crear un usuario y una base de datos que Odoo utilizará (Para este proyecto se creó el usuario: jm25prueba, contraseña: JMprueba25.).


3. Instalar Postman: esta herramienta será necesaria para probar la API que realizará las peticiones a los modulos de la instancia de odoo: https://www.postman.com/downloads/


4. Instalar Git bash para clonar este repositorio en tu ambiente local: https://git-scm.com/downloads.


# Restaurar Base de Datos de prueba
1. Abrir el PostgreSQL y crear una Base de Datos (preferiblemente con el nombre: prueba-tecnica)

2. Hacer clic derecho sobre la Base de Datos creada y seleccionar la opción "RESTORE"

3. En "format" dejarle por defecto "Custom or Tar" y proceder a buscar el archivo "prueba-tecnica-300924.sql" en la ruta "desarrollo\prueba-tecnica-odoo\db_backup" del proyecto clonado.

4. Presionar el botón "Restore" y esperar unos 5 segudos aproximadamente para que se cargue toda la estructura y datos del respaldo


# Instalación de dependencias y librerias
1. Instalar dependencias: dentro de la carpeta de este proyecto que acabas de clonar, ejecuta el siguiente comando para instalar las dependencias necesarias:
```
pip install -r requirements.txt
```


2. Ejecutar el siguiente comando para descargar las utilidades primordiales de entorno
```
pip install setuptools
``` 


3. Dentro de la carpeta raíz del repositorio clonado, ejecutar el siguiente comando vía terminal bash para instalar xml-rpc:
```
pip install pypi-xmlrpc
```


4. Ejecutar el siguiente comando vía terminal bash para instalar odoo-rpc:
```
pip install odoorpc
```


5. Ejecutar el siguiente comando vía terminal bash para instalar flask-xml-rpc:
```
pip install flask-xml-rpc
```


6. Iniciar Odoo: Puedes iniciar el proyecto Odoo ejecutando el siguiente comando en la terminal de tu preferencia (git bash, mobaxterm, power shell):
```
python odoo-bin -c odoo.conf
```


7. Para acceder a Odoo local: Abre tu navegador y ve a la siguiente dirección:
```
http://localhost:8069
```