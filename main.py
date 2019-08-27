import image as img
# import OpenCV_image as img


img_base = '.\\imagem\\completa'
img_comparsion = '.\\imagem\\completa_dist'
ext = '.jpeg'
x = []
pixels = []


def main(imgs):
    for i in imgs:
        img.load_image(i + ext)
        pixel_left = img.find_pixel_left(img.width, img.height)
        pixel_right = img.find_pixel_right(pixel_left)
        x.append(img.count_pixel([pixel_left[0], pixel_right]))
        pixels.append([pixel_left, [pixel_right, pixel_left[1]]])
        img.red_mark(pixel_left, pixel_right, i, ext)
    print_result()


def print_result():
    print(f"-----------------------------------------------\n"
          f"DADOS DA IMAGEM BASE:\n"
          f"Posição dos Pixels:\n"
          f"==> Esquerdo: {pixels[0][0]}; Direito: {pixels[0][1]}\n"
          f"Comprimento: {x[0]} pixels\n"
          f"-----------------------------------------------\n"
          f"DADOS DA IMAGEM DE COMPARAÇÃO:\n"
          f"Posição dos Pixels:\n"
          f"==> Esquerdo: {pixels[1][0]}; Direito: {pixels[1][1]}\n"
          f"Comprimento: {x[1]} pixels\n"
          f"-----------------------------------------------")
    img.distortion(x[1] - x[0])


main([img_base, img_comparsion])
