# wrapper for urllib3 to authenticate with kerberos proxy (negotiate)
import wrapt
from typing import (Any, Dict)

@wrapt.when_imported('urllib3')
def apply_patches(urllib3):
    import requests
    from requests_kerberos import HTTPKerberosAuth
    from urllib3.util import parse_url
    from urllib3.poolmanager import ProxyManager
    
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
