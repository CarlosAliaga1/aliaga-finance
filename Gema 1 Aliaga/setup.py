from setuptools import setup

setup(
    name='aliaga-finance-pro',
    version='1.0.0',
    py_modules=['aliaga_calc'],
    install_requires=['colorama'],
    entry_points={
        'console_scripts': [
            'aliaga-calc=aliaga_calc:ejecutar_aliaga',
        ],
    },
    author='Dr. Carlos Aliaga Valdez',
    description='Herramienta de precisión financiera con estética profesional.',
)
