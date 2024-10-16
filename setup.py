from setuptools import setup, find_packages

setup(
    name='imagem_simples_processamento',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Dependência necessária para manipulação de imagens
    ],
)
