from decimal import *

def receipt_content(prices_filename, cash_register_filename):
    """Construct contents of a receipt of the cash register events,
    given the store prices."""

    with open(cash_register_filename, "r") as f:
        register = f.readlines()
    with open(prices_filename, "r") as fb:
        prices = fb.readlines()
    rec = dict()
    for line in register:
        listline = line.split(";")
        if listline[1][0:-1] in rec:
            if listline[0] == "buy":
                rec[listline[1][0:-1]] += 1
            elif line[0] == "return":
                rec[listline[1][0:-1]] -= 1
        if listline[1][0:-1] not in rec:
            if listline[0] == "buy":
                rec[listline[1][0:-1]] = 1
            elif listline[0] == "return":
                rec[listline[1][0:-1]] = -1
        if listline[0] == "pay":
            payment = listline[1][0:-1]
    sortrec = sorted(rec)
    purchlist = list()
    subtotal = 0
    for item in sortrec:
        for l in prices:
            line = l.split(";")
            if item == line[0]:
                price = int(rec[item]) * float(str([line[1][0:-1]])[2:-2])
                subtotal += price
                purchlist.append((rec[item], item, price))
    vat = subtotal * 0.2
    change = float(payment) - subtotal
    return purchlist, subtotal, vat, float(payment), change



def receipt(prices_filename, cash_register_filename):
    """Construct a receipt of the cash register events,
    given the store prices."""

    # get receipt content from receipt_content()
    purcases_returns, total, vat, payment, change = receipt_content(
        prices_filename, cash_register_filename
    )

    # the formatted lines of the receipt
    receipt_lines = [f"{'Nr.':>4}  {'Item':18}  {'Price':>10}"]

    for nr, item, price in purcases_returns:
        receipt_lines.append(f"{nr:4d}  {item:18}  {price:10.2f}")

    receipt_lines.append(f"Total: {total}")
    receipt_lines.append(f"Of which VAT: {vat:.2f}")
    receipt_lines.append(f"Payment: {payment}")
    receipt_lines.append(f"Change {change}")

    # add some dividers
    max_len = max(len(line) for line in receipt_lines)
    divider = "-" * max_len
    receipt_lines.insert(1, divider)
    receipt_lines.insert(-4, divider)
    receipt_lines.insert(-2, divider)

    return "\n".join(receipt_lines)

print("Tester receipt... ", end="")
expected_value = """\
 Nr.  Item                     Price
------------------------------------
   2  apple                    10.00
   1  chips                    24.30
   1  dish soap                26.20
   1  frozen pizza             54.40
   1  peanuts                  18.50
   1  toilet paper             34.00
   3  tomato                   30.00
  -1  pocket book            -149.00
  -1  toothpaste              -13.70
------------------------------------
Total: 34.7
Of which VAT: 6.94
------------------------------------
Payment: 100.0
Change -65.3"""
assert(expected_value == receipt("prices.txt", "cash_register.txt"))
print("OK")