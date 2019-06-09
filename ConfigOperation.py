import os
import json
from TwCommon import Lang

_CONFIG_FILE_PATH = 'config.json'
_SUPPORTED_CONFIGS = {
'CN_FILE_PATH': '',
'EN_FILE_PATH': '',
'CN_FILE_LINE': 0,
'EN_FILE_LINE': 0
}
    
class ConfigOperation():
    def __init__(self):
        global _CONFIG_FILE_PATH
        global _SUPPORTED_CONFIGS
        exists = os.path.isfile(_CONFIG_FILE_PATH)
        if not exists:
            with open(_CONFIG_FILE_PATH, 'w') as f:
                json.dump(_SUPPORTED_CONFIGS, f)
                f.close()


    def getConfigData(self, key):
        global _CONFIG_FILE_PATH
        with open(_CONFIG_FILE_PATH, 'r') as f:
            configs = json.load(f)
            f.close()
            return configs[key] 

    
    def setConfigData(self, key, value):
        global _CONFIG_FILE_PATH    
        with open(_CONFIG_FILE_PATH, 'r') as f:
            configs = json.load(f)
            f.close()
        configs[key] = value
        with open(_CONFIG_FILE_PATH, 'w') as f:
            json.dump(configs, f)
            f.close()

    def getDocPath(self, lang):
        return self.getConfigData('CN_FILE_PATH') if lang==Lang.Chinese else self.getConfigData('EN_FILE_PATH')

    def setDocPath(self, value, lang):
        self.setConfigData('CN_FILE_PATH' if lang==Lang.Chinese else 'EN_FILE_PATH', value)

    def getDocLineNum(self, lang):
        return self.getConfigData('CN_FILE_LINE') if lang==Lang.Chinese else self.getConfigData('EN_FILE_LINE')
    
    def setDocLineNum(self, value, lang):
        self.setConfigData('CN_FILE_LINE' if lang==Lang.Chinese else 'EN_FILE_LINE', value)

    
if __name__ == "__main__":
    obj = ConfigOperation()
    print (obj.getDocPath(Lang.English))

