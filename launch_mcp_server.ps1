$env:STORAGE_PATH = 'C:/installs/mcp/sonarqube-mcp-storage'
$env:SONARQUBE_URL = 'https://mhaulbert-sonarqube20261.ngrok.io/'
$env:SONARQUBE_TRANSPORT = 'http'
$env:SONARQUBE_HTTP_HOST = '127.0.0.1'
$env:SONARQUBE_HTTP_PORT = '8082'
$env:SONARQUBE_HTTP_AUTH_MODE = 'TOKEN'

java -jar C:/installs/mcp/sonarqube-mcp-server/build/libs/sonarqube-mcp-server-1.19-SNAPSHOT.jar
