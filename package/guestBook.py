class GuestBook:
    def __init__(self):
        self.guests = list()

    def add_guest(self, name):
        self.guests.append({
            "Guest_name": name
            })
        
    def delete_guest(self, name):
        for guest in self.guests:
            if guest.get("Guest_name") == name:
                self.guests.remove(guest)

    def record_file(self):
        import json
        with open("./BookGuest.json", 'a') as file:
            data = {"List_of_guests": self.guests }
            json.dump(data, file) #json.dump- позволяет сохранять данные в json-файл

#if __name__ == '__main__':
#    guestbook = GuestBook()
#    guestbook.add_guest('Arina')
#    guestbook.add_guest('Kolya')
#    guestbook.delete_guest('Kolya')
#    guestbook.record_file()
