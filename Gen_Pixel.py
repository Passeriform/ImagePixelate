import cv2
import argparse
import numpy as np


def Brightness_Contrast_Fix(image, brightness = 0, contrast = 0):

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = float(highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(image, alpha_b, image, 0, gamma_b)
    else:
        buf = image.copy()

    if contrast != 0:
        f = float(131*(contrast + 127))/(127*(131-contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    if(debug==1):
        cv2.namedWindow("B_C_Fix", cv2.WINDOW_KEEPRATIO)
        cv2.imshow("B_C_Fix", buf)
        x = cv2.waitKey(0)
        if x == 27:
            cv2.destroyWindow('B_C_Fix')

    return buf


def HSV_Fix(image, hue = 0, sat = 0, val = 0):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype("float32")
    (h, s, v) = cv2.split(hsv)
    h = h + hue
    s = s + sat
    v = v + val
    h = np.clip(h, 0, 255)
    s = np.clip(s, 0, 255)
    v = np.clip(v, 0, 255)
    hsv = cv2.merge([h, s, v])
    rgb = cv2.cvtColor(hsv.astype("uint8"), cv2.COLOR_HSV2BGR)

    if(debug==1):
        cv2.namedWindow("HSV_Fix", cv2.WINDOW_NORMAL)
        cv2.imshow("HSV_Fix", rgb)
        x = cv2.waitKey(0)
        if x == 27:
            cv2.destroyWindow('HSV_Fix')

    return rgb


def Reduce_Colors(image, colorsplits = 64):
    minVal = 255/colorsplits
    reduced = np.round(image.astype("float32")/minVal)*minVal
    reduced = reduced.astype("uint8")

    if(debug==1):
        cv2.namedWindow("Reduced_Colors", cv2.WINDOW_NORMAL)
        cv2.imshow("Reduced_Colors", reduced)
        x = cv2.waitKey(0)
        if x == 27:
            cv2.destroyWindow('Reduced_Colors')

    return reduced


def Pixelate(image, intensity = 50):
    h, w = image.shape[:2]
    if(PixelateIntensity==-1):
        if(h>w): intensity = h/125
        else: intensity = w/125
    shrunk = cv2.resize(image  , (h/intensity , w/intensity), interpolation=cv2.INTER_CUBIC)
    cv2.namedWindow("Pixelated", cv2.WINDOW_NORMAL)
    cv2.imshow("Pixelated", shrunk)
    x = cv2.waitKey(0)
    if x == 27:
        cv2.destroyWindow('Pixelated')

    return shrunk


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create pixelart from image')
    parser.add_argument('origin', help='Source of image file (JPG/PNG/TIFF/BMP supported)')
    parser.add_argument('-d', '--destination', help='Source of image file (JPG/PNG/TIFF/BMP supported)')
    parser.add_argument('-g', '--hue', help='Set hue mod', type=int, default=0)
    parser.add_argument('-s', '--saturation', help='Set saturation mod', type=int, default=20)
    parser.add_argument('-l', '--value', help='Set value mod', type=int, default=0)
    parser.add_argument('-b', '--brightness', help='Set brightness mod', type=int, default=30)
    parser.add_argument('-c', '--contrast', help='Set contrast mod', type=int, default=20)
    parser.add_argument('-cs', '--csplit', help='Define number of colors in cube root', type=int, default=5)
    parser.add_argument('-i', '--intensity', help='Intensity of pixelation (Put -1 for autopixelation)', type=int, default=-1)
    parser.add_argument('-v', '--debug', help='Debugging for intermediate verbosity', default=0, action='store_true')
    args = parser.parse_args()

    file = getattr(args, 'origin')
    saturation = args.saturation
    value = args.value
    hue = args.hue
    brightness = args.brightness
    contrast = args.contrast
    channelSplits = args.csplit
    PixelateIntensity = args.intensity
    if (args.debug):
        debug = 1
    else:
        debug = 0


    img = cv2.imread(file)

    cv2.namedWindow("original", cv2.WINDOW_NORMAL)
    cv2.imshow("original" , img)

    hsvfix = HSV_Fix(img, hue, saturation, value);
    contrasted = Brightness_Contrast_Fix(hsvfix, brightness, contrast)
    reduced = Reduce_Colors(contrasted, channelSplits)
    pixelated = Pixelate(reduced, PixelateIntensity)

    if(not args.destination): outpath = 'pixelated-'+args.origin[args.origin.rfind('/')+1:args.origin.find('.')]+'.png'
    cv2.imwrite(r'ss.png', pixelated)