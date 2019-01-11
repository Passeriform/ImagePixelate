# ImagePixelate
A basic image pixelation utility

## Usage:

Gen_Pixel.py  [-h] origin [-d DESTINATION] [-g HUE] [-s SATURATION] [-l VALUE]
              [-b BRIGHTNESS] [-c CONTRAST] [-cs CSPLIT] [-i INTENSITY]
              [-v]

Create pixelart from image

positional arguments:
  origin                Source of image file (JPG/PNG/TIFF/BMP supported)

optional arguments:
  -h, --help                                          show this help message and exit
  
  -d DESTINATION, --destination DESTINATION           Source of image file (JPG/PNG/TIFF/BMP supported)
                        
  -g HUE, --hue HUE                                   Set hue mod
  
  -s SATURATION, --saturation SATURATION              Set saturation mod
  
  -l VALUE, --value VALUE                             Set value mod

  -b BRIGHTNESS, --brightness BRIGHTNESS              Set brightness mod
  
  -c CONTRAST, --contrast CONTRAST                    Set contrast mod
  
  -cs CSPLIT, --csplit CSPLIT                         Define number of colors in cube root
  
  -i INTENSITY, --intensity INTENSITY                 Intensity of pixelation (Put -1 for autopixelation)
  
  -v, --debug                                         Debugging for intermediate verbosity


Credit: https://www.shutterstock.com/blog/how-to-turn-any-photograph-into-pixel-art-with-photoshop
