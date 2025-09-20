import os
import shutil
import stat

def find_and_remove(target_dir):
    for root, dirs, _ in os.walk(target_dir):
        for folder in ['node_modules', 'vendor']:
            if folder in dirs:
                folder_path = os.path.join(root, folder)
                print(f"\nDirectorio detectado -----> {folder_path}")
                
                confirmation = input(f"¿Deseas eliminar este directorio? (s/n): ").strip().lower()
                if confirmation == 's':
                    delete_folder(folder_path)
                else:
                    print(f"El directorio no ha sufrido cambios.")
                    # Excluir el directorio para evitar que os.walk entre en él
                    dirs.remove(folder)

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path, onerror=on_rm_error)  # Usa el callback
        print(f"Se eliminó la carpeta: {folder_path}")
    except Exception as e:
        print(f"Error al eliminar {folder_path}: {e}")

def on_rm_error(func, path, exc_info):
    """
    Callback para manejar errores al eliminar archivos.
    """
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)  # Dar permisos de escritura
        func(path)  # Reintentar la operación
    else:
        raise  # Relanzar la excepción si no es un problema de permisos
