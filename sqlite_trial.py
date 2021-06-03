# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 11:47:04 2018

@author: z003zafb
"""

import sqlite3
from passlib.hash import pbkdf2_sha256

conn=sqlite3.connect('username.db')

c = conn.cursor()

# Create table

c.execute('''CREATE TABLE INFORMATION
       (
       NAME           TEXT    NOT NULL,
       PASSWORD       TEXT     NOT NULL);''')

# Insert a row of data
hash=pbkdf2_sha256.hash("23333")

#c.execute("INSERT INTO INFORMATION (NAME,PASSWORD) \
#      VALUES ('+77',pbkdf2_sha256.hash("23333"))");
c.execute("INSERT INTO INFORMATION (NAME,PASSWORD) VALUES(?,?)", ('+77',hash))
          
          
hash=pbkdf2_sha256.hash("1155665") 
c.execute("INSERT INTO INFORMATION (NAME,PASSWORD) VALUES(?,?)", ('+jiaqi',hash))                   

hash=pbkdf2_sha256.hash("666666") 
c.execute("INSERT INTO INFORMATION (NAME,PASSWORD) VALUES(?,?)", ('harry potter',hash))  
          
          
hash=pbkdf2_sha256.hash("13579") 
c.execute("INSERT INTO INFORMATION (NAME,PASSWORD) VALUES(?,?)", ('changsu mei',hash))  
# Save (commit) the changes
conn.commit()
conn.close()