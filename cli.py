import re
from colorama import init, Fore, Back, Style

init(convert=True)
print(Fore.GREEN + "  ______ _ _       _____ _                            _____              _____ _      _____\n |  ____(_) |     / ____| |                          |  __ \            / ____| |    |_   _|\n | |__   _| | ___| (___ | |_ _ __ ___  __ _ _ __ ___ | |__) | __ ___   | |    | |      | |  \n |  __| | | |/ _ \\___  \| __| '__/ _ \/ _` | '_ ` _ \|  ___/ '__/  _ \ | |    | |      | |  \n | |    | | |  __/____) | |_| | |  __/ (_| | | | | | | |   | | | (_) | | |____| |____ _| |_ \n |_|    |_|_|\___|_____/ \__|_|  \___|\__,_|_| |_| |_|_|   |_|  \___/   \_____|______|_____|\n" + Style.RESET_ALL)
print (Fore.BLUE + "Welcome to Adarsh's CLI, an easier way to deploy your bot!\nLet's get started!\n\n" + Style.RESET_ALL)

alredy = input("Do you alredy have .env file? (y/n): ")
if alredy == "n":
    api_id = input("Enter your API ID: ")
    while not re.match("[0-9]+", api_id):
        print(Fore.RED + "Invalid API ID, please try again..." + Style.RESET_ALL)
        api_id = input("Enter your API ID: ")
    api_hash = input("Enter your API HASH: ")
    while not re.match("[A-Za-z0-9]+", api_hash):
        print(Fore.RED + "Invalid API HASH, please try again..." + Style.RESET_ALL)
        api_hash = input("Enter your API HASH: ")
    bot_token = input("Enter your bot token: ")
    while not re.match("[0-9]+:[A-Za-z0-9_-]+", bot_token):
        print(Fore.RED + "Invalid bot token, please try again..." + Style.RESET_ALL)
        bot_token = input("Enter your bot token: ")

    fqdn = input("Enter your server id:")
    while not re.match("[A-Za-z0-9]+", fqdn):
        print(Fore.RED + "Invalid server id, please try again..." + Style.RESET_ALL)
        fqdn = input("Enter your server id:")
    username = input("Enter your username id, you can get it from @MissRose_bot:")
    while not re.match("[0-9]+", username):
        print(Fore.RED + "Invalid username id, please try again..." + Style.RESET_ALL)
        username = input("Enter your username id, you can get it from @MissRose_bot:")
    database = input("Enter your mongodb url:")
    while not re.match("^mongodb(?:\+srv)?:\/\/(?:\S+(?::\S*)?@)?(?:(?:(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+(?:[A-Za-z]{2,}|xn--[A-Za-z0-9]{2,}))(:[0-9]{1,5})?(?:\/(?:[^\s/?#]+(?:\?[^#\s]*)?)?)?$", database):
        print(Fore.RED + "Invalid mongodb url, please try again..." + Style.RESET_ALL)
        database = input("Enter your mongodb url:")


    print("Setting up your bot...")

    with open("configs.env", "w") as file:
        file.write(f"API_ID={api_id}\nAPI_HASH={api_hash}\nBOT_TOKEN={bot_token}\nBIN_CHANNEL=-100\nPORT=8080\nFQDN={fqdn}\nOWNER_ID={username}\nDATABASE_URL={database}\n")
        file.close()
    print("Done! Your bot is ready to be deployed!")
    input("Do you wanna to configure extra features? (y/n): ")
    if input == "y":
        print("Okay, lest configure it!")
        channel = input("Enter a public channel username, without @ (if you don't wanna set up this setting just press enter):")
        if re.match("[A-Za-z]+", channel):
            with open("configs.env", "a") as file:
                file.write(f"UPDATES_CHANNEL={channel}\n")
                file.close()
        else:
            print("Invalidad username, skipping...")
        banned_channels = input("Put a list of banned channels, separated by space (if you don't wanna set up this setting just press enter):")
        if banned_channels != "":
            with open("configs.env", "a") as file:
                file.write(f"BANNED_CHANNELS={banned_channels}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
        threshold = input("Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds. (if you don't wanna set up this setting just press enter):")
        if threshold != "":
            with open("configs.env", "a") as file:
                file.write(f"SLEEP_THRESHOLD={threshold}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
        workers = input("Set the maximum number of threads that can be used for running the functions. Defaults to 3. (if you don't wanna set up this setting just press enter):")
        if workers != "":
            with open("configs.env", "a") as file:
                file.write(f"WORKERS={workers}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
        port = input("Enter the port you wanna to use (if you don't wanna set up this setting just press enter):")
        if port != "":
            with open("configs.env", "a") as file:
                file.write(f"PORT={port}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
        
        web_server = input("Enter the web server bind address, if you're on heroku ignore this (if you don't wanna set up this setting just press enter):")
        if web_server != "":
            with open("configs.env", "a") as file:
                file.write(f"WEB_SERVER_BIND_ADDRESS={web_server}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
        noPort = input("If you don't want your port to be displayed. You should point your PORT to 80 (http) or 443 (https) for the links to work. Ignore this if you're on Heroku.")
        if noPort != "":
            with open("configs.env", "a") as file:
                file.write(f"NO_PORT={noPort}\n")
                file.close()
        else:
            print(Fore.YELLOW + "No data provided, skipping..." + Style.RESET_ALL)
            print("Done! Your bot is ready to be deployed!")

    else: 
        print("Okay, setting up the bot")
        exit()

else: 
    print("Okay, setting up the bot")
    exit()
