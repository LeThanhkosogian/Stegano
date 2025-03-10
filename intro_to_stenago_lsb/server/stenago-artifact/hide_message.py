from PIL import Image
import numpy as np

# Message to hide
MESSAGE = "ToiYeuPTIT"


# Convert message to binary
def message_to_binary(message):
    return "".join(format(ord(char), "08b") for char in message)


# Hide message into image
def encode_image(image_path, message, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    binary_message = (
        message_to_binary(message) + "1111111111111110"
    )  # Delimiter to indicate end
    bit_index = 0

    for row in image_array:
        for pixel in row:
            for color_index in range(3):  # RGB channels
                if bit_index < len(binary_message):
                    pixel[color_index] = pixel[color_index] & 254 | int(
                        binary_message[bit_index]
                    )
                    bit_index += 1

    encoded_image = Image.fromarray(image_array)
    encoded_image.save(output_path)
    print(f"Message encoded and saved as {output_path}")


# Example usage
encode_image(
    "/home/ubuntu/stenago-artifact/normal.png",
    MESSAGE,
    "/home/ubuntu/stenago-artifact/stenago.png",
)
