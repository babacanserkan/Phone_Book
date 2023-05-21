class Contact:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class PhoneBook:

    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number):
        contact = Contact(name, phone_number)
        self.contacts.append(contact)
        print("Kişi eklendi")

    def display_contacts(self):
        if not self.contacts:
            print("Rehber Boş!")
        else:
            for contact in self.contacts:
                print(f"Ad: {contact.name}, Numara: {contact.phone_number}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"{contact.name}: {contact.phone_number}")
                return
        print("Kişi Bulunamadı.")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Kişi rehberden silindi.")
        print("Kişi bulunamadı.")

class Main:
    phone_book = PhoneBook()

    while True:
        print("\n Telefon Rehber Uygulaması")
        print("1. Kişiyi Ekle")
        print("2. Kişileri Göster")
        print("3. Kişi Ara")
        print("4. Kişiyi Sil")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın (1-5): ")

        if choice == "1":
            name = input("Kişinin adını girin: ")
            phone_number = int(input("Kişinin telefon numarasını girin: "))
            phone_book.add_contact(name, phone_number)

        elif choice == "2":
            phone_book.display_contacts()

        elif choice == "3":
            name = input("Aranacak kişinin adını girin: ")
            phone_book.search_contact(name)

        elif choice == "4":
            name = input("Silinecek kişinin adını girin: ")
            phone_book.remove_contact(name)

        elif choice == "5":
            print("Telefon rehberi uygulaması kapatılıyor...")
            break

        else:
            print("Geçersiz bir işlem yaptınız. Tekrar deneyin.")
