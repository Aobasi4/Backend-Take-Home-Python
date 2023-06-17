import typing


class UsageParser(object):
    @staticmethod
    def parse(*input: str) -> typing.List[typing.Mapping[str, typing.Any]]:
        #This method will determine which of the other parse methods should be used and then pass the
        # Object to said parse method. Then return it
        pass
    def parseExtended (object) -> typing.List:
        pass
    def parseHex (object) -> typing.List:
        pass
    #Takes in a List and return a JSON-ish object containing the ID and bytes_used which are both integers
    # Note to Amara: You can speicfy that this List is String to Int for clairty 
    def parseBasic (object) -> typing.List:
        basicList = {}

        basicList["id"] = object[0]
        basicList["bytes_used"] = object[1]

        return ([basicList])
        pass

