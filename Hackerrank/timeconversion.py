s='12:40:22AM'
def ans():
    if "AM" in s and s[:2]=="12":
      tm="00"+s[2:8]
      return str(tm)
    if "AM" in s:
      tm=s[:8]
      return tm
    if "PM" in s and s[:2]=="12":
      tm=s[:8]
      return tm
    if "PM" in s:
       hh=int(s[:2])+12
       tm=str(hh)+s[2:8]
       return tm


answer=ans()
print(answer)