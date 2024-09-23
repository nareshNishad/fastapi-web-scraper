class NotificationStrategy:
    def notify(self, message):
        pass

class ConsoleNotificationStrategy(NotificationStrategy):
    def notify(self, message):
        print(message)
