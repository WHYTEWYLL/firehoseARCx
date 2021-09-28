
# Firehose Streaming app (AWS S3)

This is a full streaming experience, I talked about in the last Readme
this provide fullscalabily cost-efficient solution without needing to 
download the file. The thing is that this way because of the buffer 
AWS provides. 

Will create a object per 5 min with the calls we made in that
time. What is increible because that we will have a diferent object per
day. 


And we can easly concante everything in a moment, also we could 
create a lambda fuction so all the ETL / Dashboard is on AWS if we want to
as to create if we want a databe base on all the objects. So we could query whatever,
create dashboard so easly batchly or stream. Either way, I would recomend to
