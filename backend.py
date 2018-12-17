import cv2
import numpy as np

def load(obj, imagename="name", save="filename"):
        success, image = obj.video.read()
        im = cv2.imread("GameTemplate/"+ imagename + ".jpg")
        image = np.resize(image,(720,1280,3))
        image = cv2.flip(image, 1)
        dst = cv2.addWeighted(image,0.7,im,0.3,0)
        cv2.imwrite("GameImage/" + save + ".jpg", image)
        ret, jpeg = cv2.imencode('.jpg', dst)
        return jpeg.tobytes()

def loadpic(obj, imagename="name"):
        success, image = obj.video.read()
        im = cv2.imread("GameTemplate/" + imagename + ".jpg")
        ret, jpeg = cv2.imencode('.jpg', im)
        return jpeg.tobytes()

def default(obj):
        success, image = obj.video.read()
        image = cv2.flip(image, 1)
        image = np.resize(image,(720,1280,3))
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

def resultpic(imagename="name", template="filename"):
	img = cv2.imread("GameTemplate/" + imagename + ".jpg")
	im = cv2.imread("GameImage/" + template + ".jpg")
	dst = cv2.addWeighted(img,0.9,im,0.1,0)
	ret, jpeg = cv2.imencode('.jpg', dst)
	return jpeg.tobytes()


