def fastest_runner(path):
    leader = ""
    time = 99999
    f = open(path, "r", encoding='utf-8')
    runners = f.read() #content path
    for line in runners.splitlines():
        if int(line.split(" ")[1]) < time: #hvis løper raskere enn raskeste tid
            time = int(line.split(" ")[1]) #ny raskeste tid
            leader = line #ny leder
    return leader

print("Tester fastest_runner... ", end="")
assert "Isak 243" == fastest_runner("marathon.txt")
print("OK")


