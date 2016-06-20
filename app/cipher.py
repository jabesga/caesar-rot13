class Caesar():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, key):
        self.key = key
        self.shifted_alphabet = self.alphabet[key:] + self.alphabet[0:key]
        self.encrypt_dict = str.maketrans(self.alphabet, self.shifted_alphabet)
        self.decrypt_dict = str.maketrans(self.shifted_alphabet, self.alphabet)

    def encrypt_sentence(self, sentence):
        return sentence.translate(self.encrypt_dict)

    def decrypt_sentence(self, sentence):
        return sentence.translate(self.decrypt_dict)
