# Image dimensions
imgWidth = 400
imgHeight = 400

# Original image
_image = PImage()
drawImage = PImage()

# Image with the sorted pixels
sortedImage = PImage()
drawSortedImage = PImage()

# To verify if the index of the pixel's array has been visited before
pixelIndexSet = set()

# To search in 4-neighborhood clockwise
searchPositions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Tuple -> (y, x, value, search position to start)
stack = [(0, 0, 1, 0)]

pixelIndex = 0

def setup():
    global imgHeight, imgWidth
    global _image, drawImage
    global sortedImage, drawSortedImage

    # Load the original image and its pixels
    _image = loadImage("fe-4x4.jpg")
    _image.loadPixels()
    
    # Set dimensions
    size(800, 400)
    
    # Create sorted image by brightness
    sortedImage = _image.get()
    sortedImage.pixels = sorted(sortedImage.pixels, key = lambda _color: brightness(_color))
    sortedImage.updatePixels()
    
    # Create images to draw
    drawImage = createImage(imgWidth, imgHeight, RGB)
    drawSortedImage = createImage(imgWidth, imgHeight, RGB) 
    
    
def draw():
    global imgWidth, imgHeight
    global _image, drawImage
    global sortedImage, drawSortedImage
    global searchPositions
    global pixelIndexSet
    global stack
    global pixelIndex
    
    background(0)
    
    if stack != []:
        _image.loadPixels()
        sortedImage.loadPixels()
        
        # Get position (and value) to search in
        state = stack.pop()
        
        # Get values of the position
        y = state[0]
        x = state[1]
        value = state[2]
        startAt = state[3]
        
        # Ged the index of the pixel in the spiral
        spiralIndex = x + y * imgWidth
        if spiralIndex not in pixelIndexSet:
            # Add pixel coordinate to the visited positions
            pixelIndexSet.add(spiralIndex)
            
            drawImage.pixels[spiralIndex] = _image.pixels[spiralIndex]
            
            # Put the i-th sorted image's pixel into the spiral index
            drawSortedImage.pixels[spiralIndex] = sortedImage.pixels[pixelIndex] 
            pixelIndex = pixelIndex + 1
            
            # Search for the next cell
            for i in reverse(range(0, 4)):
                currentSearchPosition = (startAt + i) % 4
                k = searchPositions[currentSearchPosition][0]
                h = searchPositions[currentSearchPosition][1]
            
                if isValidCell(y + k, x + h):
                    # Keep the search direction 
                    stack.append((y + k, x + h, value + 1, currentSearchPosition))
        
        # Update both images to draw
        drawImage.updatePixels()
        drawSortedImage.updatePixels()

    # Draw images    
    image(drawImage, 0, 0)
    image(drawSortedImage, imgWidth, 0)
    
        
def isValidCell(y, x):
    global imgWidth, ImgHeight
    # Check if the position is into the bounds of the array as matrix
    return x >= 0 and x < imgWidth and y >= 0 and y < imgHeight 