import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(256, 256)):
    """
    Resizes all images in the input directory to the specified size
    and saves them to the output directory.

    Args:
        input_dir (str): Path to the directory containing original images.
        output_dir (str): Path to the directory where resized images will be saved.
        size (tuple): A tuple (width, height) for the desired output size.
    """
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        return

    os.makedirs(output_dir, exist_ok=True)
    print(f"Resizing images from '{input_dir}' to '{output_dir}' with size {size}...")

    image_count = 0
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            try:
                with Image.open(input_path) as img:
                    # Resize the image
                    img_resized = img.resize(size, Image.LANCZOS) # LANCZOS is a high-quality downsampling filter

                    # Save the resized image
                    # Ensure correct format when saving (e.g., convert to RGB if needed)
                    if img_resized.mode == 'RGBA': # Convert RGBA to RGB before saving as JPG if needed
                        img_resized = img_resized.convert('RGB')
                    img_resized.save(output_path)
                    image_count += 1
                    print(f"Resized '{filename}' and saved to '{output_path}'")
            except Exception as e:
                print(f"Could not process '{filename}': {e}")

    print(f"\nFinished resizing {image_count} images.")

if __name__ == "__main__":
    original_images_dir = "dataset/images/train"
    resized_images_dir = "dataset/images/resized_train_256x256" 
    target_size = (256, 256)

    resize_images(original_images_dir, resized_images_dir, target_size)

