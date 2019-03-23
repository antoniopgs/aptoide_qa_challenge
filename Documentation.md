Aptoide QA Challenge
March 22, 2019

Overview

This challenge was sent to me as a phase of a recruitment process conducted by Aptoide for their Quality Assurance and Content Team.
The challenge consists of creating a Python script to retrieve app data from one of Aptoide’s APIs.

Script Goals

1. Receive input from console: Completed ?
2. Retrieve data from all “non-trusted” apps: Completed ?
3. Print said data into the console: Completed ?
4. Export all data into csv: Completed ?
 
Specifications

The first thing I tried to do was to make the script as autonomous as possible. I created two .bat files “pip_install_requests” and “pip_install_pandas”. Both these files install the latest version of pip (if it is not already installed) and install the “requests” and “pandas” library, respectively. I also decided to include them in a Try, Except, to avoid opening the command line and batch files when said libraries are already available to be imported.
I believe is some kind of issue with the API itself. In this image, it states that the argument “trusted” is what determines if the list has “trusted apps only”:
 
I experimented with multiple queries (for example “lyft”) and if I use “trusted”: True it only shows true apps, while if I used “trusted”: False, it would be the same as not using the “trusted” argument at all.
Maybe this is some unexpected issue.
Maybe it was intended, but if so, I’d think it would be better to make “trusted” have 3 values:
• "True" for only trusted apps
• "False" for only untrusted apps
• "None" (or something else) for trusted and untrusted apps

This would facilitate the retrieval of untrusted apps, eliminating the need for a workaround (which you will find in my code). On the other hand, maybe I am just being an idiot, and this makes perfect sense, which I have to have the self-awareness to consider.

One of the major decisions I made was on how to print the retrieved data. I considered printing it like the example in the PDF (EX: App Name, md5, Version Name, Version Code, Store package name, Download Numbers) but I wasn’t sure this meant this was the desired format, or just a list with examples of information. If I printed in this format, I believe there would be too much information to make it properly readable and the indentations (sub-information) would complicate the process too. So I chose to keep it simple and print something similar to the JSON format. At first, I tried using the Pretty Print (pprint) library, but ended up coming up with what I think is a more elegant solution (no JSON punctuation, only indents) and it only took me some print statements, if and elses and some for cycles.

I also added the “query url”, “request status”, “status code”.

I added ------ NEW APP ------ and ------ RESTART ------ to facilitate reading.

When the program is not run on console I implemented a while cycle and an INSERT QUERY: message to make it as clear and intuitive as possible to use.

My script works both in and outside of the console (with slight variations to adjust for while cycles, etc.)

My script also attaches the name of the query inserted to the name of the created CSV file to facilitate identification.

My script only creates a CSV file if app data was found, to avoid creating empty files.

My script has a built in quit option, which is to type either “q” or “Q”. This avoids the quit() method.

Things I’d like to improve on:

• My CSV files have all the information, but due to the fact I had to modify the JSON information to exclude trusted apps, I created some possible indexing problems while trying to better organize the columns and the empty rows.
• When I run my script on 32-bit IDLE it runs fine. When I run it on 64-bit IDLE, it raises a “ModuleNotFoundError”, which I’m still figuring out, because I accounted for that very exact error in my Try, Except methods.
• The majority of queries work just fine. In a few of them, there is some API data that cannot be encoded into the formats I am using, which was also influenced by the untrusted apps filtering.

Thanks!
António Gonçalves
