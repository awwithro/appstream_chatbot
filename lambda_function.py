#!/usr/bin/env python3
import json
import boto3

APPSTREAM_COMMAND_ID = 1


def lambda_handler(event, context):
    request = json.loads(event["body"])
    client = boto3.client('appstream')
    if request['message']['annotations'][0]['type'] == 'SLASH_COMMAND':
        if request['message']['slashCommand']['commandId'] == APPSTREAM_COMMAND_ID:
            return response(json.dumps(appstream(client, request['message']['argumentText'])))
        else:
            return response(json.dumps({'text': 'Unrecognized Slash Command ID'}))
    else:
        return response(json.dumps({'text': "Unknown command or message"}))


# Handles appstream slash commands
def appstream(client, args):
    if args == " list":
        response = client.describe_fleets()
        names = [fleet["Name"] for fleet in response['Fleets']]
        return dict(text="Fleets:\n"+"\n".join(names))
    else:
        return "Unrecognized command."


def response(msg, code=200):
    return {
        'statusCode': code,
        'body': msg
    }