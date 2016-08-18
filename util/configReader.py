# -*-coding: utf-8-*-
import ConfigParser
import sys, os


class configReader(object):
    def __init__(self, configPath):
        self.cReader = ConfigParser.ConfigParser()
        exerunningpath = os.path.dirname(sys.executable)
        exepath = os.path.dirname(sys.path[0])
        if os.path.exists(exerunningpath + '/' + configPath):
            self.cReader.read(exerunningpath + '/' + configPath)
        else:
            self.cReader.read(exepath + "\webControlClient/" + configPath)

    def readConfig(self, section, item):
        return self.cReader.get(section, item)

    def getDict(self, section):
        commandDict = {}
        items = self.cReader.items(section)
        for key, value in items:
            commandDict[key] = value
        return commandDict