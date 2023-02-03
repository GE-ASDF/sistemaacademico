from winotify import Notification, audio

class notify:

    def notificar(self, app_id = '', title = '', msg = '', icon = '', duration = ''):
        toast = Notification(app_id=app_id, title=title,
        msg=msg, icon=icon, duration=duration)
        toast.set_audio(sound=audio.Mail, loop=False)
        return toast
        