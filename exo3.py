class MyImage :
    def __init__(self, size, format, color):
        self.size = size
        self.format = format
        self.color = color

image1 = MyImage("1900*1024", "jpg", "blue")

print(image1.color)
print(image1.format)



