s='11:59:00AM'
t=''
def timeconv():
    if s[:2]=='12' and 'AM' in s:
        t='00'+s[2:8]
        return t
    if 'PM' in s and s[:2]!='12':
        hh=int(s[:2])+12
        t=str(hh)+s[2:8]
        return t
    return s[:8]

str=timeconv()
print(str)