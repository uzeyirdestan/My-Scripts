#!/bin/bash
domain=$1
for i in $(cat $domain)
do
	result=$(dig @1.1.1.1 $i CNAME +short | grep -iE "aws|github|trafficmanager|azure")
	if [ ! -z $result ]  
	then
		echo "$i ==> $result"
	fi
done

