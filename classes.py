import time

class DataBank:
    def __init__(self, userid: str, value: int):
        self.tablename = 'bank'
        self.UserId = userid
        self.Value = value
        self.RegistrationDate = time.strftime("%y-%m-%d: %H-%M-%S")

class DataLog:
    def __init__(self, type: str, channel: str, user: str, content: str):
        self.TimeStamp = time.strftime("%y-%m-%d: %H-%M-%S")
        self.tablename = 'log'
        self.Type = type
        self.Channel = channel
        self.User = user
        self.Content = content
