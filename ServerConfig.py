class ServerConfig:
    def __init__(self, serverName, serverPort, serverProtocol, MainApiArchitecture, MainApiVersion, MainApiName, MainApiDescription, MainApiBasePath):
        self.serverName = serverName
        self.serverPort = serverPort
        self.serverProtocol = serverProtocol
        self.MainApiArchitecture = MainApiArchitecture
        self.MainApiVersion = MainApiVersion
        self.MainApiName = MainApiName
        self.MainApiDescription = MainApiDescription
        self.MainApiBasePath = MainApiBasePath

    def mock_start_webserver(self):
        # Simulate starting a web server
        print(f"Mock server '{self.serverName}' of the Type:'{self.MainApiArchitecture}' started on {self.serverProtocol}://{self.serverName}:{self.serverPort}")
