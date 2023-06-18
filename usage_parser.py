import typing


class UsageParser(object):
    @staticmethod
    def parseExtended (decodeList: list) -> typing.Dict:
        extendedDict = {}

        extendedDict["id"] = int(decodeList[0])
        extendedDict["dmcc"] = decodeList[1]
        extendedDict["mnc"] = int(decodeList[2])
        extendedDict["bytes_used"] = int(decodeList[3])
        extendedDict["cellid"] = int(decodeList[4])
        extendedDict["ip"] = None

        return (extendedDict)
        
    @staticmethod
    def parseHex (decodeList: list) -> typing.Dict:
        # Since this is a hexadecimal, the non-id integers must be base-16
        hexDict = {}

        hexDict["id"] = int(decodeList[0])
        hexDict["mnc"] = int(decodeList[1][0:4],16)
        hexDict["dmcc"] = None
        hexDict["bytes_used"] = int(decodeList[1][4:8],16)
        hexDict["cellid"] = int(decodeList[1][8:16],16)
        hexDict["ip"] = UsageParser.createHexIP(decodeList[1][16:])

        return (hexDict)
    '''
    Description: Takes in the last 8 characters in the string: decodeList and turns into a an ip address 
    It first joins them into groups of 2 character strings, converts those strings to base 16 integers, 
    then joins them back into 1 string which is returned 

    bytes: a list of strings representing each hexadecimal bit to be converted 

    intBytes: a list of base 16 integers 

    ip: A string representing the final ip address
    '''
    @staticmethod    
    def createHexIP (decodeList: list) -> typing.ByteString:
        bytes = ["".join(x) for x in zip(*[iter(decodeList)]*2)]
        intBytes = [int(x, 16) for x in bytes]
        ip = ".".join(str(x) for x in intBytes)
        return ip

    @staticmethod
    def parseBasic (decodeList: list) -> typing.Dict:
        basicDict = {}

        basicDict["id"] = int(decodeList[0])
        basicDict["bytes_used"] = int(decodeList[1])
        basicDict["cellid"] = None
        basicDict["dmcc"] = None
        basicDict["ip"] = None
        basicDict["mnc"] = None

        return (basicDict)
    
    '''
    Description: Takes in a tuple of strings, for each string it determines which parsing method should be used,
    and then appends the result to a list which is returned. 

    finalParsedList : A list of Dictionaries that contains the parsed strings 

    decodeList : A list of each entry from the input 

    id : a string representing the id, is always the first item in decodeList

    lastDigit : the last digit in the id, determines which parsing method should be used
    '''   
    @staticmethod
    def parse(*input: str) -> typing.List[typing.Mapping[str, typing.Any]]:

        finalParsedList = []

        for entry in input:

            decodeList = entry.split(",")
            id = decodeList[0]
            lastDigit = id[-1]

            if lastDigit == '4':
                finalParsedList.append(UsageParser.parseExtended(decodeList))
            elif lastDigit == '6':
                finalParsedList.append(UsageParser.parseHex(decodeList))
            else:
                finalParsedList.append(UsageParser.parseBasic(decodeList))
        
        return finalParsedList
           
        

