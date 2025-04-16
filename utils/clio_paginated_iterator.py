import sqlite3

def get_page(conn, table_name, page_size, cursor=None):
    """
    Retrieves a page of data from a table using cursor-based pagination.

    Args:
        conn: SQLite connection object.
        table_name: Name of the table to query.
        page_size: Number of rows to return per page.
        cursor: The cursor value to start from (optional).

    Returns:
        A tuple containing:
            - A list of rows representing the current page.
            - The cursor for the next page, or None if there are no more pages.
    """
    query = f"SELECT id, name FROM {table_name}"
    if cursor is not None:
        query += f" WHERE id > {cursor}"  # Assuming 'id' is the unique, sequential column
    query += f" ORDER BY id ASC LIMIT {page_size}"

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    next_cursor = None
    if rows:
        next_cursor = rows[-1][0]  # Use the ID of the last row as the next cursor

    return rows, next_cursor

if __name__ == '__main__':
    # Example usage:
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()

    # Create a sample table
    cur.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
    for i in range(25):
        cur.execute("INSERT INTO items (name) VALUES (?)", (f"Item {i+1}",))
    conn.commit()

    page_size = 5
    cursor = None

    while True:
        page, cursor = get_page(conn, "items", page_size, cursor)
        if not page:
            break  # No more data

        print("Page:")
        for row in page:
            print(row)
        print("---")

        if cursor is None:
            break  # Last page reached

    conn.close()