import cryptography
from cryptography.fernet import Fernet

class PasswordManager:
    
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        
    # ---------- Create Keys File ---------- #
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
            
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
            
    # ---------- Create Password File ---------- #
    
    # Create file 
    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
     
    # Get the existing password file
    def load_password_file(self, path):
        self.password_file = path
        
        # load password file and each line is separated by a : then read line by line to decrypt and load key value pairs
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    
    # Add a site and password to the password file
    def add_password(self, site, password):
        self.password_dict[site] = password
        
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")
        
    # Get a password from the password file by the site
    def get_password(self, site):
        return self.password_dict[site]
    
    

def main():
    password = {}
    
    pm = PasswordManager()
    
    # Command line menu
    print("""What do you want to do?
          (1) Create a new key
          (2) Load an existing key
          (3) Create a new password file
          (4) Load existing password file
          (5) Add a new password
          (6) Get a password
          (q) Quit
    """)
    
    done = False
    
    while not done:
        choice = input("Enter your choice: ")
        
        # Create a new key
        if choice == "1":
            path = input("Enter new key path: ")
            pm.create_key(path)
        
        # Load an exsisting key
        elif choice == "2":
            path = input("Enter key path to load: ")
            pm.load_key(path)
        
        # Create a new password file
        elif choice == "3":
            path = input("Enter new password path: ")
            pm.create_password_file(path, password)
        
        # Load an existing password file
        elif choice == "4":
            path = input("Enter password path to load: ")
            pm.load_password_file(path)
        
        # Add a new password
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        
        # Get a password from the file
        elif choice == "6":
            site = input("What site do you want the password for: ")
            print(f"Password for {site} is: {pm.get_password(site)}")
        
        # Quit the program
        elif choice == "q":
            done = True
            print("All passwords enctyped, you are safe now :)")
        else:
            print("INVALID CHOICE!!")

# Run the program
if __name__  == "__main__":
    main()