# whois_cli

This repo is made available under MIT license (see `LICENSE`).

`whois_cli.py` was tested in a Unix-like terminal emulator running Bash in [Ubuntu 18.04](http://releases.ubuntu.com/18.04/).

[pip](https://pypi.org/project/pip/) was used for package management.

![screen capture](screen_capture.png)

## requirements.txt

**Note**:

1. since specific Python libraries may be used system-wide in Ubuntu&mdash;to be safe&mdash;a [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment) is required.
2. if Ubuntu is using **pip** and **pip2** for Python 2 package management, then **pip3** will be the required package manager.

To install required dependencies:

`$ pip install -r requirements.txt`

```python
dnspython==1.16.0
ipwhois==1.1.0
pkg-resources==0.0.0
```

The [sys.argv](https://docs.python.org/3/library/sys.html#sys.argv) method will also be imported.

```python
from ipwhois import IPWhois
from sys import argv
```

## whois_cli.py

`IPWhois(argv[1]).lookup_rdap()`

`ipwhois.IPWhois`
: is the base class for wrapping whois lookups.

`sys.argv[1]`
: gets first command line argument passed to `whois_cli.py` or the IPv4 number.

`IPWhois.lookup_rdap()`
: became the recommended lookup method, since [RDAP](https://www.arin.net/resources/registry/whois/rdap/) provides more efficient, higher quality whois data.

`objs = w["objects"]`
: indicates that the `objects` dictionary within the whois data will be stored in the `objs` variable.

`objs1 = list(objs.keys())`
: indicates that only the `keys` from the `objs` variable will be listed in the `objs1` variable.

```python
_asn = {
    "asn": "Number",
    "asn_cidr": "CIDR",
    "asn_country_code": "Country code",
    "asn_date": "Date",
    "asn_description": "Description",
    "asn_registry": "Registry"
}
```

The dictionary above contains ASN keys with their associated values for capitalized string syntax.

```python
for i in _asn:
    if w[i] == None:
        print(f'\033[0;36m{_asn[i]}\033[0m: n/a')
    else:
        print(f'\033[0;36m{_asn[i]}\033[0m: {w[i]}')
```

In the `for` loop above, `if` an ASN key returns `None` then some form of `n/a` string will be returned, `else` the ASN key's value will be returned.
