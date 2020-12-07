import pandas as pd
import sys

from random import randint


class SantaException(Exception):
    """
    Someone's on Santa's Naughty List
    """

    pass


class SantasElf:
    def __init__(self):
        clArgs = sys.argv
        if len(clArgs) < 2:
            raise SantaException()
        self.dataFile = clArgs[1]
        self._extractData()

    def _extractData(self):
        """
        Retrieve members and emails from datafile
        """
        _df = pd.read_csv(self.dataFile)
        self.members = _df["Name"].tolist()
        self.emails = _df["Email"].tolist()

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
        self._randomPicks()


if __name__ == "__main__":
    santa = SantasElf()
    santa.sendEmails()