from PIL import Image
img=Image.open(r"C:\Users\rohan\Downloads\Pictures\macro.jpeg")
height=img.height
width=img.width
print(f"Height:{height}  Width:{width}")
r,g,b=img.getpixel((100,100))
print(f"R:{r} G:{g} B:{b}")
img.show()