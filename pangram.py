class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence.strip()
        alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for c in alphabets:
            if c not in sentence:
                return False
        return True
        