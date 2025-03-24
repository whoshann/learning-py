import pyttsx3

# Inisialisasi engine
engine = pyttsx3.init()

# Mengatur kecepatan pembicaraan
engine.setProperty('rate', 150)

# Fungsi untuk mengubah teks menjadi suara
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Contoh penggunaan
text_to_speech("halo ini adalah sebuah contoh text to speech")

# Menutup engine setelah selesai
engine.stop()
