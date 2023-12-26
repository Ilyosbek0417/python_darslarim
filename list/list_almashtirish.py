t_shaxslar=["IBN Sino", "Alxorazmiy", "gerado"]
z_shaxslar=['bil gets', 'marc sucerberc', 'ilon sack']
xabar1=t_shaxslar.pop(1)
xabar2=z_shaxslar.pop(1)
print("men tarixiy shaxlardan ", xabar1, "bilan zamonaviy  shaxslardan esa ", 
      xabar2, "bilan suxbatlashmoqchiman")
#/////////////////

friends=[]
friends.append("ali")
friends.append("vali")
friends.append('anvar')
friends.append('asad')
friends.append('bobur')
print(friends)
friends.remove('anvar')
print(friends)
friends.append('normat')
friends.insert(0, 'ahmad')
friends.insert(3, "sunnat")
print(friends)
#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)