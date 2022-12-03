def print_errors_and_warnings(text):
    raport = ""
    for line in text:
        if "Warning" in line:
            raport += f"{line}\n"
        elif "Error" in line:
            raport += f"{line}\n"
    print(raport)

print_errors_and_warnings([

  "Info: had a good nights sleep before exam",

  "Warning: not enough snacks brought for exam",

  "Info: went for a walk before exam started",

  "Error: went to wrong exam location",

  "Debug: laptop_charge=92%, charing_cable_present=True",

  "Warning: time management is important",

])