import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

# [25216, 1354, 0, 3673, 1308, 382, 17271, 1986, 1068, 138759, 1109, 24114]
text = "Hey there! My name is Navaneethakrishnan"
tokens = enc.encode(text)

decoded = enc.decode([25216, 1354, 0, 3673, 1308, 382, 17271, 1986, 1068, 138759, 1109, 24114])

print("Tokens", tokens)
print("Decoded", decoded)