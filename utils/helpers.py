import syslog

def fixedStrLen(myStr,n, align="left"):
    if(len(myStr) >= n):
        return myStr
    result = myStr
    for i in range(0, n - len(myStr)):
        if align == "left":
            # align left
            result += " "
        else:
            # align right
            result = " " + result
    return result

def log(msg):
    syslog.syslog("[COOK]:" + msg)