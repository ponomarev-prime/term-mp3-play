import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    file_path = "path/to/your/music.mp3" # только так
    play_music(file_path)

    while True:
        user_input = input("Введите 'stop' для остановки: ")
        if user_input.lower() == "stop":
            stop_music()
            break

if __name__ == "__main__":
    main()
