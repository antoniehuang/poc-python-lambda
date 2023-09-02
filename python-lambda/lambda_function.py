import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps("Changing the code to see if github action works"),
        'event': event
    }