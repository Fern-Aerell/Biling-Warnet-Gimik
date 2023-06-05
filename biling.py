import time
from pygame import mixer

mixer.init()

def play_sound(sound_file):
    sound = mixer.Sound(sound_file)
    sound.play()

def convert_to_hh_mm_ss(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time_str

billing_time = 0

def init():
    global billing_time

    print("Biling Warnet Gimik\n")
    print("1. 30 Menit")
    print("2. 1 Jam")
    print("3. 2 Jam")
    print("4. 3 Jam")
    print("5. Custom berapa jam")
    print("6. Custom berapa detik")
    jwb = input("Silahkan pilih waktu : ")

    # Mengatur waktu billing
    if jwb == "1":
        billing_time = 60 * 30
    elif jwb == "2":
        billing_time = 60 * 60
    elif jwb == "3":
        billing_time = (60 * 60) * 2
    elif jwb == "4":
        billing_time = (60 * 60) * 3
    elif jwb == "5":
        jwb = input("Mau Main Berapa Jam? : ")
        jwb = int(jwb)
        billing_time = (60 * jwb) * 60
    elif jwb == "6":
        jwb = input("Mau Main Berapa Detik? : ")
        jwb = int(jwb)
        billing_time = jwb
    elif jwb != "1" or "2" or "3" or "4" or "5" or "6":
        init()

init()

remaining_time = billing_time

while remaining_time > 0:
    # Menunggu 1 detik
    time.sleep(1)
    remaining_time -= 1

    if remaining_time == 30 * 60:  # Tersisa 30 menit
        play_sound("./sounds/topup.wav")
    elif remaining_time == 10 * 60:  # Tersisa 10 menit
        play_sound("./sounds/10.wav")
    elif remaining_time == 5 * 60:  # Tersisa 5 menit
        play_sound("./sounds/05.wav")  
    elif remaining_time == 3 * 60:  # Tersisa 3 menit
        play_sound("./sounds/03.wav")  
    elif remaining_time == 1 * 60:  # Tersisa 1 menit
        play_sound("./sounds/01.wav")

    print(convert_to_hh_mm_ss(remaining_time))

play_sound("./sounds/end.wav") # Selesai
time.sleep(7)
print("Biling Habis...")