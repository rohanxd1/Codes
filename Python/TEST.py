from PIL import Image
img=Image.open(r"C:\Users\rohan\Downloads\Pictures\IMG_5093.jpg")
height=img.height
width=img.width
print(f"Height:{height}  Width:{width}")
r,g,b=img.getpixel((100,100))
print(f"R:{r} G:{g} B:{b}")
img2=img.convert("L")
img2.show()
img2=img2.save(r"C:\Users\rohan\Downloads\Pictures\test2.jpeg")
img3=img.rotate(180)
img3.show()
img3=img3.save(r"C:\Users\rohan\Downloads\Pictures\test3.jpeg")
