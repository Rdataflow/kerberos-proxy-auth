# kerberos-proxy-auth
This package patches `requests` and `urllib3` at runtime to authenticate with kerberos proxy (spnego)

## Installation

### a) using a NON-kerberos proxy (if available)
1. set the environment variables to NON-kerberos proxy and use `pip install ...`
	```Shell
	set https_proxy=http://<NONkerberosproxy>:8080
	set http_proxy=http://<NONkerberosproxy>:8080
	pip install https://<path/to/this/repo>/kerberos-proxy-auth/archive/refs/heads/main.zip
	```

### b) from behind the kerberos proxy
1. download [this package manually](../../archive/refs/heads/main.zip) as well as all its dependancies.
2. run this command
	```Shell
	pip install path/to/kerberos-proxy-auth-main.zip path/to/dependancy1.zip path/to/dependancy2.zip [...]
	```

## Usage
After installation
1. set the environment variables
	```Shell
	set https_proxy=http://<kerberosproxy>:8080
	set http_proxy=http://<kerberosproxy>:8080
	```
2. start python and use `requests`, `urllib3` or `pip` even from behind the kerberos proxy without any further action.
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

	import urllib3, os
	http = urllib3.poolmanager.proxy_from_url(os.getenv('https_proxy'))
	r = http.request('GET', 'https://example.org')
	print(r.status)
	# expected : 200
	```

## ToDo
- test, feedback, contribute improvements
- rework to support other environments (currently only: windows/system)
- publish as python package on pypi.org
