import sqlite3

def print_downloads(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    # c.execute("SELECT tbl_name from sqlite_master WHERE type='table'")
    c.execute("SELECT host,name,value from moz_cookies")
    # c.execute("SELECT name, source, datetime(endTime/1000000,'unixepoch') " +
    #           "FROM moz_downloads;")
    for row in c:
        try:
            print row
        except:
            pass


print_downloads("/home/merlyn/.mozilla/firefox/8ebeq61s.default/cookies.sqlite")

