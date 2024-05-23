"""Read History.db and return all tables as csv files in output folder"""
import pandas
import sqlite3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


def create_history_visit_items_tbl():
    """Join history_visits and history_items tables for more readable output.
    Also convert visit_time from Unix to human-readable format (EST)"""
    conn = sqlite3.connect('History.db')
    query = """
    SELECT
        datetime(v.visit_time + 978307200, 'unixepoch', 'localtime') as date, 
        v.*,i.*
    from history_items i 
    left join history_visits v 
    on i.id = v.history_item;
    """
    df = pandas.read_sql_query(query, conn)
    df.to_csv("output/csv/history_visit_items.csv", index=False)
    return


def dump_raw_files():
    """Dump all tables in db to csv."""
    conn = sqlite3.connect('History.db')
    # get all the tables in history DB
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    # print out the tables
    tables = conn.execute(query).fetchall()
    for table in tables:
        query = "SELECT * FROM " + table[0] + ";"
        # save the table to a pandas DataFrame
        df = pandas.read_sql_query(query, conn)
        # save to output/csv as csv
        df.to_csv(f"output/csv/{table[0]}.csv", index=False)
        logger.debug(f"Saved {table[0]} as csv file.")
    logger.info("all done")


def main():
    create_history_visit_items_tbl()
    dump_raw_files()


if __name__ == "__main__":
    main()
