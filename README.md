## Project Files Overview

src/loader.py

Contains the `SlackDataLoader` class used to load Slack export data from JSON files. It reads channel folders, extracts message data, and returns structured Pandas DataFrames for analysis. This file supports the EDA and feature-engineering work completed in Tasks 1 and 2.


mongo_loader.py

Loads the raw Slack JSON data into a local MongoDB database. The current implementation stores Slack messages in a `slack_analysis.messages` collection while preserving the original JSON structure. This acts as a raw data ingestion layer for Task 3.


create_postgres_tables.py

Creates the PostgreSQL feature-store schema inside the `slack_features` database. The script defines tables for user features, channel features, message features, daily sentiment features, and topic features.


tests/test_loader.py

Contains a PyTest unit test for validating that `SlackDataLoader` returns a DataFrame with the expected columns. This supports Task 2 requirements around unit testing and software reliability.


notebooks/eda-steps.ipynb

Main analysis notebook containing work from Tasks 1 and 2. It includes Slack data loading, exploratory data analysis, user/channel metrics, response-time analysis, topic modelling, sentiment analysis, message classification, and MLFlow tracking.
