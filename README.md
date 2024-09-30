# prueba-tecnica-odoo

# Pasos para la preparación del ambiente de desarrollo local (Windows)

1. Instalar Python: Odoo está desarrollado en Python, así que primero necesitas instalarlo. Descarga la última versión de Python desde su sitio oficial. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.


2. Instalar PostgreSQL: Odoo utiliza PostgreSQL como su sistema de gestión de bases de datos. Puedes descargarlo desde el sitio oficial de PostgreSQL. Durante la instalación, recuerda crear un usuario y una base de datos que Odoo utilizará.


3. Instalar Git: Odoo se puede clonar desde su repositorio en GitHub. Descarga Git desde su sitio oficial e instálalo.


4. Clonar el repositorio de Odoo: Abre la terminal de Git Bash y ejecuta el siguiente comando para clonar la versión de Odoo que desees (por ejemplo, Odoo 15):
bash

```
git clone https://www.github.com/odoo/odoo --depth 1 --branch 15.0 --single-branch
```


5. Instalar dependencias: Navega a la carpeta de Odoo que acabas de clonar y ejecuta el siguiente comando para instalar las dependencias necesarias:
bash
   pip install -r requirements.txt


6. Configurar Odoo: Crea un archivo de configuración para Odoo. Puedes copiar el archivo de ejemplo que se encuentra en la carpeta de Odoo y renombrarlo a
odoo.conf
. Asegúrate de configurar los parámetros de conexión a la base de datos y otros ajustes necesarios.


7. Iniciar Odoo: Finalmente, puedes iniciar Odoo ejecutando el siguiente comando en la terminal:
bash
   python odoo-bin -c odoo.conf


8. Acceder a Odoo: Abre tu navegador y ve a
http://localhost:8069`. Deberías ver la pantalla de inicio de Odoo.