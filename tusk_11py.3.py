class CustomContextManager:
    def __enter__(self):
        print("=" * 10)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=" * 10)
        return self

    def exit(self, ex_type, ex_value, traceback):
        print("=" * 10)
        if exit() is not None:
            print(f"an arror occured:{ex_value}")
            return True
