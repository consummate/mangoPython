import re
def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search(text)
#    for i in range(len(mo.groups())):     
    print('Phone number found: '+str(mo.group()))

    mat = phoneNumRegex.findall(text)
    print('2Phone number found: '+str(mat))

message = 'Call me at 411-555-4242  tomorrow. 411-555-9999 is my office.'
isPhoneNumber(message)
print('Done')
