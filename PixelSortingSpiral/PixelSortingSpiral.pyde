_image = PImage()
drawImage = PImage()
drawImageSet = set()

sortedImage = PImage()
drawSortedImage = PImage()
drawSortedImageSet = set()

imageWidth = 400
imageHeight = 400

stackImage = []
stackSortedImage = []

searchPositions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

index = 0

def setup():
    global _image, stackImage, stackSortedImage, drawImage, drawSortedImage, imageWidth, imageHeight, sortedImage
    _image = loadImage("fe-4x4.jpg")
    size(800, 400)
    # Tuple -> (y, x, value, startAt)
    drawImage = createImage(imageWidth, imageHeight, RGB)
    sortedImage = _image.get()
    sortedImage.loadPixels()
    sortedImage.pixels = sorted(sortedImage.pixels, key = lambda _color: brightness(_color)) 
    sortedImage.updatePixels()
    drawSortedImage = createImage(imageWidth, imageHeight, RGB) 
    stackImage.append((0, 0, 1, 0))
    stackSortedImage.append((0, 0, 1, 0))
    
def draw():
    global _image, sortedImage, imageWidth, imageHeight, stackImage, stackSortedImage, searchPositions, drawImageSet, drawSortedImage, drawSortedImageSet, index
    
    background(0)
    
    if stackImage != []:
        _image.loadPixels()
        state = stackImage.pop()
        
        # Get values of the state
        y = state[0]
        x = state[1]
        value = state[2]
        startAt = state[3]
        
        drawImage.loadPixels()
        _image.loadPixels() 
        
        realPosition = x + y * imageWidth
        if realPosition not in drawImageSet:
            drawImageSet.add(realPosition)
            drawImage.pixels[realPosition] = _image.pixels[realPosition]
        
            for i in reverse(range(0, 4)):
                currentSearchPosition = (startAt + i) % 4
                k = searchPositions[currentSearchPosition][0]
                h = searchPositions[currentSearchPosition][1]
            
                if isValidCell(y + k, x + h):
                    stackImage.append((y + k, x + h, value + 1, currentSearchPosition))
        
        drawImage.updatePixels()
        
    if stackSortedImage != []:
        sortedImage.loadPixels()
        state = stackSortedImage.pop()
        
        # Get values of the state
        y = state[0]
        x = state[1]
        value = state[2]
        startAt = state[3]
        
        drawSortedImage.loadPixels()
        sortedImage.loadPixels() 
        
        realPosition = x + y * imageWidth
        if realPosition not in drawSortedImageSet:
            drawSortedImageSet.add(realPosition)
            drawSortedImage.pixels[realPosition] = sortedImage.pixels[index]
            index = index + 1
            
            for i in reverse(range(0, 4)):
                currentSearchPosition = (startAt + i) % 4
                k = searchPositions[currentSearchPosition][0]
                h = searchPositions[currentSearchPosition][1]
            
                if isValidCell(y + k, x + h):
                    stackSortedImage.append((y + k, x + h, value + 1, currentSearchPosition))
        
        drawSortedImage.updatePixels()
        
    image(drawImage, 0, 0)
    image(drawSortedImage, 400, 0)
    
        
def isValidCell(y, x):
    global imageWidth, ImageHeight
    return x >= 0 and x < imageWidth and y >= 0 and y < imageHeight 