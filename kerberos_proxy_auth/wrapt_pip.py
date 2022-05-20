# wrapper for pip to authenticate with kerberos proxy (negotiate)
import wrapt
from typing import (Any, Dict)


@wrapt.when_imported('pip._vendor.requests')
def apply_patches(requests):
    import requests
    from requests_kerberos import HTTPKerberosAuth
    from pip._vendor.urllib3.util import parse_url
    from pip._vendor.urllib3.poolmanager import ProxyManager
    
    def proxy_from_url(proxy_url: str, proxy_headers: Dict[str, Any] = {}, **kwargs: Any) -> ProxyManager:
        if(not 'Proxy-Authorization' in proxy_headers):
            try:
                auth = HTTPKerberosAuth()
                negotiate_details = auth.generate_request_header(None, parse_url(proxy_url).host, is_preemptive=True)
                proxy_headers['Proxy-Authorization'] = negotiate_details
            except:
                pass
        return ProxyManager(proxy_url=proxy_url, proxy_headers=proxy_headers, **kwargs)
    
    requests.adapters.proxy_from_url = proxy_from_url


@wrapt.when_imported('pip._vendor.urllib3')
def apply_patches(urllib3):
    import requests
    from requests_kerberos import HTTPKerberosAuth
    from pip._vendor.urllib3.util import parse_url
    from pip._vendor.urllib3.poolmanager import ProxyManager
    
    def proxy_from_url(proxy_url: str, proxy_headers: Dict[str, Any] = {}, **kwargs: Any) -> ProxyManager:
        if(not 'Proxy-Authorization' in proxy_headers):
            try:
                auth = HTTPKerberosAuth()
                negotiate_details = auth.generate_request_header(None, parse_url(proxy_url).host, is_preemptive=True)
                proxy_headers['Proxy-Authorization'] = negotiate_details
            except:
                pass
        return ProxyManager(proxy_url=proxy_url, proxy_headers=proxy_headers, **kwargs)
    
    urllib3.poolmanager.proxy_from_url = proxy_from_url
