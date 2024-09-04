echo "# Proyecto de Gestión de Vehículos en un Condominio

## Descripción
Este proyecto es una aplicación web desarrollada en Django que permite gestionar el registro de ingreso y salida de vehículos de propietarios en un condominio. El sistema almacena información sobre los propietarios, sus vehículos, y los registros de entrada y salida.

## Requisitos del Sistema
- Python 3.12
- Django 4.x
- SQLite3

## Instalación y Configuración
1. Clona el repositorio en tu máquina local:
   \`\`\`bash
   git clone https://github.com/tu-usuario/nombre-repositorio.git
   \`\`\`
2. Navega al directorio del proyecto:
   \`\`\`bash
   cd nombre-repositorio
   \`\`\`
3. Crea un entorno virtual y actívalo:
   \`\`\`bash
   python -m venv myvenv
   myvenv\\Scripts\\activate
   \`\`\`
4. Instala las dependencias:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
5. Realiza las migraciones para configurar la base de datos:
   \`\`\`bash
   python manage.py migrate
   \`\`\`
6. Inicia el servidor de desarrollo:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Uso
- Abre tu navegador web y ve a \`http://localhost:8000\` para acceder a la aplicación.

## Estructura del Proyecto
- \`manage.py\`: Script de administración de Django.
- \`settings.py\`: Configuraciones de la aplicación.
- \`urls.py\`: Definición de rutas.
- \`models.py\`: Definición de los modelos de la base de datos.
- \`views.py\`: Vistas de la aplicación.
- \`templates/\`: Plantillas HTML.
