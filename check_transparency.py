from PIL import Image
import sys

try:
    img = Image.open(r"C:\Users\ajaya\Downloads\amazon-kindle-vector-logo-seeklogo\amazon-kindle-seeklogo.png")
    if img.mode == 'RGBA':
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            print("Transparent")
        else:
            print("Opaque")
    else:
        print("Opaque")
except Exception as e:
    print(f"Error: {e}")
