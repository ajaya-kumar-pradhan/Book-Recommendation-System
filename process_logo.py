from PIL import Image
import numpy as np

def remove_white_bg(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path).convert("RGBA")
        data = np.array(img)
        
        # Define white threshold (e.g., pixels brighter than 240 in all channels)
        r, g, b, a = data.T
        white_areas = (r > 240) & (g > 240) & (b > 240)
        
        data[..., 3][white_areas.T] = 0
        
        new_img = Image.fromarray(data)
        new_img.save(output_path)
        print(f"Saved to {output_path}")
    except FileNotFoundError:
        print("Source logo file not found. Please ensure the path is correct.")

if __name__ == "__main__":
    input_logo = r"C:\Users\ajaya\Downloads\amazon-kindle-vector-logo-seeklogo\amazon-kindle-seeklogo.png"
    output_logo = r"C:\Users\ajaya\Downloads\kindle book\logo.png"
    remove_white_bg(input_logo, output_logo)
