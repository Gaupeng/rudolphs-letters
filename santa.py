import json
import pandas as pd
import smtplib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint


class SantaException(Exception):
    """
    Someone's on Santa's Naughty List
    """

    pass


class SantasElf:
    def __init__(self):
        clArgs = sys.argv
        if len(clArgs) < 5:
            raise SantaException()
        dataFile = clArgs[1]
        self._extractData(dataFile)
        self.budget = clArgs[2]
        self.date = clArgs[3]
        self.location = clArgs[4]

    def _extractData(self, dataFile):
        """
        Retrieve members and emails from `dataFile`
        """
        _df = pd.read_csv(dataFile)
        self.members = _df["Name"].tolist()
        self.emails = _df["Email"].tolist()
        fh = open("details.json", "r")
        jsonStuff = json.load(fh)
        self.myEmail = jsonStuff["email"]
        self.myPassword = jsonStuff["password"]

    def _randomPicks(self):
        """
        Creates a derangement of range (0, len(self.members))

        Referenced from early-refusal algorithm
        """
        while True:
            randomList = [num for num in range(len(self.members))]
            for num in range(len(self.members) - 1, -1, -1):
                randInt = randint(0, num)
                if randomList[randInt] == num:
                    break
                else:
                    randomList[randInt], randomList[num] = (
                        randomList[num],
                        randomList[randInt],
                    )

            if randomList[0] != 0:
                return randomList

    def sendEmails(self):
        """
        Sends emails to all participants informing them of their draw
        """
        degenerateList = self._randomPicks()
        for num in degenerateList:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login(self.myEmail, self.myPassword)
            message = MIMEMultipart()
            message["From"] = self.myEmail
            message["To"] = self.emails[num]
            message["Subject"] = "Secret Santa! 🎅🎄"
            messageContent = f"""Hello there {self.members[num]}!

As a part of this time's Secret Santa, you have been drawn:
{self.members[degenerateList[num]]}

The budget for this Secret Santa has been limited to {self.budget}.
Gift exchange will be on {self.date} at {self.location}.

Merry Christmas!
🎅 ❄️ 🎁 🦌 ⛄ 👪 🎄
"""

            message.attach(MIMEText(messageContent, "plain"))
            s.sendmail(self.myEmail, self.emails[num], message.as_string())
            print("Sent Email To:", self.members[num])
            s.quit()


if __name__ == "__main__":
    santa = SantasElf()
    santa.sendEmails()