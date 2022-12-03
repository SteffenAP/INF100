#Oppgave 6

#unique values fra oppgave 1
def unique_values(a):
    unique_list = []
    for index, value in enumerate(a):
        if a[index] not in unique_list:
            unique_list.append(a[index])
    return unique_list



def non_contigous_substrings(s):
    sum = [""] # liste med ""
    for i, v in enumerate(s):
        sum.append(s[i:i+1]) #Alle enkle verdier
        sum.append(s[i:i+2]) #Alle samlede par
        sum.append(s[i:(len(s)-1):2]) # annenhver med start i 0
        sum.append(s[i+1:(len(s)):2]) # annenhver med start i 1
        sum.append((s[:i] + s[i+1:])) # alle strenger med 1 space mellom seg
        sum.append(s) #Hele s
        sum.append((s[0] + s[len(s)-1])) #for å få første og siste verdi
    return(unique_values(sum))


#assert
non_contigous_substrings("foo")
print("Tester non_contigous_substrings... ", end="")
# Test 1
# Merk: rekkefølgen på elementene i listen betyr ingenting,
# siden begge listene sorteres før de sammenlignes
assert(sorted([
  "", # Den tomme strengen er alltid en substreng
  "a", "b", "c", "d",
  "ab", "ac", "ad", "bc", "bd", "cd",
  "abc", "abd", "acd", "bcd",
  "abcd",
]) == sorted(non_contigous_substrings("abcd")))

assert(sorted([
  "",
  "f", "o",  # Merk: "o" opptrer bare én gang
  "fo", "oo",
  "foo",
]) == sorted(non_contigous_substrings("foo")))
print("OK")