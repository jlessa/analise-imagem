from PIL import Image


img, pixels, width, height = [None, None, None, None]
black_color = (0, 0, 0)
white_color = (255, 255, 255)


def load_image(img_path):
    global img, pixels, width, height
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size
    filter_black_white()


def filter_black_white():
    for x in range(width):
        for y in range(height):
            # if sum(pixels[x, y])/3 < 127:
            if pixels[x, y][0] < 79 and pixels[x, y][1] < 79 and pixels[x, y][2] < 79:
                pixels[x, y] = black_color
            else:
                pixels[x, y] = white_color
    # hacker image white
    # pixels[width - 1, height - 1] = black_color


def find_pixel_left(w, h):
    found = False
    value = None
    for x in range(w):
        if found:
            break
        else:
            for y in range(h):
                if pixels[x, y] != white_color:
                    value = [x, y]
                    found = True
                    break
    return value


def find_pixel_right(i):
    pixel_left = 0
    for x in range(width-1, i[0], -1):
        if pixels[x, i[1]] != white_color:
            pixel_left = x
            break
    return pixel_left


def count_pixel(x):
    return x[1] - x[0] + 1


def distortion(x):
    #Resolução 960x1280
    print(f"DISTORÇÃO: {x} pixels ==> {x / 6.22} milímetros.")
