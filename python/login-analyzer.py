logins = [
    ("alex", "success"),
    ("sam", "failed"),
    ("alex", "failed"),
    ("john", "failed"),
    ("alex", "failed"),
    ("sam", "success"),
    ("alex", "success"),
    ("john", "failed")
]

record = {}
for i, m in logins:
    if i not in record:
        record[i] = {}
    if m == "success":
        record[i]["Successful"] = record[i].get("Successful", 0) + 1
    if m == "failed":
        record[i]["Failed"] = record[i].get("Failed", 0) + 1

for j, k in record.items():   # Items unpacks the dictionary in form of keys and values.
                              # Here the ket are names and value is the second dictionary.
    j = j[0].upper() + j[1:]
    print(f'''{j}:            
                Successful: {k.get("Successful")}
                Failed: {k.get("Failed")}''')
