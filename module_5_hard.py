import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def __str__(self):
        return f"Пользователь: {self.nickname}, возраст: {self.age}"

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Видео: {self.title}, длительность: {self.duration} секунд"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, video):
        return video in self.videos

    def __eq__(self, other):
        return self.users == other.users and self.videos == other.videos and self.current_user == other.current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                break

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self:
                self.videos.append(video)

    def get_videos(self, search_term):
        result = []
        for video in self.videos:
            if search_term.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    time.sleep(1)
                    video.time_now += 1
                    print(video.time_now)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")


if __name__ == "__main__":
    urtube = UrTube()
    urtube.register("user1", "password1", 20)
    urtube.register("user2", "password2", 16)
    urtube.log_in("user1", "password1")
    urtube.add(
        Video("Лучший язык программирования 2024 года", 36),
        Video("Для чего девушкам парень программист?", 42, True),
        Video("C++ tutorial", 30),
    )
    print(urtube.get_videos("язык"))
    urtube.watch_video("Лучший язык программирования 2024 года")
    urtube.watch_video("Для чего девушкам парень программист?")