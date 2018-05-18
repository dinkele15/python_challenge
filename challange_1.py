cipher = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
        rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl
        zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq
        rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq
        pcamkkclbcb. lmu ynnjw ml rfc spj."""


def deciphre(cipher):
    decipher = ""
    for c in cipher:

        if ord(c) >= 97 and ord(c) <= 122:
            if ord(c) + 2 > 122:
                decipher += chr((ord(c) + 2) % 122 + 96)
            else:
                decipher += chr(ord(c) + 2)
        else:
            decipher += c

    print(decipher)


# deciphre(cipher)
# deciphre("map")  # -> ocr

""" i hope you didnt translate it by hand.
        thats what computers are for. doing it in
        by hand is inefficient and that's why this
        text is so long. using string.maketrans() is
        recommended. now apply on the url."""

# http://www.pythonchallenge.com/pc/def/ocr.html
