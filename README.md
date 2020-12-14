# Rudolph's Letters

- A simple Python script to have a fun and joyful Secret Santa.
- To run your own Secret Santa:

  1. Fill up `members.csv` with the Names and Emails of participants.
  2. In `details.json` enter your gmail email ID and password (this is stored locally, so ensure it's in a secure place - or delete it after using).
  3. Run `pip3 install -r requirements.txt` to install dependent packages.
  4. Run `python3 santa.py members.csv <budget> <date> <location>`.
  
     Eg. `python3 santa.py members.csv 200INR 21-12-2020 PESU`.

- If you already have a datafile, ensure that the headers of the name and email columns are `Name` and `Email` respectively, and instead of `members.csv` pass the name of your data file.
- Edit the Subject, and Text from inside the `santa.py` code file.
