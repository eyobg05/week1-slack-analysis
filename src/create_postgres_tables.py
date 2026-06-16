from sqlalchemy import create_engine, text

DB_USER = "postgres"
DB_PASSWORD = "Skibidi789!"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "slack_features"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

create_tables_sql = """
CREATE TABLE IF NOT EXISTS users_features (
    user_id TEXT PRIMARY KEY,
    message_count INTEGER,
    reply_count INTEGER,
    mention_count INTEGER,
    reaction_count INTEGER
);

CREATE TABLE IF NOT EXISTS channel_features (
    channel_name TEXT PRIMARY KEY,
    message_count INTEGER,
    reply_count INTEGER,
    reaction_count INTEGER,
    activity_score INTEGER
);

CREATE TABLE IF NOT EXISTS message_features (
    message_id TEXT PRIMARY KEY,
    channel_name TEXT,
    user_id TEXT,
    timestamp TIMESTAMP,
    text TEXT,
    reply_count INTEGER,
    mention_count INTEGER,
    reaction_count INTEGER,
    message_class TEXT,
    sentiment_score FLOAT
);

CREATE TABLE IF NOT EXISTS daily_sentiment_features (
    date DATE PRIMARY KEY,
    days_since_start INTEGER,
    sentiment_score FLOAT
);

CREATE TABLE IF NOT EXISTS topic_features (
    id SERIAL PRIMARY KEY,
    channel_name TEXT,
    topic_id INTEGER,
    topic_keywords TEXT
);
"""

with engine.connect() as conn:
    conn.execute(text(create_tables_sql))
    conn.commit()

print("PostgreSQL feature store tables created successfully.")