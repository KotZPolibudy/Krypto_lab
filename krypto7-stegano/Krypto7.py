from PIL import Image


def image_to_rgb_array(image_path):
    img = Image.open(image_path)
    # img = img.resize((100, 100))  # Resize the image to 100x100 pixels, if needed
    rgb_array = list(img.getdata())  # Get RGB values of all pixels
    return rgb_array


def convertIntToBits(rgb):
    return "{:08b}".format(rgb)


def base2ToBase10(string):
    suma = 0
    ii = 0
    string = string[::-1]
    for i in range(len(string)):
        suma += int(string[i]) * pow(2, ii)
        ii += 1
    return suma


def changeRGB(msgbits, array, position):
    rgbPixel = array[position]
    rgbTmp = []
    for i in range(len(msgbits)):
        if i % 3 == 0 and i != 0:
            array[position] = (rgbTmp[0], rgbTmp[1], rgbTmp[2])
            rgbTmp.clear()
            position += 1
            rgbPixel = array[position]
        color = convertIntToBits(rgbPixel[i % 3])
        color = color[0:len(color) - 1]
        color += msgbits[i]
        color = base2ToBase10(color)
        rgbTmp.append(color)
        if i == len(msgbits) - 1 and len(rgbTmp) > 0:
            missing = 3 - len(rgbTmp)  # 0 or 1 or 2
            if missing == 0:
                array[position] = (rgbTmp[0], rgbTmp[1], rgbTmp[2])
            elif missing == 1:
                array[position] = (rgbTmp[0], rgbTmp[1], rgbPixel[2])
            elif missing == 2:
                array[position] = (rgbTmp[0], rgbPixel[1], rgbPixel[2])


# rawMessage = "I am a silly cat. Don't mind me"

rawMessage = "I am a silly cat. Don't mind me. This is going to be a hard message to decode, so I'll make it as long as I can, while it still fits. I just hope I can make it this long, as I am already running out of ideas what to write, and I'm getting home, so I need to get off the train and finish this code ASAP :D *MEOW*"
im = Image.open("Krypto_obraz_1.png", 'r').convert('RGB')
width, height = im.size
data = list(im.getdata())

# tutaj zamiana w bity i sprawdzenie długości, czy zmieścimy wiadomość na obrazku:
messageBits = ''.join(format(ord(i), '08b') for i in rawMessage)
print(f'messageBits = {len(messageBits)}, w*h*3 = {width * height * 3}')
if len(messageBits) > width * height * 3:
    print("AAAAA masz za długą wiadomość, albo za mały obrazek!")
assert len(messageBits) <= width * height * 3
# w ten sposób zostaje jeden bit wolny na znak, można by dodać parity check lub zapisywać cięgiem.
print(f'messageBits: {messageBits}\nrawMessage: {rawMessage}')
startPosition = 0

changeRGB(messageBits, data, startPosition)

# zapisz obraz
im = Image.new('1', (width, height)).convert('RGB')
for i in range(width):
    for j in range(height):
        im.putpixel((j, i), data[i * width + j])
im.save("wynikowy.png")

# odczytaj z zapisanego obrazu
msg = ""
im = Image.open("Krypto_obraz_1.png", 'r').convert('RGB')
width_wyn, height_wyn = im.size
data_wyn = list(im.getdata())

# czytaj bity
lastBits = ""
for i in range(width):
    for j in range(height):
        Pixel = data[i * width + j]
        lastBits += "1" if Pixel[0] % 2 == 1 else "0"
        lastBits += "1" if Pixel[1] % 2 == 1 else "0"
        lastBits += "1" if Pixel[2] % 2 == 1 else "0"

# na znaki
for i in range(int(len(lastBits) / 8)):
    msg += chr(int(lastBits[8 * i:8 * i + 8], 2))

encryptedMessage = msg[0:len(rawMessage)]
print("   Message:", encryptedMessage)
