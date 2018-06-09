#import string

def mask(cc):
    #l=len(cc))
    if len(cc) <= 4:
        return cc
    else:
        cc1=cc[0:-4:]
        len(cc1)
        new_str = cc.replace(cc1,"#"*len(cc1))
        return new_str
mask("12345678")
