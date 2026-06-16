from src.loader import SlackDataLoader


def test_get_channel_messages_expected_columns():
    loader = SlackDataLoader("data")

    df = loader.get_channel_messages("all-broadcast")

    expected_columns = {
        "channel",
        "date",
        "type",
        "user",
        "text",
        "ts",
        "reply_count",
        "reply_users_count",
        "reactions",
    }

    assert expected_columns.issubset(set(df.columns))