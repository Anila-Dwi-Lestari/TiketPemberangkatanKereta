print("1. MENU DATA PENUMPANG")
print("2. MENU PEMBAYARAN TIKET")
menu=int(input("Pilih:"))
if(menu==1):
    import main_penumpang
elif(menu==2):
    import main_pembayaran
else:
    ("MENU TIDAK TERSEDIA")
