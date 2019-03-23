# Installing Requests from Pip:
try:
    import requests
except ModuleNotFoundError:
    import subprocess
    subprocess.call([r'pip_install_requests.bat'])
    import requests

# Installing Pandas from Pip:
try:
    from pandas.io.json import json_normalize
except ModuleNotFoundError:
    import subprocess
    subprocess.call([r'pip_install_pandas.bat'])
    from pandas.io.json import json_normalize

import json
import csv
import sys

cycle = True
while cycle == True:
    try:
        query_input = str(sys.argv[1]) # Works if a command line parameter was given, sys.argv[0] is the program's name.
        cycle = False
    except IndexError:
        query_input = input("INSERT QUERY: ") # If no command line parameter was provided, program asks user for input.
    if query_input == "q" or query_input == "Q":
        break
    else:
        parameters = {"query" : query_input, "trusted" : False} # I left "trusted" : False for illustrative purposes, but it doesn't really work.
        request = requests.get("http://ws75.aptoide.com/api/7/apps/search", params = parameters)
        print(f"QUERY URL: {request.url}")
        if request:
            print(f"""REQUEST STATUS: Success.
STATUS CODE: {request.status_code}\n""")
            app_data = request.json()
            untrusted = [app_entry for app_entry in app_data['datalist']['list'] if app_entry['file']['malware']['rank'].upper() != 'TRUSTED'] # Removing "trusted" apps.
            if not untrusted:
                print("No apps were found.\n")
            else:
                for app in untrusted:
                    print("------ NEW APP ------")
                    for x in app:
                        if type(app[x]) != dict:
                            print(f"{x}: {app[x]}")
                        else:
                            print(f"{x}:")
                            for y in app[x]:
                                if type(app[x][y]) != dict:
                                    print(f"    {y}: {app[x][y]}")
                                else:
                                    print(f"    {y}:")
                                    for z in app[x][y]:
                                        print(f"        {z}: {app[x][y][z]}")
                    print()
                with open(f"{query_input}.csv", "w") as new_csv:
                    exported_data = json_normalize(untrusted)
                    exported_data.to_csv(new_csv, index = False)
        else:
           print("""REQUEST STATUS: Failure.
STATUS CODE: {request.status_code}\n""")
        if cycle == True:
            print("------ RESTART ------\n")
