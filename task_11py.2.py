class MyCustomeExpetion(Exception):
    def __init__(self, message=" Custom exception is occured"):
        self.message = message
        super().__init__(self.message)

        def str(self):
            message_ = f"{self.message}"
            return message_

try:
    raise MyCustomeExpetion("Custom exception is occured")
except MyCustomeExpetion as e:
    x = print(e)
    