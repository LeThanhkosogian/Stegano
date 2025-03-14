from PIL import Image
import numpy as np
import sys

# Message to hide
MESSAGE = "ToiYeuPTIT"


# Convert message to binary
def message_to_binary(message):
    return "".join(format(ord(char), "08b") for char in message)


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


# Encode message into image using PVD (keeping color)
def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    pixels = np.array(image)
    binary_message = message_to_binary(message) + "1111111111111110"  # End delimiter
    bit_index = 0

    for i in range(0, pixels.shape[0] - 1, 2):
        for j in range(0, pixels.shape[1] - 1, 2):
            if bit_index >= len(binary_message):
                break

            for channel in range(3):  # Process R, G, B separately
                p1 = pixels[i, j, channel]
                p2 = pixels[i, j + 1, channel]
                d = abs(p2 - p1)
                bit_capacity = get_bit_capacity(d)

                if bit_index + bit_capacity <= len(binary_message):
                    secret_bits = binary_message[bit_index : bit_index + bit_capacity]
                    bit_index += bit_capacity
                else:
                    secret_bits = binary_message[bit_index:] + "0" * (
                        bit_capacity - len(binary_message) + bit_index
                    )
                    bit_index = len(binary_message)

                secret_value = int(secret_bits, 2)
                new_d = d + secret_value if p2 >= p1 else d - secret_value

                if p2 >= p1:
                    p2 = p1 + new_d
                else:
                    p2 = p1 - new_d

                pixels[i, j + 1, channel] = np.clip(p2, 0, 255)

    encoded_image = Image.fromarray(pixels)
    encoded_image.save(output_path)
    print(f"Message encoded and saved as {output_path}")


# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hide_message.py <message>")
        sys.exit(1)
    
    MESSAGE = sys.argv[1]
    
    encode_image(
        "/home/ubuntu/steg-artifact/normal.png",
        MESSAGE,
        "/home/ubuntu/steg-artifact/steg.png",
    )
