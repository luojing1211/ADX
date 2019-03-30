adx connect localhost:84001 --one-session
adx schema
adx query -par sn --cond gt 5 --cond lt 10
adx query -par mjd --cond gt 58255 
adx query "$or : {$sn $lt 5}, {$mjd $gt 58255}"
# 58255 = 05/17/2018
adx query -par sn --cond gt 3 --exec <analysis> {} \;
# this is like find exec 
adx refresh
# this re-crawls and updates the db
adx disconnect
### oneline
adx --connect localhost:84005 query -par mjd --cond gt 57852 --exec <analysis> {} \;

adx /data --db vlbi --port 84001 --daemon
