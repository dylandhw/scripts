from PIL import Image
from rich.console import Console
from rich_pixels import Pixels

console = Console()

with Image.open("three-colors-red.jpg") as image:
    pixels = Pixels.from_image(image)
    console.print(pixels)
