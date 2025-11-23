class Show:
    def __init__(self, title, time, total_seats):
        self.title = title
        self.time = time
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seats(self, n):
        if n <= 0:
            print("Please enter a number of seat to book.")
            return False
        if self.booked_seats + n <= self.total_seats:
            self.booked_seats += n
            print(f"{n} seat booked for '{self.title}'.")
            return True
        else:
            available = self.total_seats - self.booked_seats
            print(f"Unable to book {n} seat(s). Only {available} seat(s) available for '{self.title}'.")
            return False

    def cancel_seats(self, n):
        if n <= 0:
            print("Please enter a number of seat to cancel.")
            return False
        if self.booked_seats >= n:
            self.booked_seats -= n
            print(f"{n} seat(s) cancelled for '{self.title}'.")
            return True
        else:
            print(f"Cannot cancel {n} seat(s). Only {self.booked_seats} are currently book for '{self.title}'.")
            return False

    def available_seat(self):
        return self.total_seats - self.booked_seats

    def __str__(self):
        return f"'{self.title}' at {self.time} - {self.available_seat()} seat(s) available"


class Theatre:
    def __init__(self):
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def display_shows(self):
        if not self.shows:
            print("No shows available.")
        else:
            for show in self.shows:
                print(show)

    def book_ticket(self, title, count):
        for show in self.shows:
            if show.title.lower() == title.lower():
                return show.book_seats(count)
        print(f"Show '{title}' not found.")
        return False

    def cancel_tickets(self, title, count):
        for show in self.shows:
            if show.title.lower() == title.lower():
                return show.cancel_seats(count)
        print(f"Show '{title}' not found.")
        return False


def run_theatre():
    theatre = Theatre()

    theatre.add_show(Show("Sholay", "3 hrs 48 mins", 380))
    theatre.add_show(Show("RRR", "3 hrs 02 mins", 380))
    theatre.add_show(Show("KGF", "2 hrs 48 mins", 380))
    theatre.add_show(Show("Pushpa", "3 hrs 17 mins", 380))

    while True:
        print("\n1 --> View shows")
        print("2 --> Book tickets")
        print("3 --> Cancel tickets")
        print("4 --> Quit")

        try:
            choice = int(input("Enter any number (1-4): "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:
            theatre.display_shows()

        elif choice == 2:
            t = input("Which show do you want to watch?: ").strip()
            try:
                n = int(input("Enter number of seat to be book: "))
            except ValueError:
                print("Invalid input.")
                continue
            if theatre.book_ticket(t, n):
                print("Booked successfully!")

        elif choice == 3:
            t = input("Enter show name: ").strip()
            try:
                n = int(input("Enter number of seat to cancel: "))
            except ValueError:
                print("Invalid input.")
                continue
            if theatre.cancel_tickets(t, n):
                print("Cancelled successfully!")

        elif choice == 4:
            print("Thanks for visiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please enter between 1 and 4.")


run_theatre()
