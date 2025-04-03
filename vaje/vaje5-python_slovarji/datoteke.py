import os


files = {}

print(os.listdir("V5-datoteke"))
fpath = "V5-datoteke"

for fname in os.listdir(fpath):
    cfn = fpath + "/" + fname
    print(f'Opening "{cfn}"...')
    with open(cfn) as f:
        print(f' Reading "{cfn}"...')
        files[fname] = f.readlines()

for i in range(len(files)-1):
    k = list(files.keys())
    v = list(files.values())
    vv = v[i][0]
    print(f"{k[i]}: {vv}")

# for data in files:
#     [print(f"{some[0]}:\n {some[1][0].strip()}\n") for some in files.items()]