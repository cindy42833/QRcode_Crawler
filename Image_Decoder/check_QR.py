# Import Library
import cv2
import glob
import sys
import os
import pandas as pd
import numpy as np
from PIL import Image
import zxing


def main():

    input_images_directory = os.path.abspath("/home/server/QRcode_Crawler/Image_Crawler/Imagecapture/spiders/output/images") + '/' + sys.argv[1] + '/'
    input_images_list_directory = os.path.abspath("/home/server/QRcode_Crawler/Image_Crawler/Imagecapture/spiders") + '/' + sys.argv[2] 

    col_list = ["category", "image_name", "image_urls", "indomain", "layer", "relative_path"] 

    # Read a image info
    df = pd.read_csv(input_images_list_directory, usecols = col_list, encoding = 'unicode_escape')
    image_list = df["image_name"].tolist()

    for item in image_list:
        full_filename =  input_images_directory + item
        # read the QRCODE image
        image = cv2.imread(full_filename)
        #image = cv2.imread(sys.argv[1])

        # If read image not success
        if image is None:
            print("Empty: " + full_filename) 
            #print("Empty: " + sys.argv[1])

        # If read image success
        else:
            print("READ")
            reader = zxing.BarCodeReader()
            barcode = reader.decode(full_filename)
            #barcode = reader.decode(sys.argv[1])
            print(barcode.parsed)
            print(": " + item)
            # initialize the cv2 QRCode detector
            # detector = cv2.QRCodeDetector()
            # # detect and decode
            # data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
            # # if there is a QR code
            # # print the data
            # if vertices_array is not None:
            #     print(filename + " data:")
            #     print(data)
            # else:
            #     print(filename + ": not qrcode")

if __name__ == "__main__":
    main()
