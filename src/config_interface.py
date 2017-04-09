from configparser import SafeConfigParser

# interface for uniformly interacting with the config file

# open and parse the config file
# returns a SafeConfigParser object
def readConfig(file="../config.ini"):
        parser = SafeConfigParser()
        parser.read(file)
        return parser

# write updated config info to file
def writeConfig(parser, file="../config.ini"):
        # safe file handling
        with open(file, 'wb') as configfile:
                parser.write(configfile)
