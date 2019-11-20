#!/usr/bin/python3
# $ ./whois_cli.py 52.3.137.27
# prints whois data to terminal
# made available under MIT license (see LICENSE)

from ipwhois import IPWhois
from sys import argv

w = IPWhois(argv[1]).lookup_rdap()
objs = w["objects"]
objs1 = list(objs.keys())
net = w["network"]

# ASN
_asn = {
    "asn": "Number",
    "asn_cidr": "CIDR",
    "asn_country_code": "Country code",
    "asn_date": "Date",
    "asn_description": "Description",
    "asn_registry": "Registry"
}
# Network general
net_gen = {
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
# Network status
net_stat = net["status"]
# Network remarks
net_rmrks = net["remarks"]
net_rmrks1 = {
    "title": "Title",
    "description": "Description",
    "links": "Links"
}
# Network notices
net_notc = {
    "description": "Description",
    "links": "Links",
    "title": "Title"
}
net_notc1 = net["notices"]
# Network events
net_evnts = {
    "action": "Action",
    "actor": "Actor",
    "timestamp": "Timestamp"
}
net_evnts1 = net["events"]
# Objects general
obj_misc = {
    'events_actor': 'Events actor',
    'handle': 'Handle',
    'notices': 'Notices',
    'raw': 'Raw'
}
obj_misc_keys = list(obj_misc.keys())
# Objects contact
obj_contact = {
    "email": "Email",
    "kind": "Kind",
    "name": "Name",
    "phone": "Phone",
    "role": "Role",
    "title": "Title"
}
obj_contact1 = list(obj_contact.keys())
# Objects address
obj_add = {
    'type': 'Type',
    'value': 'Value'
}
# Objects events
obj_evnt = {
    "action": "Action",
    "timestamp": "Timestamp",
    "actor": "Actor"
}
# Objects remarks
obj_rmrks = {
    "title": "Title",
    "description": "Description",
    "links": "Links"
}

print(f'\033[0;31mASN\033[m =================================================')

for i in _asn:
    if w[i] is None:
        print(f'\033[0;36m{_asn[i]}\033[0m: n/a')
    else:
        print(f'\033[0;36m{_asn[i]}\033[0m: {w[i]}')

print('\033[0;31mNetwork general\033[m ======================================')

for i in net_gen:
    if net[i] is None:
        print(f'\033[0;36m{net_gen[i]}\033[0m: n/a')
    else:
        print(f'\033[0;36m{net_gen[i]}\033[0m: {net[i]}')  # Network general

if net_stat is None:
    print(f'\033[0;36mStatus:\033[0m: n/a')
else:
    print(f'\033[0;36mStatus\033[0m: {net_stat[0]}')  # Network status

print('\033[0;31mNetwork remarks\033[m ======================================')

if net_rmrks is None:
    print(f'n/a')
else:
    for i in net_rmrks1:
        if net_rmrks[0][i] is None:
            print(f'\033[0;36m{net_rmrks1[i]}\033[0m: n/a')
        else:
            print(f'\033[0;36m{net_rmrks1[i]}\033[0m: {net_rmrks[0][i]}')
            # Network remarks

print('\033[0;31mNetwork links\033[m ========================================')

for i in net["links"]:
    print(i)  # Network links

print('\033[0;31mNetwork notices\033[m ======================================')

n = 0
for i in net_notc1:
    for j in i:
        if net_notc1[n][j] is None:
            print(f'\033[0;36m{net_notc[j]}\033[0m: n/a')
        elif type(net_notc1[n][j]) == list:
            print(f'\033[0;36m{net_notc[j]}\033[0m: \
                {net_notc1[n][j][0]}')
        else:
            print(f'\033[0;36m{net_notc[j]}\033[0m: \
                {net_notc1[n][j]}')  # Network notices
    n += 1

print('\033[0;31mNetwork events\033[m =======================================')

n = 0
for i in net_evnts1:
    for j in i:
        if net_evnts1[n][j] is None:
            print(f'\033[0;36m{net_evnts[j]}\033[0m: n/a')
        else:
            print(f'\033[0;36m{net_evnts[j]}\033[0m: \
            {net_evnts1[n][j]}')  # Network events
    n += 1

print('\033[0;31mNIR \033[m =================================================')

_nir = f'\033[0;36mNIR\033[0m: n/a' if w["nir"] is None else f'\033[0;36mNIR\033[0m: {w["nir"]}'
print(_nir)

print('\033[0;31mObjects general\033[m ======================================')

for i in objs:
    for j in obj_misc_keys:
        if objs[i][j] is None:
            print(f'\033[0;36m{i} {obj_misc[j]}\033[0m: n/a')
        else:
            print(f'\033[0;36m{i} {obj_misc[j]}\033[0m: {objs[i][j]}')

print('\033[0;31mObjects contact\033[m ======================================')

for i in objs:
    if objs[i]["contact"] is None:
        print(f'\033[0;36mContact {i}\033[0m: n/a')
    else:
        for j in obj_contact1:
            if objs[i]["contact"][j] is None:
                print(f'\033[0;36m{obj_contact[j]}\033[0m: n/a')
            elif isinstance(objs[i]["contact"][j], list):
                if objs[i]["contact"][j][0]["type"] is None:
                    print(f'\033[0;36m{obj_contact[j]} type\033[0m: n/a')
                elif isinstance(objs[i]["contact"][j][0]["type"], list):
                    print(f'\033[0;36m{obj_contact[j]} type\033[0m:')
                    for k in objs[i]["contact"][j][0]["type"]:
                        print(f'{k}')
                else:
                    print(f'\033[0;36m{obj_contact[j]} type\033[0m: \
                        {objs[i]["contact"][j][0]["type"]}')
                print(f'\033[0;36m{obj_contact[j]} value\033[0m: \
                    {objs[i]["contact"][j][0]["value"]}')
            else:
                print(f'\033[0;36m{obj_contact[j]}\033[0m: \
                    {objs[i]["contact"][j]}')  # Objects contact

print('\033[0;31mObjects contact address\033[m ==============================')

for i in objs:
    try:
        for j in objs[i]["contact"]["address"][0].keys():
            if objs[i]["contact"]["address"][0][j] is None:
                print(f'\033[0;36m{obj_add[j]} {i}\033[0m: n/a')
            else:
                print(f'\033[0;36m{obj_add[j]} {i}\033[0m: \
                    {objs[i]["contact"]["address"][0][j]}')
    except TypeError:
        print(f'\033[0;36mContact address {i}\033[0m: n/a')

print('\033[0;31mObjects entities\033[m =====================================')

for i in objs:
    if objs[i]["entities"] is None:
        print(f'\033[0;36m{i} entity\033[0m: n/a')
    else:
        for j in objs[i]["entities"]:
            print(j)  # Object entities

print('\033[0;31mObjects events\033[m =======================================')

for i in objs1:
    if objs[i]["events"] is None:
        print(f'\033[0;36m{i} event:\033[0m: n/a')
    else:
        c = 0
        for j in objs[i]["events"]:
            for k in j:
                print(f'\033[0;36m{obj_evnt[k]}\033[0m: \
                    {objs[i]["events"][c][k]}')  # Objects events
            c += 1

print('\033[0;31mObjects links\033[m ========================================')

for i in objs:
    if objs[i]["links"] is None:
        print(f'\033[0;36m{i} links\033[0m: n/a')
    else:
        for j in objs[i]["links"]:
            print(j)  # Objects links

print('\033[0;31mObjects remarks\033[m ======================================')

for i in objs:
    if objs[i]["remarks"] is None:
        print(f'\033[0;36m{i} remarks\033[0m: n/a')
    else:
        obj_rmrks1 = list(objs[i]["remarks"][0].keys())
        c = 0
        for j in objs[i]["remarks"]:
            for k in range(len(obj_rmrks1)):
                print(f'\033[0;36m{i} {obj_rmrks[obj_rmrks1[k]]}\033[0m: \
                    {objs[i]["remarks"][c][obj_rmrks1[k]]}')  # Objects remarks
            c += 1

print('\033[0;31mObjects roles\033[m ========================================')

for i in objs:
    if objs[i]["roles"] is None:
        print(f'\033[0;36m{i} roles\033[0m: n/a')
    else:
        for j in objs[i]["roles"]:
            print(f'\033[0;36m{i} roles\033[0m: {j}')  # Objects roles

print('\033[0;31mObjects status\033[m =======================================')

for i in objs:
    if objs[i]["status"] is None:
        print(f'\033[0;36m{i} status\033[0m: n/a')
    else:
        for j in objs[i]["status"]:
            print(f'\033[0;36m{i} status\033[0m: {j}')  # Objects status

print('\033[0;31mRaw\033[m ==================================================')

if w["raw"] is None:
    print(f'n/a')
else:
    print(f'{w["raw"]}')  # Raw
