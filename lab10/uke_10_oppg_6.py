from datetime import timedelta, datetime

#Oppgave 6
def first_friday_13th_after(date):
    friday = date + timedelta(1) #sjekker fra dagen etterpå for å forhindre feil hvis dagen det starter på er f13
    while True: #løkke som sjekker alle datoer
        if friday.day == 13 and friday.weekday() == 4: #Hvis dagen er 13 og ukedagen er 4 (fredag)
            return friday # gi et svar
        else:
            friday += timedelta(1) #ellers gå til neste dag


#Assert oppgave 6
print("Tester first_friday_13th_after... ", end="")
# Test 1
result = first_friday_13th_after(datetime(2022, 10, 24))
assert((2023, 1, 13) == (result.year, result.month, result.day))
# Test 2
result = first_friday_13th_after(datetime(2023, 1, 13))
assert((2023, 10, 13) == (result.year, result.month, result.day))
# Test 3
result = first_friday_13th_after(datetime(1950, 1, 1))
assert((1950, 1, 13) == (result.year, result.month, result.day))
print("OK")