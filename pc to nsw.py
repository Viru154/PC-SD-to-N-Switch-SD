import os
import shutil
from datetime import datetime

def process_images_with_nested_structure(source_folder, target_folder):
    # Traverse all directories and files in the source folder / Recorrer todas las carpetas y archivos en la carpeta de origen
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith((".jpg", ".png")):  # Valid extensions / Extensiones válidas
                file_path = os.path.join(root, file)  # Full path of the current file / Ruta completa del archivo actual
                
                # Generate the file name in Nintendo Switch format / Crear el nombre del archivo con formato de Nintendo Switch
                creation_time = os.path.getmtime(file_path)  # Get file creation time / Obtener la fecha de creación del archivo
                formatted_time = datetime.fromtimestamp(creation_time).strftime("%Y%m%d%H%M%S")  # Format timestamp / Formatear la fecha y hora
                new_file_name = f"{formatted_time}_s.jpg"  # Append "_s" to the formatted name / Agregar "_s" al nombre formateado

                # Create the folder structure Year/Month/Day / Crear la estructura de carpetas Año/Mes/Día
                year = datetime.fromtimestamp(creation_time).strftime("%Y")  # Extract year / Extraer el año
                month = datetime.fromtimestamp(creation_time).strftime("%m")  # Extract month / Extraer el mes
                day = datetime.fromtimestamp(creation_time).strftime("%d")  # Extract day / Extraer el día

                # Define the path for the new folder / Definir la ruta de la nueva carpeta
                new_folder_path = os.path.join(target_folder, "Nintendo", "Album", year, month, day)

                # Full path for the new file / Ruta completa para el nuevo archivo
                new_file_path = os.path.join(new_folder_path, new_file_name)

                # Create the folder if it doesn't exist / Crear la carpeta si no existe
                os.makedirs(new_folder_path, exist_ok=True)

                # Check if the file already exists in the destination / Verificar si el archivo ya existe en el destino
                if os.path.exists(new_file_path):
                    print(f"File already exists: {new_file_path}")  # Archivo ya existe
                    continue  # Skip to the next file / Saltar al siguiente archivo

                # Copy and rename the file / Copiar y renombrar el archivo
                shutil.copy2(file_path, new_file_path)  # Use copy2 to preserve metadata / Usar copy2 para conservar los metadatos
                print(f"File copied: {file_path} -> {new_file_path}")  # Archivo copiado

# Source and destination folders / Carpetas de origen y destino
source_folder = "c:example"  # Replace with the actual source folder / Reemplazar con la carpeta de origen
target_folder = "c:example"  # Replace with the actual destination folder / Reemplazar con la carpeta de destino

# Process the images / Procesar las imágenes
process_images_with_nested_structure(source_folder, target_folder)
