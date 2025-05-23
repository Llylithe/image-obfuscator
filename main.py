from PIL import Image
import numpy as np

def generate_shares(image_path):
    img = Image.open(image_path).convert("RGB")
    data = np.array(img, dtype=np.uint8)

    share_a = np.random.randint(0, 256, size=data.shape, dtype=np.uint8)
    temp_a = share_a.astype(np.int16)
    temp_data = data.astype(np.int16)

    share_b = (temp_data - temp_a) % 256
    share_b = share_b.astype(np.uint8)

    Image.fromarray(share_a).save("share_a.png")
    Image.fromarray(share_b).save("share_b.png")

    print("Shares generated: share_a.png, share_b.png")

def reconstruct_image(share_a_path, share_b_path):
    a = np.array(Image.open(share_a_path).convert("RGB"), dtype=np.uint16)
    b = np.array(Image.open(share_b_path).convert("RGB"), dtype=np.uint16)

    reconstructed = (a + b) % 256
    Image.fromarray(reconstructed.astype(np.uint8)).save("reconstructed.png")
    print("Reconstructed image saved as reconstructed.png")

# Call the functions with string filenames
generate_shares("bathtub.jpg")
reconstruct_image("share_a.png", "share_b.png")
