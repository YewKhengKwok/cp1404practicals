"""
CP1404/CP5632 Practical
Band class
"""
from musician import Musician
from guitar import Guitar


class Band:

    def __init__(self, name):
        self.band_name = name
        self.band_members = []

    def __str__(self):
        members_info = []
        for member in self.band_members:
            instruments_info = ", ".join(str(instrument) for instrument in member.instruments)
            member_info = f"{member.name} ([{instruments_info}])"
            members_info.append(member_info)

        return f"{self.band_name} ({', '.join(members_info)})"

    def add(self, musician):
        self.band_members.append(musician)

    def play(self):
        output = []
        for member in self.band_members:
            if member.instruments:
                instruments_info = ", ".join(str(instrument) for instrument in member.instruments)
                output.append(f"{member.name} is playing: {instruments_info}")
            else:
                output.append(f"{member.name} needs an instrument!")

        return '\n'.join(output)
