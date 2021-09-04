all = {"ABC", "ARC", "AGC", "AHC"}
inputs = {input() for _ in range(3)}
print((all - inputs).pop())