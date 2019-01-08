# @Author: George Onoufriou <georgeraven>
# @Date:   2019-01-08
# @Filename: botoTest.py
# @Last modified by:   georgeraven
# @Last modified time: 2019-01-08
# @License: Please see LICENSE in project root.
# @Copyright: George Onoufriou

import os
import sys

import boto3

tableName = "keys"
primaryKeyName = "keyId"
sortKeyName = "keyType"
readUnitsNum = 1
writeUnitsNum = 1
toCreateDb = False

dynamodb = boto3.resource('dynamodb')

if(toCreateDb == True):
    # Get the service resource.

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName=tableName,
        KeySchema=[
            {
                'AttributeName': primaryKeyName,
                'KeyType': 'HASH'
            },
            {
                'AttributeName': sortKeyName,
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': primaryKeyName,
                'AttributeType': 'S'
            },
            {
                'AttributeName': sortKeyName,
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': readUnitsNum,
            'WriteCapacityUnits': writeUnitsNum
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=tableName)

    # Print out some data about the table.
    print(table.item_count)

table = dynamodb.Table(tableName)
print(table.creation_date_time)

table.put_item(
    Item={
        primaryKeyName: "pkTest",
        sortKeyName: "skTest"
    }
)
