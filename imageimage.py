import sys
import os
import argparse
import numpy as np
from PIL import Image 

def print_custom_help():
    """
    Prints a custom help message.
    """
    help_text = """
    imageimage.py

    A Python program to convert images into ASCII image representations.

    Usage:
        python imageimage.py --file <image_path> --scale <float> --ascii_cols <int> --symbols <string> --out <path> --font_color <str> --font_type <str>

    Options:
        --file         Path to the input image file (required).
        --scale        Scaling factor for image height (default: 0.43).
        --ascii_cols   Number of ASCII columns (default: 100).
        --symbols      Symbols to use for ASCII art.
        --out          Output path (default: ./results).
        --font_color   Font color for output image (e.g., "black").
        --font_type    Font type (e.g., "Courier").
    
    Author:
        agarnung
    """
    print(help_text)

def main():
    if '--help' in sys.argv:
        print_custom_help()
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False, default=0.43, type=float)
    parser.add_argument('--ascii_cols', dest='ascii_cols', required=False, default=100, type=int)
    parser.add_argument('--symbols', dest='symbols', required=False, default="@%#*+=-:. ")
    parser.add_argument('--out', dest='out', required=False, default='./results')
    parser.add_argument('--font_color', dest='font_color', required=False, default='black')
    parser.add_argument('--font_type', dest='font_type', required=False, default='Courier')

    args = parser.parse_args()

    output_dir = args.out
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image = Image.open(args.imgFile)
    scale = args.scale

    print(f"Input image dimensions: {image.size[0]} x {image.size[1]}")
    print("Generating image art...")

    #,,,

    print(f"Result saved in {output_dir}")

if __name__ == '__main__':
    main()
	
