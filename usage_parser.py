import typing


class UsageParser(object):
    @staticmethod
    def parseExtended (object) -> typing.List:
        pass
    @staticmethod
    def parseHex (object) -> typing.List:
        pass
    #Takes in a List and return a JSON-ish object containing the ID and bytes_used which are both integers
    # Note to Amara: You can speicfy that this List is String to Int for clairty 
    # Note: The parse method essentially will be a for loop that creates the Json object because you have multiple per input! 
    # Make variable names more conscise and make sure you're workflow is well commented and stuff
    @staticmethod
    def parseBasic (obj) -> typing.List:
        basicList = {}

        basicList["id"] = int(obj[0])
        basicList["bytes_used"] = int(obj[1])
        basicList["cellid"] = None
        basicList["dmcc"] = None
        basicList["ip"] = None
        basicList["mnc"] = None

        return (basicList)
        

    @staticmethod
    def parse(*input: str) -> typing.List[typing.Mapping[str, typing.Any]]:
        #This method will determine which of the other parse methods should be used and then pass the
        # Object to said parse method. Then return it
        finalEmptyList = []
        decodeArray = input[0].split(",")
        id = decodeArray[0]
        #Determine what kind of parsing needs to be done
        for entry in input:
            decodeArray = entry.split(",")
            id = decodeArray[0]
            if id[-1] == 4:
                finalEmptyList.append(UsageParser.parseExtended(decodeArray))
            elif id[-1] == 6:
                finalEmptyList.append(UsageParser.parseHex(decodeArray))
            else:
                finalEmptyList.append(UsageParser.parseBasic(decodeArray))
        
        return finalEmptyList
           
        

