#!/usr/bin/python3
# $ ./whois_cli.py 52.3.137.27
# prints whois data to terminal
# made available under MIT license (see LICENSE)

from ipwhois import IPWhois
from sys import argv

w = IPWhois(argv[1]).lookup_rdap()
_net = w["network"]
_obj = w["objects"]
red = "\x1b[0;31m"
cyan = "\x1b[0;36m"
end = "\x1b[0m"

# ASN
_asn = {
    "asn": "ASN",
    "asn_cidr": "CIDR",
    "asn_country_code": "Country code",
    "asn_date": "Date",
    "asn_description": "Description",
    "asn_registry": "Registry"
}
# Network general
net_misc = {
    "name": "Name",
    "cidr": "CIDR",
    "start_address": "Start address",
    "end_address": "End address",
    "ip_version": "IP version",
    "handle": "Handle",
    "parent_handle": "Parent handle",
    "country": "Country",
    "type": "Type",
    "raw": "Raw"
}
# Network remarks
net_remarks = {
    "title": "Title",
    "description": "Description",
    "links": "Links"
}
# Network notices
net_notices = {
    "description": "Description",
    "links": "Links",
    "title": "Title"
}
# Network events
net_events = {
    "action": "Action",
    "actor": "Actor",
    "timestamp": "Timestamp"
}
# Objects general
obj_misc = {
    'events_actor': 'events actor',
    'handle': 'handle',
    'notices': 'notices',
    'raw': 'raw'
}
# Objects contact
obj_contact = {
    "email": "email",
    "kind": "kind",
    "name": "name",
    "phone": "phone",
    "role": "role",
    "title": "title"
}
# Objects address
obj_add = {
    'type': 'type',
    'value': 'value'
}
# Objects events
obj_events = {
    "action": "action",
    "timestamp": "timestamp",
    "actor": "actor"
}
# Objects remarks
obj_remarks = {
    "title": "title",
    "description": "description",
    "links": "links"
}

print(f'================ {red}ASN{end} ======================================')

try:
    for k, v in _asn.items():
        print(f'{cyan}{v}{end}: {w[k]}')
except TypeError:
    print(f'{cyan}{v}{end}: n/a')

print(f'================ {red}Network misc{end} =============================')

try:
    for k, v in net_misc.items():
        print(f'{cyan}{v}{end}: {_net[k]}')
except TypeError:
    print(f'{cyan}{v}{end}: n/a')

try:
    print(f'{cyan}Status{end}: {_net["status"][0]}')
except TypeError:
    print(f'{cyan}Status{end}: n/a')

print(f'================ {red}Network remarks{end} ==========================')

try:
    for k, v in net_remarks.items():
        print(f'{cyan}{v}{end}: {_net["remarks"][0][k]}')
except TypeError:
    print(f'{cyan}{v}{end}: n/a')

print(f'================ {red}Network links{end} ============================')

[print(i) for i in _net["links"]]

print(f'================ {red}Network notices{end} ==========================')

n = 0
for k, v in net_notices.items():
    if isinstance(_net["notices"][n]["links"], list):
        print(f'{cyan}{v}{end}: {_net["notices"][n]["links"][0]}')
    else:
        print(f'{cyan}{v}{end}: {_net["notices"][n][k]}' if True else "n/a")
    n += 1

print(f'================ {red}Network events{end} ===========================')

n = 0
for i in _net["events"]:
    try:
        for k, v in net_events.items():
            print(f'{cyan}{v}{end}: {_net["events"][n][k]}')
    except TypeError:
        print(f'{cyan}{v}{end}: n/a')
    n += 1

print(f'================ {red}NIR{end} ======================================')

print(f'{w["nir"] or "n/a"}')

print(f'================ {red}Objects misc{end} =============================')

for i in _obj:
    try:
        for k, v in obj_misc.items():
            print(f'{cyan}{i} {v}{end}: {_obj[i][k]}')
    except TypeError:
        print(f'{cyan}{i} {v}{end}: n/a')

print(f'================ {red}Objects contact{end} ==========================')

for i in _obj:
    if _obj[i]["contact"] is None:
        print(f'{cyan}{i}{end}: n/a')
    else:
        for k, v in obj_contact.items():
            if _obj[i]["contact"][k] is None:
                print(f'{cyan}{i} {v}{end}: n/a')
            elif isinstance(_obj[i]["contact"][k], list):
                if _obj[i]["contact"][k][0]["type"] is None:
                    print(f'{cyan}{i} {v} type{end}: n/a')
                elif isinstance(_obj[i]["contact"][k][0]["type"], list):
                    print(f'{cyan}{i} {v} type{end}:')
                    for m in _obj[i]["contact"][k][0]["type"]:
                        print(f'{m}')
                else:
                    print(f'{cyan}{i} {v} type{end}: \
{_obj[i]["contact"][k][0]["type"]}')
                print(f'{cyan}{i} {v} value{end}: \
{_obj[i]["contact"][k][0]["value"]}')
            else:
                print(f'{cyan}{i} {v}{end}: {_obj[i]["contact"][k]}')

print(f'================ {red}Objects contact address{end} ==================')

for i in _obj:
    try:
        for k, v in obj_add.items():
            print(f'{cyan}{i} {v}{end}: {_obj[i]["contact"]["address"][0][k]}')
    except TypeError:
        print(f'{cyan}{i} {v}{end}: n/a')

print(f'================ {red}Objects entities{end} =========================')

for i in _obj:
    try:
        for j in _obj[i]["entities"]:
            print(f'{j}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')

print(f'================ {red}Objects events{end} ===========================')

for i in _obj:
    try:
        for k, v in obj_events.items():
            print(f'{cyan}{i} {v}{end}: {_obj[i]["events"][0][k]}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')  # ref. 45.32.195.192

print(f'================ {red}Objects links{end} ============================')

for i in _obj:
    try:
        for j in _obj[i]["links"]:
            print(f'{j}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')

print(f'================ {red}Objects remarks{end} ==========================')

for i in _obj:
    n = 0
    try:
        for j in _obj[i]["remarks"]:
            for k, v in obj_remarks.items():
                    print(f'{cyan}{i} {v}{end}: {_obj[i]["remarks"][n][k]}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')
        n += 1  # ref. 72.21.91.29

print(f'================ {red}Objects roles{end} ============================')

for i in _obj:
    try:
        for j in _obj[i]["roles"]:
            print(f'{cyan}{i}{end}: {j}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')

print(f'================ {red}Objects status{end} ===========================')

for i in _obj:
    try:
        for j in _obj[i]["status"]:
            print(f'{cyan}{i}{end}: {j}')
    except TypeError:
        print(f'{cyan}{i}{end}: n/a')

print(f'================ {red}Raw{end} ======================================')

print(f'{w["raw"] or "n/a"}')
