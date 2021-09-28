import os
import boto3
from etherScan import getEth
from datetime import datetime
from dotenv import load_dotenv

def main():

    firehose = boto3.client('firehose',
                region_name = 'us-east-1',
                aws_access_key_id = AWS_KEY_ID,
                aws_secret_access_key = AWS_SECRET)  
    
    try:

        response = firehose.create_delivery_stream(
            DeliveryStreamName= DELIVERY_NAME,
            DeliveryStreamType='DirectPut',
            S3DestinationConfiguration={
                'RoleARN': ROLE,
                'BucketARN': BUCKET_ARN + VERTICAL,
                    }
            )
    except Exception as e:
        print('The firehose already exists.')
    
    data = getEth(SCAN_KEY)
    
    
    firehose.put_record(
    DeliveryStreamName = 'ARCxDev',
    Record = {
        'Data':data + "\n"
    })

if __name__ == "__main__":
    
    startTime = datetime.now()

    load_dotenv()

    try:

        # AWS Settings
        AWS_KEY_ID = os.getenv('AWS_KEY_ID')
        AWS_SECRET = os.getenv('AWS_SECRET')
        AWS_SERVER = os.getenv('AWS_SERVER')

        # AWS S3   
        BUCKET_ARN = os.getenv('BucketARN')

        # AWS Firehose Settings 
        DELIVERY_NAME = os.getenv('DeliveryStreamName')
        REGION_NAME = os.getenv('REGION_NAME')
        ROLE = os.getenv('Role')
        # Etherscan Settings
        SCAN_KEY = os.getenv('apikey') # Etherscan APIkey

        # Vertical Deployment
        VERTICAL = os.getenv('vertical') # Vertical could be { dev / prod / test}


    except Exception as e:
        error(f"Error setting Environment Variables: {e}")
        exit()

    main()
    print (datetime.now() - startTime )


