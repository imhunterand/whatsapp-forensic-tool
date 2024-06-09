import sqlite3

def extract_deleted_messages(cursor):
    query = """
    SELECT chat_list.key_remote_jid, messages.key_from_me, messages.data, messages.timestamp
    FROM messages
    LEFT JOIN chat_list ON messages.key_remote_jid = chat_list.key_remote_jid
    WHERE messages.deleted = 1;
    """
    cursor.execute(query)
    return cursor.fetchall()
