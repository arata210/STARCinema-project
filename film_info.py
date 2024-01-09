from connect_dbs import MySQLConn


def find_film():
    film_info = MySQLConn()
    query = "SELECT * FROM film"
    result = film_info.execute_query(query)
    film_info.close_conn()
    return result


print(find_film()[2])
