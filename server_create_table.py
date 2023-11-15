import psycopg2

DATABASE_URL = 'postgres://roboinstrumentadorpostgresql_user:3CC4JHHevUFA5mUuAwI0SF4JLvmBtS46@dpg-cl60fgcn7k7c73capqn0-a.oregon-postgres.render.com/roboinstrumentadorpostgresql'


def create_tables():

    conn = None
    try:
#
        # connect to the PostgreSQL server
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        # create table one by one
        cur.execute(open("schema.sql", "r").read())

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()



