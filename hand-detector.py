import cv2
import mediapipe as mp
from deepface import DeepFace
import numpy as np

# Inisialisasi MediaPipe
mp_hands = mp.solutions.hands
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Inisialisasi model
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
face_detector = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

def detect_gesture(hand_landmarks):
    fingers = []
    
    # Ibu jari
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)
    
    # 4 jari lainnya
    for tip in [8, 12, 16, 20]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    
    total_fingers = sum(fingers)
    
    if total_fingers == 0:
        return "Genggam"
    elif total_fingers == 1:
        return "Satu"
    elif total_fingers == 2:
        return "Dua"
    elif total_fingers == 3:
        return "Tiga"
    elif total_fingers == 4:
        return "Empat"
    elif total_fingers == 5:
        return "Lima"
    
    return f"Jari: {total_fingers}"

def detect_emotion(image):
    try:
        result = DeepFace.analyze(image, 
                                 actions=['emotion'],
                                 enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        
        # Terjemahkan emosi ke Bahasa Indonesia
        emotion_dict = {
            'angry': 'Marah',
            'disgust': 'Jijik',
            'fear': 'Takut',
            'happy': 'Senang',
            'sad': 'Sedih',
            'surprise': 'Terkejut',
            'neutral': 'Netral'
        }
        
        return emotion_dict.get(emotion, emotion)
    except:
        return None

def main():
    cap = cv2.VideoCapture(0)
    
    # Untuk mengatur interval deteksi emosi (karena prosesnya berat)
    frame_count = 0
    emotion_result = None
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Flip horizontal untuk tampilan mirror
        image = cv2.flip(image, 1)
        
        # Konversi BGR ke RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Deteksi emosi setiap 30 frame
        frame_count += 1
        if frame_count % 30 == 0:
            emotion_result = detect_emotion(image)
        
        if emotion_result:
            cv2.putText(image, f'Emosi: {emotion_result}', (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        
        # Deteksi tangan
        hand_results = hands.process(image_rgb)
        if hand_results.multi_hand_landmarks:
            for hand_landmarks in hand_results.multi_hand_landmarks:
                # Gambar landmark tangan
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(0,0,255), thickness=2))
                
                # Deteksi dan tampilkan gesture
                gesture = detect_gesture(hand_landmarks)
                cv2.putText(image, gesture, (10, 70),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        # Deteksi wajah
        face_results = face_detector.process(image_rgb)
        if face_results.detections:
            for detection in face_results.detections:
                mp_drawing.draw_detection(image, detection)

        # Tampilkan hasil
        cv2.imshow('Deteksi Tangan, Wajah, dan Emosi', image)
        
        # Tekan ESC untuk keluar
        if cv2.waitKey(5) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()