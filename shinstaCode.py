import morse_talk as mtalk
def encodeMessage(plainText):
    codeText=mtalk.encode(plainText)
    shinstaText=codeText.replace(".",":ShinstaHead:")
    shinstaText=shinstaText.replace("-",":ShinstaBody:")
    shinstaText=shinstaText.replace("       ",":ShinstaTail:")
    shinstaText=shinstaText.replace("   "," ")
    return shinstaText
def decodeMessage(shinstaText):
    shinstaText=shinstaText.replace(" ","   ")
    codeText=shinstaText.replace(":ShinstaHead:",".")
    codeText=codeText.replace(":ShinstaBody:","-")
    codeText=codeText.replace(":ShinstaTail:","       ")
    codeText=codeText+"   .----"
    plainText=mtalk.decode(codeText)
    plainText=plainText[0:len(plainText)-1]
    return plainText