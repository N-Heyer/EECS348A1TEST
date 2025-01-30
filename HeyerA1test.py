from maxheap import MaxHeap

class Email:
    """
    Represents an email with sender category, subject, date, and arrival order.
    """
    PRIORITY_MAP = {
        "Boss": 5,
        "Subordinate": 4,
        "Peer": 3,
        "ImportantPerson": 2,
        "OtherPerson": 1
    }

    def __init__(self, sender_category, subject, date, arrival_order):
        self.sender_category = sender_category
        self.subject = subject
        self.date = date
        self.arrival_order = arrival_order
        self.priority = (self.PRIORITY_MAP.get(sender_category, 0), arrival_order * -1)

    def __lt__(self, other):
        """
        Custom comparison for heap sorting:
        - Higher priority sender ranks first.
        - Newer emails (higher arrival_order) come first if sender priority is the same.
        """
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"Sender: {self.sender_category}, Subject: {self.subject}, Date: {self.date}"

def main():
    email_queue = MaxHeap()
    arrival_counter = 1  # Tracks order of email arrival

    file_name = input("Enter the file containing emails and commands: ")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(", ")
                command = parts[0]

                try:
                    if command == "EMAIL":
                        sender_category = parts[1]
                        subject = parts[2]
                        date = parts[3]

                        email = Email(sender_category, subject, date, arrival_counter)
                        email_queue.add(email)
                        arrival_counter += 1  # Increase counter for next email

                    elif command == "COUNT":
                        count = email_queue.count()
                        print(f"\nThere are {count} emails to read.\n")

                    elif command == "NEXT":
                        try:
                            next_email = email_queue.peek()
                            print("\nNext email:")
                            print(f"  Sender: {next_email.sender_category}")
                            print(f"  Subject: {next_email.subject}")
                            print(f"  Date: {next_email.date}\n")
                        except IndexError:
                            print("\nNo emails waiting.\n")

                    elif command == "READ":
                        try:
                            read_email = email_queue.pop()
                            print(f"\nRead email from {read_email.sender_category}: {read_email.subject} ({read_email.date})\n")
                        except IndexError:
                            print("\nNo emails to read.\n")

                    else:
                        print("\nInvalid command found in file.\n")

                except IndexError:
                    print("\nFile formatted improperly.\n")
                except ValueError:
                    print("\nFile formatted improperly.\n")

    except FileNotFoundError:
        print("\nFile not found.\n")

if __name__ == "__main__":
    main()
