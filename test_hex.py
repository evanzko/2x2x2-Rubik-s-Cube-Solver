hex_string = "#"
r = "0x{:02x}".format(244)
g = "0x{:02x}".format(4)
b = "0x{:02x}".format(131)
hex_string = hex_string + r[2] + r[3] + g[2] + g[3]  + b[2] + b[3]
print(hex_string)
print(round(1.9678))