#CRUD operation on table of ESM Database

import sqlite3 as s
import pandas as pd
con=s.connect("esm.db")

# Query:-1 : Create table employee

ctbl="create table IF NOT EXISTS employee \
      (\
          eid int primary key,\
          ename text,\
          dept text,\
          basic int,\
          branch text)"

cur=con.cursor()
cur.execute(ctbl)
con.commit()

# Query:-2 :Insert 5 Records directly, 5 records using tuple and 5 records using taking input from user


#(i):Insert 5 Records Directly.

ins1="insert into employee values(1,'omi','Account',8000,'Surat'),\
                                  (2,'shiv','HR',5000,'Mumbai'),\
                                  (3,'drishti','IT',9000,'Delhi'),\
                                  (4,'priya','Inventory',15000,'Mumbai'),\
                                  (5,'jasmin','HR',78000,'Bangluru')"
cur.execute(ins1)
con.commit()

#(ii) : Insert 5 Records Using Tuple.

insq="insert into employee values(?,?,?,?,?)"
tup=[(101,'om','Account',5000,'surat'),
     (102,'sai','it',8000,'surat'),
     (103,'ram','HR',9000,'surat'),
     (104,'prachi','Account',17000,'surat'),
     (105,'prakruti','IT',4000,'surat')]
cur.executemany(insq,tup)
con.commit()

#(iii) : Insert 5 Records Using Taking Input From User.
li=[]
for i in range(5):
    no=int(input("\nEnter Id Of Employee :"))
    ename=input("\nEnter Name Of Employee :")
    dept=input("\nEnter Department Of Employee :")
    basic=int(input("\nEnter Basic Salary Of Employee :"))
    branch=input("\nEnter Branch Of Employee :")
    t=(no,ename,dept,basic,branch)
    li.append(t)
cur.executemany(insq,li)
con.commit()


#Query:-3 : Update records who are from "Surat" branch with increment in salary 10%.

upq="update employee\
     set basic=basic+(basic*10/100)\
     where branch='Surat' or branch='surat'"
cur.execute(upq)
con.commit()


#Query:-4 : Print All records.

seq="select * from employee"
cur.execute(seq)
print("\n\n\n OUTPUT OF QUERY NO:-4 : PRINT ALL RECORDS \n")
re1=cur.fetchall()
df1=pd.DataFrame(re1,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'],index=None)
print(df1.to_string(index=False))
con.commit()


#Query:-5 : Print records where dept is "HR" and "IT".

sehi="select * from employee\
    where dept IN('hr','HR','IT','it')"
cur.execute(sehi)
print("\n\n\n OUTPUT OF QUERY NO:-5 : PRINT RECORDS WHERE DEPT IS \"HR\" AND \"IT\" \n")
re2=cur.fetchall()
df2=pd.DataFrame(re2,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'],index=None)
print(df2.to_string(index=False))
con.commit()


#Query:-6 : Print records in sorting order of department.

sortasc="select * from employee\
       order by dept"
cur.execute(sortasc)
print("\n\n\n OUTPUT OF QUERY NO:-6 : PRINT RECORDS IN SORTING ORDER OF DEPARTMENT \n ")
re3=cur.fetchall()
df3=pd.DataFrame(re3,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'],index=None)
print(df3.to_string(index=False))
con.commit()


#Query:-7 : Print records where basic is >6000.

basicq="select * from employee\
      where basic>6000"
cur.execute(basicq)
print("\n\n\n OUTPUT OF QUERY NO:-7 : PRINT RECORDS WHERE BASIC IS >6000 \n")
re4=cur.fetchall()
df4=pd.DataFrame(re4,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'])
print(df4.to_string(index=False))
con.commit()


#Query:-8 : Print records whrere employee name second character is "r".

rchar="select * from employee\
      where ename LIKE '_r%'"
cur.execute(rchar)
print("\n\n\n OUTPUT OF QUERY NO:-8 : PRINT RECORDS WHERE EMPOLYEE NAME SECOND CHARACTER IS 'r' \n")
re5=cur.fetchall()
df5=pd.DataFrame(re5,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'])
print(df5.to_string(index=False))
con.commit()


#Query:-9 : Grouping record of employee who are from "Account" and "Inventory".

groupq="select dept,count(*) from employee\
        group by dept\
        having dept IN('Account','account','Inventory','inventory')"
cur.execute(groupq)
print("\n\n\n OUTPUT OF QUERY NO:-9 : GROUPING RECORD OF EMPLOYEE WHO ARE FROM \"Account \n")
re6=cur.fetchall()
df6=pd.DataFrame(re6,columns=['DEPARTMENT','NUMBER OF EMPLOYEE'])
print(df6.to_string(index=False))
con.commit()


#Query:-10 : Print all records based on branch name in descending order.

sortdes="select * from employee\
         order by branch DESC"
cur.execute(sortdes)
print("\n\n\n OUTPUT OF QUERY NO:-10 : PRINT ALL RECORD BASED ON BRANCH NAME IN DESCENDING ORDER. \n")
re7=cur.fetchall()
df7=pd.DataFrame(re7,columns=['ID','NAME','DEPARTMENT','BASIC','BRANCH'])
print(df7.to_string(index=False))
con.commit()

con.close()




