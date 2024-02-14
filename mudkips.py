import cv2

# Carregar a imagem principal
img = cv2.imread("C:/Users/User/Desktop/read_image/Pokemondo.png")

# Selecionar a parte da imagem 'mudkip' da imagem principal
mudkip = img[120:360, 900:1000]

# Redimensionar a parte da imagem 'mudkip' para corresponder às dimensões da região em 'img'
mudkip_resized = cv2.resize(mudkip, (100, 240))

# Substituir a região em 'img' pela parte da imagem 'mudkip' redimensionada
img[0:240, 500:600] = mudkip_resized

# Adicionar texto à imagem 'img'
text_to_show = "mudkip!"
cv2.putText(img, text_to_show, (20, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(255, 0, 0))

# Exibir a imagem resultante
cv2.imshow("Mudkips", img)
cv2.waitKey(0)
