<h1 align="center">Password Manager with Encryption in Python</h1>

<h2>How to use:</h2>

1. [Run the main.py file](#run_main)
2. [Create a new key](#create_key)
3. [Create a new password file](#create_pass)
4. [Load an existing key](#load_key)
5. [Load an existing password file](#load_pass)
6. [Add a new password](#add_pass)
7. [(OPTIONAL) Get a password)](#get_pass)
8. [Quit the program](#quit_program)

---
<a name="run_main"></a>
<h3>1. Run the main.py file</h3>

In Most IDE's:

1. Open the main.py file
2. Scroll to the bottom of the program and run the line:
        
        if __name__ == "__main__":
            main()
3. You then should be prompted with a command line menu
        
        What do you want to do?
          (1) Create a new key
          (2) Load an existing key
          (3) Create a new password file
          (4) Load existing password file
          (5) Add a new password
          (6) Get a password
          (q) Quit

<br/>
<h2 align="center"> <b><u>**** Warning: If you already have a password file and key skip to step 4 ****</u></b></h2>

---
<a name="create_key"></a>
<h3>2. Create a new key</h3>

1. Enter '1' in the command line
2. Enter the name of a file where the key will be stored (ie. key.key)

        Enter your choice: 1
        Enter new key path: key.key
    
    <h2 align="center"><b>** if the file does not exist it will create a new file **</b></h2>
---
<a name="create_pass"></a>
<h3>3. Create a new password file</h3>

1. Enter 3 in the command line
2. Enter the name of a file where the passwords will be stored (ie. passwords.pass)

        Enter your choice: 3
        Enter new password path: passwords.pass

    <h2 align="center"><b>** if the file does not exist it will create a new file **</b></h2>
---
<a name="load_key"></a>
<h3>4. Load an existing key</h3>

1. Enter 2 in the command line
2. Enter the name of the file where the key is stored (ie. key.key)

        Enter your choice: 2
        Enter key path to load: key.key
---
<a name="load_pass"></a>
<h3>5. Load an existing passwords file</h3>

1. Enter 4 in the command line
2. Enter the name of the file where the passwords are stored (ie. passwords.pass)

        Enter your choice: 4
        Enter password path to load: passwords.pass
---
<a name="add_pass"></a>
<h3>6. Add a new password</h3>

1. Enter 5 in the command line
2. Add a new password to the file by entering is assiciated site (press enter) then type in the password for the associated site

        Enter your choice: 5
        Enter the site: youtube
        Enter the password: youtubepass123
---
<a name="get_pass"></a>
<h3>7. (OPTIONAL) Get a password</h3>

1. Enter 6 in the command line
2. Enter the site of which you would like to retrieve the password for and the program will output the associated password

        Enter your choice: 6
        What site do you want the password for: youtube
        Password for youtube is: youtubepass123
---
<a name="quit_program"></a>
<h3>8. Quit the program</h3>

1. Enter 'q' in the command line to

        Enter your choice: q
        Bye

---
<h2 align="center"><b>The program will not remember the key or password file so if at any point you need to retrieve your passwords, you need to load the key file and password file as depicted from steps 4 to 6</b></h2>