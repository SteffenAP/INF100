#Oppgave 5
def complement(seq):
    com = []
    for i, v in enumerate(seq):
        if v == "A":
            com.append("T")
        elif v == "T":
            com.append("A")
        elif v == "C":
            com.append("G")
        elif v == "G":
            com.append("C")
    com.reverse()
    return "".join(com)

#assert 5
print("Tester complement... ", end="")
assert("ACTGCTAT" == complement("ATAGCAGT"))
assert("TAGTATCTAGT" == complement("ACTAGATACTA"))
assert("ACACAGCTGCAT" == complement("ATGCAGCTGTGT"))
print("OK")