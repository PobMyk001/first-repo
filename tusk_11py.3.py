class CustomContextManager:
    def __enter__(self):
        print("=" * 10)


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            print(exc_val)
        else:
            print("=" *10)



