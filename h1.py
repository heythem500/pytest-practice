
def checkNameHas(userName):
    if "@" in userName:
        return "member used @ sign"
    elif "." in userName:
        return "member used dot sign"
    else:
        return userName
nameIs = checkNameHas("Hssssdcom")
print(nameIs)