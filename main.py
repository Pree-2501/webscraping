import json
import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
  logger.info("Event: "+json.dumps(event))

  for record in event.get("Records",[]):
    s3_object_key=record['s3']['object']['key']
    logger.info(f'File Uploaded: {s3_object_key}')
    logger.info(f"An Image has been Added Successfully")
  return{
    'statusCode': 200,
    'body': json.dumps('Success')
  }