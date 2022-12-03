def mean(data):
    summation = 0.0 #tom variabel, float
    for number in data:
        summation += float(number) #summerer alle tall
    instances = len(data) #hvor mange tall i data
    total = summation/instances #deler sum på antall
    return total

def median(data):
    median = 0.0 # tom variabel for å lagre median
    newdata = sorted(data) #ny a for å sortere listen
    index = (len(data)//2) # finne midten av listen
    if len(data) % 2 == 0: #partall betyr det er 2 tall i senter
        median = ((float(newdata[index-1]) + float(newdata[index])) / 2)
    else: # ellers er det bare ett tall i senter
        median = newdata[index]
    return median

def mode(data):
    counter = 0 # teller
    countednumber = float() #høyest telte nummer
    for number in data: #sjekker hvert tall
        if data.count(number) > counter: #hvis antall ganger tallet dukker opp er over nåværende høyeste
            counter = data.count(number) #ny høyeste telt
            countednumber = float(number) #ny mest forekommende tall
    return countednumber


def almost_equals(a, b):
   return abs(a - b) < 0.00000001

if __name__ == "__main__": #utføres bare hvis denne filen kjøres
    def cmd_main():
        print("Regn ut statistiske gjennomsnitt for en liste.\nOppgi tallene du vil regne ut gjennomsnitt for, sepearert av mellomrom:")
        rawdata = input() #bruker input
        datalist = rawdata.split(" ") #gjør input om til liste, delt ved mellomrom
        print(f"\nGjennomsnitt: {round(mean(datalist), 1)}")
        print(f"Median:       {median(datalist)}")
        print(f"Typetall:     {mode(datalist)}")
    cmd_main()
        

assert(almost_equals(2.75, mean([2, 5, 3, 1]))) 

assert(almost_equals(5.0, median([4, 12, 3, 9, 5])))
assert(almost_equals(6.0, median([4, 12, 3, 9, 5, 7])))

assert(almost_equals(4.0, mode([3, 4, 22, 7, 4, 15, 4, 7, 1])))

a = [3, 22, 7, 7, 7, 22.0, 3, 22.0] # Tricky case: både 22 og 22.0
assert(almost_equals(22.0, mode(a)))

# Sjekk at a ikke er mutert
for i, v in enumerate([3, 22, 7, 7, 7, 22.0, 3, 22.0]):
   assert(a[i] == v), f"Feil verdi: a[{i}]={a[i]}, men forventet {v}"
   assert(type(a[i]) == type(v)), f"Feil type: type(a[{i}])={type(a[i])}"