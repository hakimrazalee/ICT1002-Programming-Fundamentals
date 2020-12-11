import sys


def elvish(x, eCheck=False, lCheck=False, fCheck=False):
    if eCheck and lCheck and fCheck:
        return True

    if not x:
        return False

    elif eCheck and lCheck:
        if x[0] == 'f':
            return elvish(x[1:], eCheck=True, lCheck=True, fCheck=True)
        else:
            return elvish(x[1:], eCheck=True, lCheck=True)

    elif eCheck and fCheck:
        if x[0] == 'l':
            return elvish(x[1:], eCheck=True, lCheck=True, fCheck=True)
        else:
            return elvish(x[1:], eCheck=True, fCheck=True)

    elif fCheck and lCheck:
        if x[0] == 'e':
            return elvish(x[1:], eCheck=True, lCheck=True, fCheck=True)
        else:
            return elvish(x[1:], fCheck=True, lCheck=True)

    elif eCheck:
        if x[0] == 'l':
            return elvish(x[1:], eCheck=True, lCheck=True)
        elif x[0] == 'f':
            return elvish(x[1:], eCheck=True, fCheck=True)
        else:
            return elvish(x[1:], eCheck=True)

    elif lCheck:
        if x[0] == 'e':
            return elvish(x[1:], eCheck=True, lCheck=True)
        elif x[0] == 'f':
            return elvish(x[1:], lCheck=True, fCheck=True)
        else:
            return elvish(x[1:], lCheck=True)

    elif fCheck:
        if x[0] == 'l':
            return elvish(x[1:], fCheck=True, lCheck=True)
        elif x[0] == 'e':
            return elvish(x[1:], fCheck=True, eCheck=True)
        else:
            return elvish(x[1:], fCheck=True)

    elif x[0] == 'e':
        return elvish(x[1:], eCheck=True)

    elif x[0] == 'l':
        return elvish(x[1:], lCheck=True)

    elif x[0] == 'f':
        return elvish(x[1:], fCheck=True)

    else:
        return elvish(x[1:])


z = str(sys.argv[1])

if elvish(z):
    print(z + " is one elfish word!")
else:
    print(z + " is not an elfish word!")
