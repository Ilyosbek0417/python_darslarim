# ## 1
# maxsulotlar1 = [ ]
# ishora1 = True
# while ishora1:
#     print('oladigan massulotni kiriting')
#     maxsulot1 = input()
#     maxsulotlar1.append(maxsulot1)
#     javob = input('yana maxsulo qoshasizmi (ha/yo`q)')
#     if javob != 'ha':
        
#         break
    
# for maxsulot1 in maxsulotlar1:
#     print(maxsulot1.title())
    
##  2
maxsulot2 = {}
ishora = True

while ishora:
    nomi = input('oladihan maxsulotni nomi= ')
    narx = int(input('naarxi= '))
    maxsulot2[nomi] = narx
    javob = input('yana maxsulot qoshasizmi (ha/yo`q)')
    if javob == 'yo`q':
        ishora = False
        
for nomi, narx in maxsulot2.items():
    print(f"{nomi} - {narx} = so`m (ikkinchi)")


buyurtma = ['olma', 'bexi', 'olcha', 'nok', 'banan']

while buyurtma:
    savat = buyurtma.pop()
    if savat in maxsulot2.keys():
        print(f"{nomi} - {narx}=so`m")
    else:
        print(f"bizda {savat} meva yo`q")






