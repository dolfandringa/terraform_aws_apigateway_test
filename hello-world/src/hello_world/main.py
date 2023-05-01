"""Hello world lambda"""
import json


def main(event, context):
    """Main http lambda"""
    print(f"Event: {event}")
    print(f"Context: {context}")
    name = "World"
    if (
        "queryStringParameters" in event
        and event["queryStringParameters"] is not None
        and "Name" in event["queryStringParameters"]
    ):
        name = event["queryStringParameters"]["Name"]
    message = f"Hello, {name}!"

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(
            {
                "message": message,
            }
        ),
    }
