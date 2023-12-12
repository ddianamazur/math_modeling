# списковые включения - листкомп - на выходе список
# хранит в себе все хначения сразу:

symbols = 'Python'
symbol_codes = [ord(symbol)*0 for symbol in symbols]
print(symbol_codes) 

# генераторные выражения
#

symbols = 'Snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes)
