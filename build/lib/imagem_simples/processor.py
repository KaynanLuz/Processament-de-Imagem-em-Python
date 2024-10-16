from PIL import Image, ImageFilter

class ImageProcessor:
    def __init__(self, image_path):
        """Inicializa o processador com o caminho da imagem."""
        self.image = Image.open(image_path)

    def resize(self, width, height):
        """Redimensiona a imagem para as dimensões especificadas."""
        self.image = self.image.resize((width, height))
        return self

    def grayscale(self):
        """Converte a imagem para tons de cinza."""
        self.image = self.image.convert('L')
        return self

    def blur(self, radius=2):
        """Aplica um filtro de desfoque à imagem."""
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))
        return self

    def save(self, output_path):
        """Salva a imagem processada no caminho especificado."""
        self.image.save(output_path)

    def show(self):
        """Mostra a imagem atual."""
        self.image.show()
