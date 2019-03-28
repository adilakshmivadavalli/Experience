import MySQLdb

#Upload score
def upload_score(score,num_se,num_me,num_be,total_time,num_sb,num_db,num_normalbullet,num_doublebullet,num_super):
    score = int(score)
    num_se = int(num_se)
    num_me = int(num_me)
    num_be = int(num_be)
    total_time = int(total_time)
    num_sb = int(num_sb)
    num_db = int(num_db)
    num_normalbullet = int(num_normalbullet)
    num_doublebullet = int(num_doublebullet)
    num_super = int(num_super)
    
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "INSERT INTO score_board(score,num_se,num_me,num_be,total_time,num_sb,num_db,num_normalbullet,num_doublebullet,num_super)VALUES('%d','%d','%d','%d','%d','%d','%d','%d','%d','%d')"% \
                                    (score,num_se,num_me,num_be,\
                                     total_time,num_sb,num_db,\
                                     num_normalbullet,num_doublebullet,num_super)
                                    

    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    db.close()

#Get data from database
def get_bestScore():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(score) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_se():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_se) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_me():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_me) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_be():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_be) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestTotal_time():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(total_time) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_sb():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_sb) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_db():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_db) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_normalbullet():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_normalbullet) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_doublebullet():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_doublebullet) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]

def get_bestNum_super():
    db = MySQLdb.connect("localhost","root","123456","aircraft_war" )
    cursor = db.cursor()
    sql = "SELECT MAX(num_super) FROM score_board"
    try:
    #Execute SQL query
        cursor.execute(sql)
        db.commit()
    except:
    # Rollback in case there is any error
        db.rollback()
    data = cursor.fetchone()
    return data[0]
    
