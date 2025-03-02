def remove_start(bin):
    while bin[0] == "0":
        bin = bin[1:]
    return bin



def convert(num):
    i = 128
    bin = ""
    while i >= 1:
        if (num - i >= 0):
            bin += "1"
            num -= i
        else:
            bin += "0"
        i /= 2
    bin = remove_start(bin)
    return bin


def turn_to_neg(num):
    bin = convert(num)
    neg_bin = ""
    for i in range (len(bin)):
        if bin[i] == "0":
            neg_bin += "1"
        else:
            neg_bin += "0"
    neg_bin = neg_bin[::-1]
    neg_bin2 = ""
    i = 0
    while i < len(neg_bin):
        if (neg_bin[i] == "1"):
            neg_bin2 += "0"
        else:
            neg_bin2 += "1"
            i += 1
            while i < len(neg_bin):
                neg_bin2 += neg_bin[i]
                i += 1
            break
        i += 1
    i = len(neg_bin2)
    while i < 8:
        neg_bin2 += "1"
        i += 1
    neg_bin2 = neg_bin2[::-1]
    print(neg_bin2)

turn_to_neg(42)




