MESSAGE = "ToiYeuPTIT"

def message_to_binary(message):
	return "".join(format(ord(char), "08b") for char in message)

print(message_to_binary(MESSAGE))
