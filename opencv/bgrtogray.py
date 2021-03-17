import cv2 as cv

class GrayScale():

    def GrayScaling(self,filename):
        img = cv.imread(filename)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(filename, gray)
        print("in gray_Scaling function")

# filename = 'C:\\Users\\jinal\\Documents\\Python training\\Image Processing\\files\\FrontFace.jpg'
# obj = GrayScale()
# obj.GrayScaling(filename)