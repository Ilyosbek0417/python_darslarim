taomlar = ['ow', 'kabob', 'ko`za worva', 'siltama', 'qovurdoq']
print(taomlar)
nonushta=taomlar[:]
print(nonushta)
nonushta.remove('kabob')
nonushta.remove('ko`za worva')
nonushta.remove('siltama')
nonushta.append('qaymoq')
nonushta.append('non issiq')
print(taomlar)
print(nonushta)


nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)