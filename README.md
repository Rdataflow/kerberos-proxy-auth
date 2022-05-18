# kerberos-proxy-auth
This package patches `requests` at runtime to authenticate with kerberos proxy (spnego)

## Installation
From behind the proxy 
1. download [this package manually](../../archive/refs/heads/main.zip)
2. run this command
```Shell
pip install path/to/kerberos-proxy-auth-main.zip
```

## Usage
After installation
1. set the environment variables
```Shell
set https_proxy=http://<kerberosproxy>:8080
set http_proxy=http://<kerberosproxy>:8080
```
2. start python and use requests even from behind the kerberos proxy without any further action.
```python
import requests
r = requests.get('https://example.org')
print(r.status_code)
# expected: 200

r = requests.head('https://example.org')
print(r.status_code)
# expected: 200

r = requests.request('GET', 'https://example.org')
print(r.status_code)
# expected : 200
```

## ToDo
- test, feedback, contribute improvements
- rework to support other environments (currently only: windows/system)
- publish as python package on pypi.org
- support more packages i.e. `urllib3` and `botocore`
