"""C:\Users\liwen>set http_proxy=http://127.0.0.1:1080

C:\Users\liwen>set https_proxy=http://127.0.0.1:1080

C:\Users\liwen>pip install scrapy
Collecting scrapy
  Downloading https://files.pythonhosted.org/packages/5d/12/a6197eaf97385e96fd8ec56627749a6229a9b3178ad73866a0b1fb377379/Scrapy-1.5.1-py2.py3-none-any.whl (249kB)
    100% |████████████████████████████████| 256kB 47kB/s
Collecting PyDispatcher>=2.0.5 (from scrapy)
  Downloading https://files.pythonhosted.org/packages/cd/37/39aca520918ce1935bea9c356bcbb7ed7e52ad4e31bff9b943dfc8e7115b/PyDispatcher-2.0.5.tar.gz
Collecting service-identity (from scrapy)
  Downloading https://files.pythonhosted.org/packages/29/fa/995e364220979e577e7ca232440961db0bf996b6edaf586a7d1bd14d81f1/service_identity-17.0.0-py2.py3-none-any.whl
Requirement already satisfied: six>=1.5.2 in d:\program files (x86)\python36\lib\site-packages (from scrapy) (1.11.0)
Collecting queuelib (from scrapy)
  Downloading https://files.pythonhosted.org/packages/4c/85/ae64e9145f39dd6d14f8af3fa809a270ef3729f3b90b3c0cf5aa242ab0d4/queuelib-1.5.0-py2.py3-none-any.whl
Collecting lxml (from scrapy)
  Downloading https://files.pythonhosted.org/packages/3c/06/d8db111411e4ad0677d72985af1d45ead6f1d0e8d09d80bddc45c1f91cfe/lxml-4.2.3-cp36-cp36m-win_amd64.whl (3.6MB)
    100% |████████████████████████████████| 3.6MB 85kB/s
Collecting cssselect>=0.9 (from scrapy)
  Downloading https://files.pythonhosted.org/packages/7b/44/25b7283e50585f0b4156960691d951b05d061abf4a714078393e51929b30/cssselect-1.0.3-py2.py3-none-any.whl
Collecting w3lib>=1.17.0 (from scrapy)
  Downloading https://files.pythonhosted.org/packages/37/94/40c93ad0cadac0f8cb729e1668823c71532fd4a7361b141aec535acb68e3/w3lib-1.19.0-py2.py3-none-any.whl
Collecting Twisted>=13.1.0 (from scrapy)
  Downloading https://files.pythonhosted.org/packages/90/50/4c315ce5d119f67189d1819629cae7908ca0b0a6c572980df5cc6942bc22/Twisted-18.7.0.tar.bz2 (3.1MB)
    100% |████████████████████████████████| 3.1MB 300kB/s
Collecting parsel>=1.1 (from scrapy)
  Downloading https://files.pythonhosted.org/packages/fd/1a/9642a5ea68763d5e7c419df0873073e54bb23d0a8897d3c78e146dd6f355/parsel-1.5.0-py2.py3-none-any.whl
Collecting pyOpenSSL (from scrapy)
  Downloading https://files.pythonhosted.org/packages/96/af/9d29e6bd40823061aea2e0574ccb2fcf72bfd6130ce53d32773ec375458c/pyOpenSSL-18.0.0-py2.py3-none-any.whl (53kB)
    100% |████████████████████████████████| 61kB 71kB/s
Collecting pyasn1-modules (from service-identity->scrapy)
  Downloading https://files.pythonhosted.org/packages/19/02/fa63f7ba30a0d7b925ca29d034510fc1ffde53264b71b4155022ddf3ab5d/pyasn1_modules-0.2.2-py2.py3-none-any.whl (62kB)
    100% |████████████████████████████████| 71kB 132kB/s
Collecting attrs (from service-identity->scrapy)
  Downloading https://files.pythonhosted.org/packages/41/59/cedf87e91ed541be7957c501a92102f9cc6363c623a7666d69d51c78ac5b/attrs-18.1.0-py2.py3-none-any.whl
Collecting pyasn1 (from service-identity->scrapy)
  Downloading https://files.pythonhosted.org/packages/a0/70/2c27740f08e477499ce19eefe05dbcae6f19fdc49e9e82ce4768be0643b9/pyasn1-0.4.3-py2.py3-none-any.whl (72kB)
    100% |████████████████████████████████| 81kB 75kB/s
Collecting zope.interface>=4.4.2 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/5d/d7/aba043947b0fa58a2dd6d5e25295426508c834945840954182099c676910/zope.interface-4.5.0-cp36-cp36m-win_amd64.whl (132kB)
    100% |████████████████████████████████| 133kB 113kB/s
Collecting constantly>=15.1 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/b9/65/48c1909d0c0aeae6c10213340ce682db01b48ea900a7d9fce7a7910ff318/constantly-15.1.0-py2.py3-none-any.whl
Collecting incremental>=16.10.1 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/f5/1d/c98a587dc06e107115cf4a58b49de20b19222c83d75335a192052af4c4b7/incremental-17.5.0-py2.py3-none-any.whl
Collecting Automat>=0.3.0 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/a3/86/14c16bb98a5a3542ed8fed5d74fb064a902de3bdd98d6584b34553353c45/Automat-0.7.0-py2.py3-none-any.whl
Collecting hyperlink>=17.1.1 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/a7/b6/84d0c863ff81e8e7de87cff3bd8fd8f1054c227ce09af1b679a8b17a9274/hyperlink-18.0.0-py2.py3-none-any.whl
Collecting PyHamcrest>=1.9.0 (from Twisted>=13.1.0->scrapy)
  Downloading https://files.pythonhosted.org/packages/9a/d5/d37fd731b7d0e91afcc84577edeccf4638b4f9b82f5ffe2f8b62e2ddc609/PyHamcrest-1.9.0-py2.py3-none-any.whl (52kB)
    100% |████████████████████████████████| 61kB 228kB/s
Collecting cryptography>=2.2.1 (from pyOpenSSL->scrapy)
  Downloading https://files.pythonhosted.org/packages/67/62/67faef32908026e816a74b4b97491f8b9ff393d2951820573599c105cc32/cryptography-2.2.2-cp36-cp36m-win_amd64.whl (1.3MB)
    100% |████████████████████████████████| 1.3MB 438kB/s
Requirement already satisfied: setuptools in d:\program files (x86)\python36\lib\site-packages (from zope.interface>=4.4.2->Twisted>=13.1.0->scrapy) (39.0.1)
Requirement already satisfied: idna>=2.5 in d:\program files (x86)\python36\lib\site-packages (from hyperlink>=17.1.1->Twisted>=13.1.0->scrapy) (2.7)
Collecting asn1crypto>=0.21.0 (from cryptography>=2.2.1->pyOpenSSL->scrapy)
  Downloading https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl (101kB)
    100% |████████████████████████████████| 102kB 152kB/s
Collecting cffi>=1.7; platform_python_implementation != "PyPy" (from cryptography>=2.2.1->pyOpenSSL->scrapy)
  Downloading https://files.pythonhosted.org/packages/2f/85/a9184548ad4261916d08a50d9e272bf6f93c54f3735878fbfc9335efd94b/cffi-1.11.5-cp36-cp36m-win_amd64.whl (166kB)
    100% |████████████████████████████████| 174kB 366kB/s
Collecting pycparser (from cffi>=1.7; platform_python_implementation != "PyPy"->cryptography>=2.2.1->pyOpenSSL->scrapy)
  Downloading https://files.pythonhosted.org/packages/8c/2d/aad7f16146f4197a11f8e91fb81df177adcc2073d36a17b1491fd09df6ed/pycparser-2.18.tar.gz (245kB)
    100% |████████████████████████████████| 256kB 233kB/s
Building wheels for collected packages: PyDispatcher, Twisted, pycparser
  Running setup.py bdist_wheel for PyDispatcher ... done
  Stored in directory: C:\Users\liwen\AppData\Local\pip\Cache\wheels\88\99\96\cfef6665f9cb1522ee6757ae5955feedf2fe25f1737f91fa7f
  Running setup.py bdist_wheel for Twisted ... done
  Stored in directory: C:\Users\liwen\AppData\Local\pip\Cache\wheels\a9\85\24\fc82998fb686cb31e65a26c027a20120fd1219c9f1e925913a
  Running setup.py bdist_wheel for pycparser ... done
  Stored in directory: C:\Users\liwen\AppData\Local\pip\Cache\wheels\c0\a1\27\5ba234bd77ea5a290cbf6d675259ec52293193467a12ef1f46
Successfully built PyDispatcher Twisted pycparser
Installing collected packages: PyDispatcher, pyasn1, pyasn1-modules, attrs, asn1crypto, pycparser, cffi, cryptography, pyOpenSSL, service-identity, queuelib, lxml, cssselect, w3lib, zope.interface, constantly, incremental, Automat, hyperlink, PyHamcrest, Twisted, parsel, scrapy
Successfully installed Automat-0.7.0 PyDispatcher-2.0.5 PyHamcrest-1.9.0 Twisted-18.7.0 asn1crypto-0.24.0 attrs-18.1.0 cffi-1.11.5 constantly-15.1.0 cryptography-2.2.2 cssselect-1.0.3 hyperlink-18.0.0 incremental-17.5.0 lxml-4.2.3 parsel-1.5.0 pyOpenSSL-18.0.0 pyasn1-0.4.3 pyasn1-modules-0.2.2 pycparser-2.18 queuelib-1.5.0 scrapy-1.5.1 service-identity-17.0.0 w3lib-1.19.0 zope.interface-4.5.0
"""