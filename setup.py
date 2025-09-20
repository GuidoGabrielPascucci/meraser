from setuptools import setup, find_packages

setup(
    name="meraser",
    version="1.0.0",
    description="Herramienta para limpiar directorios node_modules y vendor",
    author="Guido Gabriel Pascucci",
    author_email="guidogpascucci@gmail.com",
    packages=find_packages(),
    py_modules=['meraser', 'cleaner_functions', 'validate_functions'],
    entry_points={
        'console_scripts': [
            'meraser=meraser:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)