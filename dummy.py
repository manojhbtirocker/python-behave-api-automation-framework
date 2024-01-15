from utils.Config import Config

configObj = Config()

baseUrl = configObj.getApiConfig()['baseUrl']
print(baseUrl)




