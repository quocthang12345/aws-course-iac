import json
import os

_table = None


def _get_table():
    global _table
    if _table is None:
        import boto3
        _table = boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
    return _table


def next_count(table):
    r = table.update_item(
        Key={"id": "visits"},
        UpdateExpression="ADD hits :one",
        ExpressionAttributeValues={":one": 1},
        ReturnValues="UPDATED_NEW",
    )
    return int(r["Attributes"]["hits"])


def handler(event, context):
    hits = next_count(_get_table())
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"hits": hits, "version": os.environ.get("APP_VERSION", "v1")}),
    }
