'''
Author: Nick Heyer
KUID: 3142337
Date: 9/30/25
Lab: Assignment1
Last modified: 9/30/25
'''
from maxheap import MaxHeap

class Email:
    PRIORITY_MAP = { #used to create an actual priority based on the senders
        "Boss": 5,
        "Subordinate": 4,
        "Peer": 3,
        "ImportantPerson": 2,
        "OtherPerson": 1
    }

    def __init__(self, sender_category, subject, date, arrival_order): #init the sender cat, subject,date, arrival order of emails and priority of the sender
        self.sender_category = sender_category.strip()
        self.subject = subject.strip()
        self.date = date.strip()
        self.arrival_order = arrival_order
        self.priority = (self.PRIORITY_MAP.get(self.sender_category, 0), -arrival_order)  #this is using the priority map to keep the highest priority at the top and the less relevant at the bottom

    def __lt__(self, other): #helps the priority by using the less than magic method
        return self.priority < other.priority

    def __gt__(self, other):# helps the priority by using the greater than magic method
        return self.priority > other.priority

    def __repr__(self): #magic method to make a string "representation"
        return f"Sender: {self.sender_category}, Subject: {self.subject}, Date: {self.date}"


def main():
    email_queue = MaxHeap()
    arrival_counter = 1  #keeps track of the order of email arrival

    file_name = input("Enter the file name containing emails and commands: ").strip() 

    try:
        with open(file_name, 'r') as file: #opens the file and reads the contents
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(" ", 1) #splits the commands up
                command = parts[0].strip().upper()

                try:
                    if command == "EMAIL": #safety incase the formatting of the email is wrong aka more than one part
                        if len(parts) < 2:
                            print(f"\nInvalid EMAIL format: {line}\n")
                            continue
                        
                        email_data = parts[1].split(",") #splits the email into 3 parts and checks for invalid formatting by having more than 3 parts
                        if len(email_data) != 3:
                            print(f"\nInvalid EMAIL format: {line}\n")
                            continue
                        
                        sender_category = email_data[0].strip()
                        subject = email_data[1].strip()  #strips
                        date = email_data[2].strip()

                        email = Email(sender_category, subject, date, arrival_counter)
                        email_queue.add(email)
                        arrival_counter += 1

                    elif command == "COUNT": #used to count the emails like listed above after being called on COUNT
                        count = email_queue.count()
                        print(f"\nThere are {count} emails to read.\n")

                    elif command == "NEXT": #looks at the next email but doesnt remove it 
                        try:
                            next_email = email_queue.peek()
                            print("\nNext email:")
                            print(f"\tSender: {next_email.sender_category}")
                            print(f"\tSubject: {next_email.subject}")
                            print(f"\tDate: {next_email.date}\n")
                        except IndexError:
                            print("\nNo emails waiting.\n")

                    elif command == "READ": #reads the email and pops it 
                        try:
                            read_email = email_queue.pop()
                        except IndexError:
                            print("\nNo emails to read.\n")

                    else:
                        print(f"\nInvalid command found in file: {line}\n") #invalid command, problems with EMAIL and COUNT

                except (IndexError, ValueError):
                    print(f"\nFile formatted improperly: {line}\n") #wrong format for file, problems with EMAIL and COUNT 

    except FileNotFoundError:
        print("\nFile not found.\n") #mistype the file name 


main()
