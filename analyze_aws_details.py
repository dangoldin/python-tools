#!/usr/bin/env python

import sys
import pandas

def load_file(fp):
    dtype_cols = {
        'InvoiceID' : str,
        'PayerAccountId' : str,
        'LinkedAccountId' : str,
        'RecordType' : str,
        'RecordId' : str,
        'ProductName' : str,
        'RateId' : str,
        'SubscriptionId' : str,
        'PricingPlanId' : str,
        'UsageType' : str,
        'Operation' : str,
        'AvailabilityZone' : str,
        'ReservedInstance' : str,
        'ItemDescription' : str,
        'UsageStartDate' : str,
        'UsageEndDate' : str,
        'UsageQuantity' : 'float64',
        'Rate' : 'float64',
        'Cost' : 'float64',
        'ResourceId' : str,
        'aws:autoscaling:groupName' : str,
        'aws:cloudformation:logical-id' : str,
        'aws:cloudformation:stack-id' : str,
        'aws:cloudformation:stack-name' : str,
        'user:Alerts' : str,
        'user:Name' : str,
        'user:opsworks:device' : str,
        'user:opsworks:instance' : str,
        'user:opsworks:instance_id' : str,
        'user:opsworks:layer:aerospike' : str,
        'user:opsworks:layer:assetrouter' : str,
        'user:opsworks:layer:bidder' : str,
        'user:opsworks:layer:bidder3psettings' : str,
        'user:opsworks:layer:bidderservice' : str,
        'user:opsworks:layer:clusterstatus' : str,
        'user:opsworks:layer:datadashboard' : str,
        'user:opsworks:layer:datamigrator' : str,
        'user:opsworks:layer:dmpsync' : str,
        'user:opsworks:layer:druid' : str,
        'user:opsworks:layer:eb' : str,
        'user:opsworks:layer:exchange' : str,
        'user:opsworks:layer:exchangeservice' : str,
        'user:opsworks:layer:imageanalysis' : str,
        'user:opsworks:layer:imagecalculator' : str,
        'user:opsworks:layer:imagerender' : str,
        'user:opsworks:layer:impression_bus' : str,
        'user:opsworks:layer:impression_bus_service' : str,
        'user:opsworks:layer:kafka' : str,
        'user:opsworks:layer:kafka_v2' : str,
        'user:opsworks:layer:kafkaconsumer' : str,
        'user:opsworks:layer:main-zk' : str,
        'user:opsworks:layer:optimizations' : str,
        'user:opsworks:layer:prod-zk' : str,
        'user:opsworks:layer:rsupload' : str,
        'user:opsworks:layer:storm' : str,
        'user:opsworks:layer:taskservice' : str,
        'user:opsworks:mount_point' : str,
        'user:opsworks:stack' : str,
        'user:opsworks:stack_id' : str,
        'user:opsworks:volume_id' : str,
        'user:role' : str,
        'user:workload-type' : str,
    }

    return pandas.read_csv(fp, dtype=dtype_cols, low_memory=False)

def get_application(row):
    for key in ['aerospike', 'assetrouter', 'bidder', 'bidder3psettings', 'bidderservice', 'clusterstatus', 'datadashboard', 'datamigrator', 'dmpsync', 'druid', 'eb', 'exchange', 'exchangeservice', 'imageanalysis', 'imagecalculator', 'imagerender', 'impression_bus', 'impression_bus_service', 'kafka', 'kafka_v2', 'kafkaconsumer', 'main-zk', 'optimizations', 'prod-zk', 'rsupload', 'storm', 'taskservice']:
        try:
            if type(row['user:opsworks:layer:' + key]) == str and len(row['user:opsworks:layer:' + key]) > 0:
                return key
        except Exception, e:
            print key, e
    return 'None'

if __name__ == '__main__':
    fp = sys.argv[1]

    d = load_file(fp)
    d['app'] = d.apply(get_application, axis=1)

