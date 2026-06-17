"""상속 기초 예제입니다."""


class Notification:
    """알림의 기본 클래스입니다."""

    def send(self, message: str) -> None:
        print("알림:", message)


class EmailNotification(Notification):
    """이메일 알림 클래스입니다."""

    def send(self, message: str) -> None:
        print("이메일 전송:", message)


noti = Notification()
noti.send("Python 고급 과정 학습 알림")


notifier = EmailNotification()
notifier.send("Python 고급 과정 학습 알림")

notis = [Notification(), EmailNotification()]
for noti in notis:
    noti.send("Python 고급 과정 학습 알림")
