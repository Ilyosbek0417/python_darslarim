# def salom_berish():
#     """salom beruvchi funksiya"""
#     print('Assalomu alykum')
    
# salom_berish()

# ##///////////////

# def shaxsga_salom():
#     """ismizga salom beruvchi funksiya"""
#     ism = input("ismingizni kiriting")
#     print(f"Assalomu alykum {ism.title()}")
# shaxsga_salom()

# ##////////////////////////

# def yosh_hisobla():
#     ism = input("Ismingizni kiriting ")
#     yil = int(input('tug`ilgan yilingizni kiriting '))
#     print(f"Salom {ism.title()} siz {2024 - yil} yoshdasiz")

# yosh_hisobla()

# ##/////////

def toliq_ism_yasa(ism, familiya, otasini_ismi = ''):
    """toliq ism qytaruvchi funksiya"""
    if otasini_ismi:
        toliq_ism = f"{ism.title()} {otasini_ismi.title()}vich {familiya.title()} "
    else:
        toliq_ism =f"{ism.title()} {familiya.title()}"
    return toliq_ism
talaba1 = toliq_ism_yasa('ali', 'aliyev', 'alisherbek')
talaba2 = toliq_ism_yasa('vali', 'valiyev')

print(f"Darska kelmagan talabalar {talaba1} va {talaba2} lar")





