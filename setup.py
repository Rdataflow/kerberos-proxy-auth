import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description=readme.read()

# ToDo: rework to support other environments (currently only: windows/system)
packages_path='lib/site-packages'

setup(
    name='kerberos-proxy-auth',
    version='0.0.2',
    #use_scm_version=True,
    # intentionally drop scm_version to support manual download
    # and pip install /path/to/kerberos-proxy-auth-main.zip
    #setup_requires=['setuptools_scm'],
    description='This package patches requests at runtime to authenticate with kerberos proxy (negotiate)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rdataflow',
    author_email='waldgis@bafu.admin.ch',
    license='BSD',
    url='https://github.com/Rdataflow/kerberos-proxy-auth',
    packages=['kerberos_proxy_auth'],
    data_files=[(packages_path, ['kerberos-proxy-auth-init.pth'])],
    install_requires=['wrapt>=1.10.4', 'requests-kerberos>=0.14.0'],# 'setuptools_scm'],
)
