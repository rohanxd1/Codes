from PIL import Image
img=Image.open(r"C:\Users\rohan\Downloads\Pictures\IMG_5093.jpg")
height=img.height
width=img.width
print(f"Height:{height}  Width:{width}")
r,g,b=img.getpixel((100,100))
print(f"R:{r} G:{g} B:{b}")
#img.show()

for i in range(width):
    avg=0
    for j in range(height):
        r,g,b=img.getpixel((i,j))
        avg=(r+g+b)/3
        if avg>=127:
            img.putpixel((i,j),(255,255,255))
        else:
            img.putpixel((i,j),(0,0,0))
img.show()
img=img.save(r"C:\Users\rohan\Downloads\Pictures\test4.jpeg")