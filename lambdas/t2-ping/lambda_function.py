import greengrasssdk
import random
import logging

def run():
    num = random.randint(10,99)                    
    client = greengrasssdk.client('iot-data')
    msg = str(num)
    response = client.publish(
        topic = 't2/test',
        qos = 0,
        payload = msg.encode()
    )
    logging.info("t2-ping:publish[t2/test] " + msg)

def function_handler(event, context):
    logging.info('t2-ping:function_handler:start')
    return

logging.info("t2-ping:start")
run()
