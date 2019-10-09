# -*-coding: utf-8 -*-
# Created by samwell

import boto3

if __name__ == '__main__':
    client = boto3.client('lambda')
    resp = client.list_functions()
    for funcinfo in resp['Functions']:
        name = funcinfo['FunctionName']
        client.update_function_code(
            FunctionName=name,
            S3Bucket='cloudspider',
            S3Key='py-lambda-package.zip')
        print('Updated ', name)
