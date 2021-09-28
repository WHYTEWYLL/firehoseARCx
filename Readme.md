
# Firehose Streaming app (AWS S3)

This is a full streaming experience, I talked about in the last Readme
this provides a full scalabily cost-efficient solution without needing to download the file. The thing is that this way because of the buffer 
AWS provides. 

Will create an object per 5 min with the calls we made in that
time. This is incredible because that we will have a different object per
day. 


And we can easily concatenate everything in a moment, also we could create a lambda function so all the ETL / Dashboard is on AWS if we want to
create if we want a database base on all the objects. So we could query whatever,
create dashboard so easily batch or stream. Either way, I would recommend these solutions, if we want to use AWS.
