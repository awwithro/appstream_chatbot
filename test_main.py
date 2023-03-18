import boto3
from botocore.stub import Stubber
from .lambda_function import appstream


def test_appstream():
    client = boto3.client('appstream', region_name='us-west-2')
    stubber = Stubber(client)
    expected_params = {}
    describe_fleets_response = {
        "Fleets": [
            {
                "Arn": "string",
                "ComputeCapacityStatus": {
                    "Available": 5,
                    "Desired": 5,
                    "InUse": 5,
                    "Running": 5
                },
                "Description": "A Fleet",
                "DisplayName": "One",
                "FleetErrors": [
                    {
                    "ErrorCode": "string",
                    "ErrorMessage": "string"
                    }
                ],
                "InstanceType": "string",
                "Name": "One",
                "State": "RUNNING",
            },
            {
                "Arn": "string",
                "ComputeCapacityStatus": {
                    "Available": 5,
                    "Desired": 5,
                    "InUse": 5,
                    "Running": 5
                },
                "Description": "A Fleet",
                "DisplayName": "Two",
                "FleetErrors": [
                    {
                        "ErrorCode": "string",
                        "ErrorMessage": "string"
                    }
                ],
                "InstanceType": "string",
                "Name": "Two",
                "State": "RUNNING",
            },
            {
                "Arn": "string",
                "ComputeCapacityStatus": {
                    "Available": 5,
                    "Desired": 5,
                    "InUse": 5,
                    "Running": 5
                },
                "Description": "A Fleet",
                "DisplayName": "Three",
                "FleetErrors": [
                    {
                        "ErrorCode": "string",
                        "ErrorMessage": "string"
                    }
                ],
                "InstanceType": "string",
                "Name": "Three",
                "State": "RUNNING",
            }
        ],
        "NextToken": "string"
        }
    stubber.add_response('describe_fleets', describe_fleets_response, expected_params)
    stubber.activate()
    assert appstream(client, "list") == {'text': {'Fleets:\nOne\nTwo\nThree'}}
