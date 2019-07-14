

import os
ip="10.11.1."
for i in range(1,255):
	full_ip= ip + str(i)
        command="ping -c 1 "+full_ip
        os.system(command)

