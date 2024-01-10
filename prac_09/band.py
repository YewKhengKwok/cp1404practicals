"""
CP1404/CP5632 Practical
Band class
"Band has Musicians" in much the same way that "Musician has Guitars" (association)
"""


class Band:
    """Band class"""

    def __init__(self, name):
        """Band class constructor"""
        self.band_name = name
        self.band_members = []

    def __str__(self):
        """Return a string representation of members and their info."""
        members_info = []
        for member in self.band_members:
            instruments_info = ", ".join(str(instrument) for instrument in member.instruments)
            member_info = f"{member.name} ([{instruments_info}])"
            members_info.append(member_info)

        return f"{self.band_name} ({', '.join(members_info)})"

    def add(self, musician):
        """Method add musician as band members"""
        self.band_members.append(musician)

    def play(self):
        """Method returns what the member is playing or needs an instrument"""
        output = []
        for member in self.band_members:
            if member.instruments:
                instruments_info = ", ".join(str(instrument) for instrument in member.instruments)
                output.append(f"{member.name} is playing: {instruments_info}")
            else:
                output.append(f"{member.name} needs an instrument!")

        return '\n'.join(output)
