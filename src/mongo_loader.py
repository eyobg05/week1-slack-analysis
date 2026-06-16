import json
import os
from pymongo import MongoClient


DATA_PATH = "data"
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "slack_analysis"


def load_slack_json_to_mongo(data_path=DATA_PATH):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]

    messages_collection = db["messages"]

    inserted_count = 0

    for channel_name in sorted(os.listdir(data_path)):
        channel_path = os.path.join(data_path, channel_name)

        if not os.path.isdir(channel_path):
            continue

        for filename in sorted(os.listdir(channel_path)):
            if not filename.endswith(".json"):
                continue

            file_path = os.path.join(channel_path, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                messages = json.load(f)

            for message in messages:
                message["channel"] = channel_name
                message["date"] = filename.replace(".json", "")

            if messages:
                messages_collection.insert_many(messages)
                inserted_count += len(messages)

        print(f"Loaded channel: {channel_name}")

    print(f"Inserted {inserted_count} messages into MongoDB.")


if __name__ == "__main__":
    load_slack_json_to_mongo()