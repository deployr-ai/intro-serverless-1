import json
import pandas as pd
import tweepy
import os
import datetime as dt
import boto3

# definiciones de AWS/S3
BUCKET_NAME = 'NOMBRE_DE_TU_BUCKET' # nombre del bucket, en mi caso era 'serverless-tracker-datalake' 
LOCAL_LAMBDA_FOLDER = '/tmp/'
FOLDER_STRUCTURE = 'raw/ethereum/'

def lambda_handler(event, context):
    TIMESTAMP = dt.datetime.today().strftime("%Y-%m-%d_%H:%M")
    LOCAL_FILENAME = f'{TIMESTAMP}.csv' # nombre del archivo que levantamos ahora
    LAMBDA_FILEPATH = f'{LOCAL_LAMBDA_FOLDER}/{LOCAL_FILENAME}'
    S3_FILEPATH = f'{FOLDER_STRUCTURE}{LOCAL_FILENAME}'
    
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    TWEET_FIELDS = ['id', 'text', 'author_id', 'created_at', 'possibly_sensitive', 'referenced_tweets']
    QUERY = 'ethereum'
    
    client = tweepy.Client(bearer_token=bearer_token)
    response = client.search_recent_tweets(query=query,
                                           max_results=100,
                                           tweet_fields=tweet_fields)

    response_df = pd.DataFrame(response.data)

    response_df.to_csv(LAMBDA_FILEPATH, index=False, encoding='utf-8')
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)

    bucket.upload_file(LAMBDA_FILEPATH, S3_FILEPATH)
    
    print(f'Son las {TIMESTAMP}')
    print(f'Subido el archivo a la carpeta {S3_FILEPATH}')
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Subido a la carpeta {S3_FILEPATH}')
    }
    