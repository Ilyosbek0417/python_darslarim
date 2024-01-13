mevalar = {
    'olma':10000,
    'nok':15000,
    'anor':20000,
    'anjir':15000,
    'o`rik':17000,
    'olcha':20000
    }

telefonlar = {
    "ali":'iphon x',
    'vali':'galaxsi s9',
    'tohir': 'nokia',
    'marp':'mi 10 pro',
    'gani': 'iphon x',
    'sobr': 'iphon x',
    'nosir':'mi 10 pro'
    }

# bozorlik = ['olma', 'sabzi', 'anor', 'olcha']
# for meva in mevalar:
#     if meva in bozorlik:
#         print(f"{meva.title()} {mevalar[meva]} so`m")
        
# for buyum in bozorlik:
#     if buyum not in mevalar:
#         print(f"iltimos do`koninggizga {buyum.title()}ni ham olib keling")

# print('dokoninggizdagi maxsulotlar:')
# for maxsulot in sorted(mevalar):
#     print(maxsulot.title())

# print(telefonlar)
# for tel in telefonlar.values():
#     print(tel)
    
for tel in set(telefonlar.values()):
    print(tel)

toys = {'boll', 'car', 'lemp', 'bear', 'boll', 'car'}
print(toys)
    

