from pprint import pprint

list_dict = [{"bin": bin(i), "dec": i, "oct": oct(i), "hex": hex(i)} for i in range(16)]
pprint(list_dict)
#