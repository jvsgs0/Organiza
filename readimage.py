import cv2

img = cv2.imread("C:/Users/User/Desktop/read_image/Pokemondo.png")

cv2.imshow("Imagem de exibicao", img)
print(img)
cv2.waitKey(0)



gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("Preto e branco", gray_img)

print(gray_img)

cv2.waitKey(0)