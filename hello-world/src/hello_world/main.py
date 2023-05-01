"""Hello world lambda"""
import json


def main(event, context):
    """Main http lambda"""
    print(f"Event: {event}")
    print(f"Context: {context}")
    message = "Hello, World!"

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
