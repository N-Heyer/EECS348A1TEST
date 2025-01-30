from maxheap import MaxHeap

class Email:
    """
    Represents an email with sender category, subject, date, and arrival order.
    Priority is determined by sender category and then by arrival order (newest first).
    """
    PRIORITY_MAP = {
        "Boss": 5,
        "Subordinate": 4,
        "Peer": 3,
        "ImportantPerson": 2,
        "OtherPerson": 1
    }

    def __init__(self, sender_category, subject, date, arrival_order):
        self.sender_category = sender_category.strip()
        self.subject = subject.strip()
        self.date = date.strip()
        self.arrival_order = arrival_order
        self.priority = (self.PRIORITY_MAP.get(self.sender_category, 0), -arrival_order)  # Negative arrival_order for newest first

    def __lt__(self, other):
        """Custom comparison for max-heap behavior."""
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __repr__(self):
        return f"Sender: {self.sender_category}, Subject: {self.subject}, Date: {self.date}"


def main():
    email_queue = MaxHeap()
    arrival_counter = 1  # Tracks order of email arrival

    file_name = input("Enter the file containing emails and commands: ").strip()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                
                parts = line.split(",", maxsplit=2)  # Split into command, sender, subject+date
                
                command = parts[0].strip().upper()  # Convert command to uppercase for case-insensitive checking
                
                try:
                    if command == "EMAIL":
                        if len(parts) < 3:
                            print(f"\nInvalid EMAIL format: {line}\n")
                            continue
                        sender_category = parts[1].strip()
                        subject_and_date = parts[2].rsplit(",", maxsplit=1)  # Separate last comma for date

                        if len(subject_and_date) != 2:
                            print(f"\nInvalid EMAIL format: {line}\n")
                            continue

                        subject = subject_and_date[0].strip()
                        date = subject_and_date[1].strip()

                        email = Email(sender_category, subject, date, arrival_counter)
                        email_queue.add(email)
                        arrival_counter += 1

                    elif command == "COUNT":
                        count = email_queue.count()
                        print(f"\nThere are {count} emails to read.\n")

                    elif command == "NEXT":
                        try:
                            next_email = email_queue.peek()
                            print("\nNext email:")
                            print(f"\tSender: {next_email.sender_category}")
                            print(f"\tSubject: {next_email.subject}")
                            print(f"\tDate: {next_email.date}\n")
                        except IndexError:
                            print("\nNo emails waiting.\n")

                    elif command == "READ":
                        try:
                            read_email = email_queue.pop()
                        except IndexError:
                            print("\nNo emails to read.\n")

                    else:
                        print(f"\nInvalid command found in file: {line}\n")

                except (IndexError, ValueError):
                    print(f"\nFile formatted improperly: {line}\n")

    except FileNotFoundError:
        print("\nFile not found.\n")

if __name__ == "__main__":
    main()
