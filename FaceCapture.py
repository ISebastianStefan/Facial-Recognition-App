import face_recognition
import cv2
from PIL import Image, ImageDraw, ImageFont

# Capturarea imaginilor de la camera web
camera = cv2.VideoCapture(0)
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite('student' + str(i) + '.png', image)
del(camera)

# Încărcarea imaginii cu un student specific (în acest caz, student5.png)
uk = face_recognition.load_image_file('student5.png')

print(uk.shape)

# Găsirea locațiilor fețelor în imagine
l = face_recognition.face_locations(uk, model='hog') # model poate fi 'hog' sau 'cnn'
print(l)

# Extrage coordonatele colțurilor feței
top = l[0][0]
right = l[0][1]
bottom = l[0][2]
left = l[0][3]

# Inițializarea unui obiect Image dintr-un numpy array (imaginea cu studentul)
uk_image = Image.fromarray(uk)

# Inițializarea unui obiect ImageDraw pentru desenarea pe imagine
draw = ImageDraw.Draw(uk_image)

# Desenarea unui dreptunghi în jurul feței
draw.rectangle(
    (left, top, right, bottom),
    outline=(0, 0, 255),
    width=4
)

# Adăugarea unui text pentru identificarea feței ca "Unknown"
fnt = ImageFont.truetype("arial", 40)
draw.text((left+50, bottom-5), "Unknown", font=fnt, fill=(255, 0, 0))

# Afișarea imaginii modificată
# uk_image.show()
