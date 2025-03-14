import sys

def message_to_binary(message):
    return "".join(format(ord(char), "08b") for char in message)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 message_to_binary.py <message>")
        sys.exit(1)
    
    MESSAGE = sys.argv[1]
    print(message_to_binary(MESSAGE))
