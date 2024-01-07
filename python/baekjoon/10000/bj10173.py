while True:
    inp = input()
    if inp == "EOI":
        break
    inp = inp.upper()
    if inp.find("NEMO") == -1:
        print("Missing")
    else:
        print("Found")
