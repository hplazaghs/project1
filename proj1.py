import statistics
from PIL import  Image

#GITHUB LINK
#https://github.com/hplazaghs/project1



img1 = Image.open ("images/1.png")
img2 = Image.open ("images/2.png")
img3 = Image.open ("images/3.png")
img4 = Image.open ("images/4.png")
img5 = Image.open ("images/5.png")
img6 = Image.open ("images/6.png")
img7 = Image.open ("images/7.png")
img8 = Image.open ("images/8.png")
img9 = Image.open ("images/9.png")

imgList = [img1, img2, img3, img4, img5, img6, img7, img8, img9]

imgWidth = img1.size[0]
imgLength = img1.size[1]

redMedPixel = 0
greenMedPixel = 0
blueMedPixel = 0

redPixList = []
greenPixList = []
bluePixList = []

newImg = Image.new("RGBA", (imgWidth, imgLength), "White")

for x in range(0, imgWidth):
  for y in range(0, imgLength):
    for image in imgList:
      red, green, blue = image.getpixel((x,y))
      
      redPixList.append(red)
      greenPixList.append(green)
      bluePixList.append(blue)
      
    redMedPixel = statistics.median(redPixList)
    greenMedPixel = statistics.median(greenPixList)
    blueMedPixel = statistics.median(bluePixList)
      
    redPixList = []
    greenPixList = []
    bluePixList = []
      
    newImg.putpixel((x,y), (redMedPixel, greenMedPixel, blueMedPixel))
      
newImg.save("combinedImage.png")
print("Success")
      
      
      
      





