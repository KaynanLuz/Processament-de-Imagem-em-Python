from imagem_simples import ImageProcessor

# Carregar uma imagem de exemplo
processor = ImageProcessor("imagem_test.jpg")

# Aplicar algumas manipulações e salvar
processor.resize(300, 300).grayscale().save("imagem_processada.jpg")
