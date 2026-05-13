$env:STORAGE_PATH = 'C:/installs/mcp/sonarqube-mcp-storage'
$env:SONARQUBE_URL = 'https://mhaulbert-sonarqube20261.ngrok.io/'
$env:SONARQUBE_TRANSPORT = 'https'
$env:SONARQUBE_HTTP_HOST = '127.0.0.1'
$env:SONARQUBE_HTTP_PORT = '8443'
$env:SONARQUBE_HTTP_AUTH_MODE = 'TOKEN'

# Update these paths/passwords to match your certificate material.
$env:SONARQUBE_HTTPS_KEYSTORE_PATH = 'C:/installs/mcp/sonarqube-mcp-server/certs/keystore.p12'
$env:SONARQUBE_HTTPS_KEYSTORE_PASSWORD = 'changeit'
$env:SONARQUBE_HTTPS_KEYSTORE_TYPE = 'PKCS12'
$env:SONARQUBE_HTTPS_TRUSTSTORE_PATH = 'C:/installs/mcp/sonarqube-mcp-server/certs/truststore.p12'
$env:SONARQUBE_HTTPS_TRUSTSTORE_PASSWORD = 'changeit'
$env:SONARQUBE_HTTPS_TRUSTSTORE_TYPE = 'PKCS12'

if (-not (Test-Path $env:SONARQUBE_HTTPS_KEYSTORE_PATH)) {
  throw "Keystore not found at $($env:SONARQUBE_HTTPS_KEYSTORE_PATH). Create one first, then rerun this script."
}

java -jar C:/installs/mcp/sonarqube-mcp-server/build/libs/sonarqube-mcp-server-1.19-SNAPSHOT.jar
