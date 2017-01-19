#!/usr/bin/python



from IPy import IP
import sys
import os
import subprocess
import MySQLdb


iprange=sys.argv[1]

ip=IP(iprange)
record=[]
for i in ip:
    cmd='ping %s -c 2 >/dev/null' %i
#    print cmd
    result=os.system(cmd)
#    print result
#    if result==0:
#        print '%s is avaliable' %i
#    else:
#        print '%s is not avaliable' %i
#        sys.exit()


    if result==0:
        cmd1="snmpwalk -v 2c -c public %s sysName.0|awk -F':' {'print $4'}" %i
        hostname=subprocess.Popen(cmd1,stdout=subprocess.PIPE,shell=True).communicate()

        db = MySQLdb.connect('localhost','root','','cmdb')
        cursor=db.cursor()
#        sql="insert into Host(hostip,hostname) values('%s','%s')" %(i,hostname)
        try:
            cursor.execute('insert into Host(hostip,hostname) values("%s","%s")' %(i,hostname))
            db.commit()
        except:
            db.rollback()
        db.close()
    else:
        print "%s can't be reach" %i



