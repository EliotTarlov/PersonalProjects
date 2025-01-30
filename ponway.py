import re
goal="pon pon way way way pon pon way pon way pon pon, way way pon pon pon way way pon way pon way way"
biney=[int(x=="pon") for x in goal.split()]
strig=int("".join([str(x) for x in biney]),2)
print(" ".join([int(x)*"pon" + (int(x)^1)*"way" \
for x in bin(13018004)[2:]]))
