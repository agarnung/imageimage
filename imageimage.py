import sys
import os
import argparse
import numpy as np
from PIL import Image
from skimage.color import rgb2lab, rgb2gray
from skimage.filters import sobel
from tqdm import tqdm

def print_custom_help():
    help_text = """
    imageimage.py

    A Python program to convert images into image representations.

    Usage:
        python imageimage.py --file <image_path> --inputs <database_path> [options]

    Options:
        --file         Path to the input image file (required).
        --inputs       Path to the database of small images (required).
        --out          Output path (default: ./results).
        --width        Width of each small image in pixels (default: 32).
        --height       Height of each small image in pixels (default: 32).
        --cols         Number of columns in output image (default: auto-calculate).
        --rows         Number of rows in output image (default: auto-calculate).
        --color_weight Weight to give to color/grayscale similarity (default: 1.0).
        --gradient_weight Weight to give to gradient (edge) similarity (default: 1.0).
    
    Author:
        agarnung
    """
    print(help_text)

def load_image_database(database_path, target_size=(32, 32)):
    database_images = []
    lab_images = []
    gray_images = []

    if not os.path.exists(database_path):
        print(f"Error: Database directory '{database_path}' not found!")
        sys.exit(1)

    for filename in os.listdir(database_path):
        try:
            img_path = os.path.join(database_path, filename)
            img = Image.open(img_path).convert('RGB')
            img = img.resize(target_size, Image.LANCZOS)
            database_images.append(img)
            
            # Precompute both LAB and Grayscale versions
            np_img = np.array(img)
            lab_images.append(rgb2lab(np_img))
            gray_images.append(rgb2gray(np_img))
        except:
            continue

    if not database_images:
        print("Error: No valid images found in the database directory!")
        sys.exit(1)

    return database_images, lab_images, gray_images

def compute_color_similarity(target, db, is_grayscale):
    """Calcula la similitud de color o escala de grises"""
    if is_grayscale:
        return np.linalg.norm(target - db)
    else:
        return np.linalg.norm(target - db)

def compute_gradient_similarity(target, db):
    """Calcula la similitud de gradiente entre dos imágenes"""
    target_grad = sobel(target)
    db_grad = sobel(db)
    return np.sum(target_grad * db_grad) / (np.linalg.norm(target_grad) * np.linalg.norm(db_grad) + 1e-8)

def find_best_match(target_patch, database, database_lab, database_gray, 
                   color_weight=1.0, gradient_weight=1.0, is_grayscale=False):
    if is_grayscale:
        target_img = np.array(target_patch.convert('L'))
        target = target_img / 255.0  # Normalizar a [0,1]
        db_images = database_gray
    else:
        target_rgb = np.array(target_patch.convert('RGB')) / 255.0
        target = rgb2lab(target_rgb)
        db_images = database_lab

    best_score = float('inf')
    best_index = 0

    for i, db_img in enumerate(db_images):
        color_sim = compute_color_similarity(target, db_img, is_grayscale)
        
        # Para gradiente, usamos el canal L en color o la imagen completa en grises
        grad_input = target[:,:,0] if not is_grayscale else target_img
        grad_db = db_img[:,:,0] if not is_grayscale else (database_gray[i] * 255)
        gradient_sim = compute_gradient_similarity(grad_input, grad_db)
        
        score = (color_weight * color_sim + 
                 gradient_weight * (1 - gradient_sim))

        if score < best_score:
            best_score = score
            best_index = i

    return database[best_index]

def create_image_mosaic(input_image, database, database_lab, database_gray, output_size,
                       tile_size=(32, 32), color_weight=1.0, gradient_weight=1.0, 
                       is_grayscale=False):
    cols = output_size[0] // tile_size[0]
    rows = output_size[1] // tile_size[1]
    input_image = input_image.resize((cols * tile_size[0], rows * tile_size[1]), Image.LANCZOS)
    output_image = Image.new('RGB', (cols * tile_size[0], rows * tile_size[1]))

    for row in tqdm(range(rows), desc="Rows", ncols=100):
        for col in range(cols):
            left = col * tile_size[0]
            upper = row * tile_size[1]
            right = left + tile_size[0]
            lower = upper + tile_size[1]

            patch = input_image.crop((left, upper, right, lower))
            best_match = find_best_match(patch, database, database_lab, database_gray,
                                       color_weight=color_weight,
                                       gradient_weight=gradient_weight, 
                                       is_grayscale=is_grayscale)
            output_image.paste(best_match, (left, upper))

    if is_grayscale:
        output_image = output_image.convert('L')

    return output_image

def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        print_custom_help()
        sys.exit(0)

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', dest='imgFile', required=True, help='Input image file path')
    parser.add_argument('--inputs', dest='inputs', required=True, help='Path to database of small images')
    parser.add_argument('--out', dest='out', default='./results', help='Output directory path')
    parser.add_argument('--width', dest='width', type=int, default=32, help='Width of each small image')
    parser.add_argument('--height', dest='height', type=int, default=32, help='Height of each small image')
    parser.add_argument('--cols', dest='cols', type=int, default=None, help='Number of columns in output')
    parser.add_argument('--rows', dest='rows', type=int, default=None, help='Number of rows in output')
    parser.add_argument('--color_weight', dest='color_weight', type=float, default=1.0,
                       help='Weight to give to color/grayscale similarity. Default is 1.0')
    parser.add_argument('--gradient_weight', dest='gradient_weight', type=float, default=1.0,
                       help='Weight to give to gradient similarity (edges). Default is 1.0')

    args = parser.parse_args()

    output_dir = args.out
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        input_image = Image.open(args.imgFile)
        is_grayscale = input_image.mode == 'L'
        if not is_grayscale:
            input_image = input_image.convert('RGB')
    except Exception as e:
        print(f"Error loading input image: {e}")
        sys.exit(1)
        
    print(f"Input image dimensions: {input_image.size[0]} x {input_image.size[1]} | mode: {input_image.mode}")
    print("Loading image database...")

    tile_size = (args.width, args.height)
    database_images, database_lab, database_gray = load_image_database(args.inputs, tile_size)
    print(f"Loaded {len(database_images)} images from database")

    if args.cols and args.rows:
        output_size = (args.cols * tile_size[0], args.rows * tile_size[1])
    else:
        aspect = input_image.size[0] / input_image.size[1]
        if not args.cols and not args.rows:
            if input_image.size[0] > input_image.size[1]:
                cols = 50
                rows = int(cols / aspect)
            else:
                rows = 50
                cols = int(rows * aspect)
        elif args.cols:
            cols = args.cols
            rows = int(cols / aspect)
        else:
            rows = args.rows
            cols = int(rows * aspect)
        output_size = (cols * tile_size[0], rows * tile_size[1])

    print("Generating image art...")
    print(f"Output will be {output_size[0]} x {output_size[1]} with {tile_size[0]}x{tile_size[1]} tiles")

    mosaic = create_image_mosaic(
        input_image,
        database_images,
        database_lab,
        database_gray,
        output_size,
        tile_size,
        color_weight=args.color_weight,
        gradient_weight=args.gradient_weight,
        is_grayscale=is_grayscale
    )

    output_filename = os.path.join(
        output_dir,
        os.path.splitext(os.path.basename(args.imgFile))[0] + '_imageified.jpg'
    )

    mosaic.save(output_filename, quality=95)
    print(f"Result saved as {output_filename}")

if __name__ == '__main__':
    main()
