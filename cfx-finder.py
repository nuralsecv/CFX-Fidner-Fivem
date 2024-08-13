#Libs
import requests
import os
import time

# S
Title = "Nural CFX Finder"



#Title of the window
os.system("title " + Title)

# Clear the screan

os.system("cls")

## API

def nural_cfx_finder(nural_url):
    try:
        if not nural_url:
            return "ERROR: Link cannot be empty!"
        else:
            respo = requests.get("https://" + nural_url)
            respo.raise_for_status()
            ip = respo.headers["X-Citizenfx-Url"]
            ipcut = ip.replace("http://", "")
            return f"IP of {nural_url} : " + ipcut.replace("/", "")
    except requests.ConnectionError:
        return "ERROR: Connection error!"
    except requests.exceptions.HTTPError as err:
        return f"ERROR: {err}"


# Print the results

if __name__ == "__main__":
    nural_url = input("Nural CFX Finder > Provide cfx.re link: ")
    
# Clear the screan

    os.system("cls")
# Results    
    result = nural_cfx_finder(nural_url)
    print("waiting ...")
    time.sleep(1.5)
    print("waiting .....")
    time.sleep(0.5)
    print("waiting ..........")
    print(result)
