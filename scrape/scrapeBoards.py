import requests
import sqlite3

# Note: If - Modified - Since: < day - name >, < day > < month > < year > < hour >: < minute >: < second > GMT


keys = test.keys

base_endpoint = 'https://a.4cdn.org'

boards_request = 'boards.json'

threads_request = 'threads.json'

"""

Boards Table Structure
| board | title | per_page | pages | last_modified | current thread # list


"""


def get_boards():
    """ Get board statistics API request in JSON format and input to database
    ensures each board is in board table and has separate table for thread information
    todo: update list of current threads using get_threads
    todo: input into sqlite3 database

    Boards Table Structure
    | board | title | per_page | pages

    Threads Table Structure
    | thread no | closed | last_modified | timestamp | sub | com | replies | archived
    """

    # request 4chan board information
    get_board_info = "{}/{}".format(base_endpoint, boards_request)
    boards = requests.get(get_board_info, params=keys).json()

    # set up database connection
    conn = sqlite3.connect('4ChanWords.db')
    c = conn.cursor()

    # create boards table and thread table for each board
    create_table = 'CREATE TABLE IF NOT EXISTS '
    board_columns = '''  (board text, title text, per_page integer, pages integer ) '''

    statement = create_table + 'boards' + board_columns
    c.execute(statement)

    thread_columns = ''' ( thread_no integer, 
                            closed integer, 
                            timestamp integer, 
                            last_modified integer,
                            sub text,
                            com text,
                            replies integer,
                            archived integer ) '''

    board_list = []
    # create thread table for each board
    for x in boards['boards']:
        if x['board'][0].isnumeric():
            x['board'] = 'chan_' + x['board']
        statement = create_table + x['board'] + thread_columns
        c.execute(statement)
        board_list.append((x['board'], x['title'], x['per_page'], x['pages']))

    # insert each board into boards table
    c.executemany('REPLACE INTO boards VALUES(?,?,?,?)', board_list)
    conn.commit()
    conn.close()


def get_thread_list(boardname):
    """ Get thread information from first 10 pages of "boardname" JSON format
    todo: return list of current thread #s to keep track of
    conn = sqlite3.connect('4ChanWords.db')

    get_thread_list = "{}/{}/{}".format(base_endpoint, boardname, threads_request)
    thread_list = requests.get(get_thread_list, params=keys).json()
    """
    thread_list = test.sample_thread_list


def get_full_thread(boardname, thread_no):
    """ Get a post and all of its replies
    todo: input into sqlite3 database

    conn = sqlite3.connect('4ChanWords.db')

    get_thread = "{}/{}/thread/{}".format(base_endpoint, boardname, thread_no)
    threads = requests.get(get_thread, params=keys).json()
    """
    threads = test.sample_thread


sql = "DELETE FROM myTable WHERE Save_Date <= date('now','-1 day')"

get_boards()

