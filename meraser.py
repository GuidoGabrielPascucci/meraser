import sys
from validate_functions import *
from cleaner_functions import find_and_remove

def main():
    try:
        if not validate_args(sys.argv):
            raise ValueError()
        directory = sys.argv[1]
        if not validate_dir(directory):
            raise NotADirectoryError(directory)
        find_and_remove(directory)
    except ValueError:
        print("Usage: meraser <path>")
        sys.exit(1)
    except NotADirectoryError as directory_err:
        print(f"Error: La ruta '{directory_err}' no es un directorio válido.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nSalida del programa solicitada por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    print()
