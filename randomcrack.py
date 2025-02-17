class Cracker:
    def __init__(self):
        self.state = "initialized"

    def submit(self, number):
        return f"Processing number: {number}"

    def is_cracked(self):
        return True

    def random(self):
        return 42