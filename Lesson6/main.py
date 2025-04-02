from PIL import Image, ImageFilter, ImageEnhance

orange_cat = Image.open(r"Lesson6\Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg")
blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.save(r"Lesson6\blurry_cat.jpg")
bw_cat = ImageEnhance.Color(orange_cat).enhance(0).save(r"Lesson6\bw_cat.jpg")
bright_cat = ImageEnhance.Color(orange_cat).enhance(10).save(r"Lesson6\bright_cat.jpg")
