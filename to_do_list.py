yapilacaklar = []

while True:
    print("\n--- Yapılacaklar Listesi ---")
    print("1 - Yapılacak ekle")
    print("2 - Yapılacakları göster")
    print("3 - Yapıldı olarak işaretle")
    print("4 - Yapılacak sil")
    print("5 - Çıkış")

    secim = input("Seçimin (1-5): ")

    if secim == "1":
        yeni_gorev = input("Yapılacak: ")
        yapilacaklar.append({"gorev": yeni_gorev, "durum": False})
        print("✅ Yapılacak eklendi.")

    elif secim == "2":
        if len(yapilacaklar) == 0:
            print("📭 Liste boş.")
        else:
            print("\nYapılacaklar:")
            for i in range(len(yapilacaklar)):
                durum = "✅" if yapilacaklar[i]["durum"] else "❌"
                print(f"{i + 1}. {durum} {yapilacaklar[i]['gorev']}")

    elif secim == "3":
        if len(yapilacaklar) == 0:
            print("❌ İşaretlenecek görev yok.")
        else:
            for i in range(len(yapilacaklar)):
                durum = "✅" if yapilacaklar[i]["durum"] else "❌"
                print(f"{i + 1}. {durum} {yapilacaklar[i]['gorev']}")

            numara = int(input("Yapıldı olarak işaretlenecek numara: "))
            yapilacaklar[numara - 1]["durum"] = True
            print("🎉 Görev yapıldı olarak işaretlendi.")

    elif secim == "4":
        if len(yapilacaklar) == 0:
            print("❌ Silinecek görev yok.")
        else:
            for i in range(len(yapilacaklar)):
                durum = "✅" if yapilacaklar[i]["durum"] else "❌"
                print(f"{i + 1}. {durum} {yapilacaklar[i]['gorev']}")

            silinecek = int(input("Silmek istediğin numara: "))
            silinen = yapilacaklar.pop(silinecek - 1)
            print(f"🗑️ '{silinen['gorev']}' silindi.")

    elif secim == "5":
        print("👋 Programdan çıkılıyor...")
        break

    else:
        print("⚠️ Geçersiz seçim, tekrar dene.")