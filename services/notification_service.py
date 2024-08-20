from nameko.rpc import rpc

class NotificationService:
    name = "notification_service"

    @rpc
    def send_notification(self, message):
        # Implement notification logic
        pass
