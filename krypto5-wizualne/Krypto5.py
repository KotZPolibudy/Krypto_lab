from PIL import Image
import random

choices = [(0, 1), (1, 0)]


def image_to_rgb_array(image_path):
    img = Image.open(image_path)
    # img = img.resize((100, 100))  # Resize the image to 100x100 pixels, if needed
    rgb_array = list(img.getdata())  # Get RGB values of all pixels
    return rgb_array


def convert_to_black_and_white(rgb_array, width, height, preserve_alpha=False):
    bw_array = []
    for pixel in rgb_array:
        # If preserving alpha channel, keep it unchanged
        if preserve_alpha:
            grayscale_value = sum(pixel[:3]) // 3
            bw_pixel = (grayscale_value, grayscale_value, grayscale_value, pixel[3])
        else:
            # Average the RGB values to get a grayscale value
            grayscale_value = sum(pixel[:3]) // 3
            # Set all three channels (R, G, B) to the grayscale value
            bw_pixel = (grayscale_value, grayscale_value, grayscale_value)
        bw_array.append(bw_pixel)

    # Create a new image from the black and white array
    # bw_image = Image.new('RGBA' if preserve_alpha else 'RGB', (width, height))
    # bw_image.putdata(bw_array)
    # return bw_image
    return bw_array


# def convert_to_black_or_white(greyscale_array, width, height, threshold=128):
def threshold_on_black_and_white(greyscale_array, width, height, threshold=128):
    bw_array = []
    for pixel in greyscale_array:
        # If grayscale value is above the threshold, set it to white (255), otherwise black (0)
        bw_value = 255 if pixel[0] > threshold else 0
        # Create a black or white pixel tuple
        bw_pixel = (bw_value, bw_value, bw_value)
        bw_array.append(bw_pixel)

    # Create a new image from the black and white array
    # bw_image = Image.new('RGB', (width, height))
    # bw_image.putdata(bw_array)
    # return bw_image
    return bw_array


def make_bit_array(pixel_array, threshold=128):
    bit_array = []
    for pixel in pixel_array:
        bit = 1 if pixel[0] > threshold else 0
        bit_array.append(bit)
    return bit_array


def adjust_secret(sec):
    sec_array = []
    for choice in sec:
        for bit in choice:
            color = 255 if bit == 1 else 0
            pix = (color, color, color)
            sec_array.append(pix)
    return sec_array


def add_second_panel_pixel_for_bit(pixel):
    if pixel == 1:
        u1 = random.choice(choices)
        u2 = choices[choices.index(u1)]
        return u1, u2
    else:
        u1 = random.choice(choices)
        choices.remove(u1)
        u2 = random.choice(choices)
        choices.append(u1)
        return u1, u2


def split_secret_from_bit_array(bits):
    u1 = []
    u2 = []
    for bit in bits:
        p1, p2 = add_second_panel_pixel_for_bit(bit)
        u1.append(p1)
        u2.append(p2)
    return u1, u2


def unsecret_the_secrets(s1, s2):
    final = []
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            final.append((255, 255, 255))
        else:
            final.append((0, 0, 0))
    return final


def putOnSections(u1, u2):
    last = []
    black = (0, 0, 0)
    for i in range(len(u1)):
        if(u1[i] == u2[i]):
            last.append(u1[i])
        else:
            last.append(black)
    return last


def Create_image(pixel_array, isAlpha=False, width=100, height=100):
    image = Image.new('RGBA' if isAlpha else 'RGB', (width, height))
    image.putdata(pixel_array)
    image.show()
    return image


# image_paths = ["krypto_obraz_1.png", "krypto_obraz_2.png"]
image_paths = ["krypto_obraz_2.png"]
for image_path in image_paths:
    rgb_array = image_to_rgb_array(image_path)
    # print(rgb_array[:10])  # Print the first 10 RGB values as a sample
    bw_image = convert_to_black_and_white(rgb_array, 100, 100)
    greyscale_array = convert_to_black_and_white(rgb_array, 100, 100)
    bw_array = threshold_on_black_and_white(greyscale_array, 100, 100, threshold=128)
    bit_array = make_bit_array(bw_array, threshold=128)
    secret1, secret2 = split_secret_from_bit_array(bit_array)
    secret1_bw = adjust_secret(secret1)
    secret2_bw = adjust_secret(secret2)

    # Create_image(greyscale_array)
    Create_image(bw_array)
    # print the secret
    print(bit_array)

    # print the split secret
    print(secret1)
    print(secret2)

    Create_image(secret1_bw, width=200)
    Create_image(secret2_bw, width=200)

    final_form = unsecret_the_secrets(secret1, secret2)
    Create_image(final_form)

    final_put = putOnSections(secret1_bw, secret2_bw)
    Create_image(final_put, width=200)
