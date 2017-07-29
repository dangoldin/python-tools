import json

with open('instances.json', 'r') as f:
    r = f.read()

j = json.loads(r)

for r in j['Reservations']:
    for i in r['Instances']:
        public_dns_name = i['PublicDnsName']
        private_dns_name = i['PrivateDnsName']
        name = ''
        for t in i.get('Tags',[]):
            if t['Key'] == 'Name':
                name = t['Value']
        print public_dns_name, ',', private_dns_name, ',', name
