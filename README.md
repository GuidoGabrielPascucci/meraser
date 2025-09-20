# MEraser

Herramienta para limpiar automáticamente directorios `node_modules` y `vendor` de proyectos de desarrollo.

## ¿Para qué sirve?

- Encuentra recursivamente carpetas `node_modules` (Node.js) y `vendor` (PHP/Composer)
- Te pregunta antes de eliminar cada una
- Perfecto para hacer backups o liberar espacio en disco
- Las dependencias se pueden regenerar con `npm install` o `composer install`

## Instalación

### Opción 1: Instalación con pip (Recomendado)
```bash
git clone https://github.com/GuidoGabrielPascucci/meraser.git
cd meraser
pip install .
```

> **💡 Tip:** Usa `pip install --user .` para instalar solo para tu usuario (recomendado para evitar conflictos de permisos).

Después de la instalación, puedes usar `meraser` desde cualquier lugar:
```bash
meraser /ruta/a/tu/proyecto
```

### Opción 2: Instalación directa desde GitHub
```bash
pip install git+https://github.com/GuidoGabrielPascucci/meraser.git
```

> **💡 Tip:** Agrega `--user` si prefieres instalación a nivel usuario: `pip install --user git+...`

### Opción 3: Ejecución directa (sin instalar)
```bash
python meraser.py /ruta/a/tu/proyecto
```

## Uso

```bash
meraser /ruta/del/directorio/a/limpiar
```

**En Windows:**
```cmd
meraser C:\mis-proyectos
```

**En Linux/Mac:**
```bash
meraser ~/mis-proyectos
```

El programa:
1. Buscará recursivamente carpetas `node_modules` y `vendor`
2. Te mostrará cada una encontrada
3. Te preguntará si deseas eliminarla
4. Eliminará solo las que confirmes

## Ejemplo

```
$ meraser C:\mis-proyectos

Directorio detectado -----> C:\mis-proyectos\proyecto1\node_modules
¿Deseas eliminar este directorio? (s/n): s
Se eliminó la carpeta: C:\mis-proyectos\proyecto1\node_modules

Directorio detectado -----> C:\mis-proyectos\proyecto2\vendor
¿Deseas eliminar este directorio? (s/n): n
El directorio no ha sufrido cambios.
```

## Desinstalación

```bash
pip uninstall meraser
```

## Licencia

MIT License