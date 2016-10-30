#!/usr/bin/env python

import sys

from boto.ec2 import EC2Connection

csv_file = open('instances.csv','w+')

def get_instances(connection):
  return [instance for reservation in connection.get_all_instances() for instance in reservation.instances ]

if __name__ == '__main__':
  fn = 'instances.csv'
  if len(sys.argv) > 1:
    fn = sys.argv[1]

  connection = EC2Connection()
  instances = get_instances(connection)
  with open(fn, 'w') as f:
    for instance in instances:
      f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (instance.id, instance.tags.get('Name',''),
        instance.private_ip_address, instance.public_dns_name, instance.state, instance.placement,
        instance.architecture, instance.vpc_id, instance.kernel, instance.instance_type,
        instance.image_id, instance.launch_time))
