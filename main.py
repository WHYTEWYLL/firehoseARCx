from dotenv import load_dotenv
from datetime import datetime
import boto3
from  etherScan import getEth
import os

def main():

    firehose = boto3.client('firehose',
                region_name='us-east-1',
                aws_access_key_id=AWS_KEY_ID,
                aws_secret_access_key=AWS_SECRET)  
    
    try:

        response = firehose.create_delivery_stream(
            DeliveryStreamName='ARCxDev',
            DeliveryStreamType='DirectPut',
            S3DestinationConfiguration={
                'RoleARN': ROLE,
                'BucketARN': 'arn:aws:s3:::ether-price-gid-requests-' + VERTICAL,
                    }
            )
    except Exception as e:
        print('The firehose already exists.')
    
    eth_res = getEth(SCAN_KEY)
    
    data = " ".join( str(x) for x in [eth_res])
    
    firehose.put_record(
    DeliveryStreamName = 'ARCxDev',
    Record = {
        'Data':data + "\n"
    })

if __name__ == "__main__":
    
    startTime = datetime.now()

    load_dotenv()

    try:
        AWS_KEY_ID = os.getenv('AWS_KEY_ID')
        AWS_SECRET = os.getenv('AWS_SECRET')
        SCAN_KEY = os.getenv('apikey') # Etherscan APIkey
        VERTICAL = os.getenv('vertical') # Vertical could be { dev / prod / test}
        ROLE = os.getenv('Role')
    except Exception as e:
        error(f"Error setting Environment Variables: {e}")
        exit()

    main()
    print (datetime.now() - startTime )


