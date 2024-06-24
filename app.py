import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Iniciar captura de vídeo
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = FaceDetector(minDetectionCon=0.5)

while True:
    _, img = video.read()
    img, bboxes = detector.findFaces(img, draw=False)
    img2 = img.copy()
    if bboxes:
        for bbox in bboxes:
            x, y, w, h = bbox['bbox']
            # Verificar se as coordenadas estão dentro dos limites da imagem
            if x >= 0 and y >= 0 and x+w <= img.shape[1] and y+h <= img.shape[0]:
                rec = img[y:y+h, x:x+w]
                # Verificar se a região não está vazia
                if rec.size > 0:
                    recBlur = cv2.blur(rec, (30, 30))
                    img2[y:y+h, x:x+w] = recBlur

    cv2.imshow('IMG', img)
    cv2.imshow('IMG2', img2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
