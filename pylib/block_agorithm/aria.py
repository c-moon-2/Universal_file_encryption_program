import jpype

def runAriaEncrypt(key, Text):
    ariaCyper = jpype.JClass('kr.re.nsri.aria.ARIA').runAriaEncrypt(key, Text)
    return ariaCyper
    
def runAriaDecrypt(key, Text):
    ariaDecyper = jpype.JClass('kr.re.nsri.aria.ARIA').runAriaDecrypt(key, Text)
    return ariaDecyper