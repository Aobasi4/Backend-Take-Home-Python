import typing


class UsageParser(object):
    @staticmethod
    def parseExtended (obj) -> typing.List:
        # order : <id>,<dmcc>,<mnc>,<bytes_used>,<cellid> everything an int besides dmcc 
        basicList = {}

        basicList["id"] = int(obj[0])
        basicList["dmcc"] = obj[1]
        basicList["mnc"] = int(obj[2])
        basicList["bytes_used"] = int(obj[3])
        basicList["cellid"] = int(obj[4])
        basicList["ip"] = None

        return (basicList)
        
    @staticmethod
# - Bytes 1-2 → `mnc`
# - Bytes 3-4 > `bytes_used`
# - Bytes 5-8 → `cellid`
# - Bytes 9-12 → `ip`
#     - String
#     - Each byte is one segment of the ip, separated by a period: e.g. `c0a80001` would be `'192.168.0.1'`
    def parseHex (obj) -> typing.List:

        basicList = {}

        basicList["id"] = int(obj[0])
        basicList["mnc"] = int(obj[1][0:4],16)
        basicList["dmcc"] = None
        basicList["bytes_used"] = int(obj[1][4:8],16)
        basicList["cellid"] = int(obj[1][8:16],16)
        basicList["ip"] = UsageParser.createHexIP(obj[1][16:])

        return (basicList)
        
        pass
    def createHexIP (obj) -> typing.ByteString:
        bytes = ["".join(x) for x in zip(*[iter(obj)]*2)]
        bytes = [int(x, 16) for x in bytes]
        ip = ".".join(str(x) for x in bytes)
        return ip

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
        #Determine what kind of parsing needs to be done
        for entry in input:
            decodeArray = entry.split(",")
            id = decodeArray[0]
            if id[-1] == '4':
                finalEmptyList.append(UsageParser.parseExtended(decodeArray))
            elif id[-1] == '6':
                finalEmptyList.append(UsageParser.parseHex(decodeArray))
            else:
                finalEmptyList.append(UsageParser.parseBasic(decodeArray))
        
        return finalEmptyList
           
        

