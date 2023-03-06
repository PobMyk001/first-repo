class MyCustomeExcpetion(Exception):
    def __init__(self, message="Custom exception is occured"):
        self.message = message
        super().__init__(self.message)

        def str(self):
            return  f"{self.message}"




