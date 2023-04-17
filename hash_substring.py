# python3

def read_input():
    
    letter = input()

    if 'I' in letter:

        return (input().rstrip(), input().rstrip())

    elif 'F' in letter:

        with open("tests/06") as file:

            return (file.readline().rstrip(), file.readline().rstrip())
        


def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    textLength = len(text)
    patternSize = len(pattern)
    textHash = []
    for i in range(textLength - patternSize + 1):

        substring = text[i:i + patternSize]
        hash = hash(substring)
        textHash.append(hash)

    hashLength = len(textHash)
    outprint = []
    if textLength < patternSize:
        return outprint
        
    patternHash = hash(pattern)
    for i in range(hashLength):
         
         if patternHash == textHash[i] and text[i:i + patternSize] == pattern:

            outprint.append(i)

    return outprint 
    
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
