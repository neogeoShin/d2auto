from PIL import ImageGrab
#from PIL import ImageFilter
import pygetwindow as gw
#import pyocr
import easyocr
import numpy
import cv2

boundaries = [      
    ([50, 200, 50], [100, 255, 100]),    #set item
    ([60, 60, 120], [200, 200, 255]),    #magic item
]

def within_pixel(list1, list2, list3):
    for i in range(3):
        if list1[i] < list2[i] or list1[i] > list3[i]:
            return False
    return True

if __name__ == "__main__":
    # Get the window with the title "Your Window Title"
    window = gw.getWindowsWithTitle("Diablo II: Resurrected")[0]
    # make that window front
    window.activate() 

    # Get the window coordinates
    x1, y1, x2, y2 = window.left, window.top, window.left + window.width, window.top + window.height

    # Capture the specified window
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    pixel = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)

    # change image tone

    #for x in range(im.size[0]):
    #    for y in range(im.size[1]):
    #        for z in range(len(boundaries)):
    #            if within_pixel(pixel[x,y], boundaries[z][0], boundaries[z][1]):
    #                pixel[x,y] = (200, 200, 200)

    #for debug
    #im.show()

    #sharp the image
    #sharpened_im = im.filter(ImageFilter.SHARPEN);


    # init OCR module
    #tools = pyocr.get_available_tools()
    # use tessertact as OCR module
    #tool = tools[0]


    #builder = pyocr.builders.TextBuilder()
    #result = tool.image_to_string(im, lang="kor+eng", builder=builder)

    # use easy ocr
    reader = easyocr.Reader(['ko','en'], gpu=True)
    result = reader.readtext(pixel)

    print(result)
