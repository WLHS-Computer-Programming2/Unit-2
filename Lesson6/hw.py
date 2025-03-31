from PIL import Image, ImageFilter

Hippo = Image.open(r"Lesson6\Hippo.jpg")
upside_down = Hippo.transpose(Image.FLIP_TOP_BOTTOM)
upside_down.show()
rotated_hippo = Hippo.rotate(45)
rotated_hippo.show()
rotated_img = Hippo.rotate(45, expand=True)
rotated_img.show()
img_gray = Hippo.convert("L")
edges = img_gray.filter(ImageFilter.FIND_EDGES)
edges.show()