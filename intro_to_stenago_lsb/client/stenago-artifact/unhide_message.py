from PIL import Image
import numpy as np

# Unhide message from image
def decode_image(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    binary_message = ""
    for row in image_array:
        for pixel in row:
            for color_value in pixel[:3]:
                binary_message += str(color_value & 1)

    # Extract message until delimiter
    delimiter = "1111111111111110"
    message_bits = binary_message.split(delimiter)[0]

    # Convert binary to text
    decoded_message = "".join(
        chr(int(message_bits[i : i + 8], 2)) for i in range(0, len(message_bits), 8)
    )
    print(f"Decoded message: {decoded_message}")


# Example usage
decode_image("/home/ubuntu/stenago-artifact/stenago.png")
