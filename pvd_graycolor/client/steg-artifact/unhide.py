from PIL import Image
import numpy as np

# Determine how many bits can be hidden based on pixel difference
def get_bit_capacity(d):
    if d < 16:
        return 2
    elif d < 32:
        return 3
    elif d < 64:
        return 4
    elif d < 128:
        return 5
    else:
        return 6

def unhide_message_in_image(image_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    binary_message = ""

    for i in range(0, pixels.shape[0] - 1, 2):
        for j in range(0, pixels.shape[1] - 1, 2):
            for channel in range(3):  # Extract from R, G, B separately
                p1 = pixels[i, j, channel]
                p2 = pixels[i, j + 1, channel]
                d = abs(p2 - p1)
                bit_capacity = get_bit_capacity(d)

                secret_bits = format(d, f"0{bit_capacity}b")
                binary_message += secret_bits

                if "1111111111111110" in binary_message:
                    break

    binary_message = binary_message.split("1111111111111110")[0]
    decoded_message = "".join(
        chr(int(binary_message[i : i + 8], 2)) for i in range(0, len(binary_message), 8)
    )
    return decoded_message

# Example usage
if __name__ == "__main__":
    image_path = input("Input the path to image: ")
    # image_path = "C:\\Users\\Admin\\Desktop\\Stegano\\temp\\pvd_graycolor\\server\\steg.png"
    hided_message = unhide_message_in_image(image_path)
    print("Message has been hidden in the image:", hided_message)
