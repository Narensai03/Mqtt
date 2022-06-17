import paho.mqtt.client as mqtt
import time
from datetime import datetime
import datetime
from psycopg2.extras import RealDictCursor
import models
import psycopg2
from database import engine


def on_message(client, userdata, message):
    test = str(message.payload.hex())
    print(test)
    # EPC = test[8:-30]
    EPC1 = test[10:-36]
    # data = EPC
    data1 = EPC1
    create_at = datetime.datetime.now()
    # print("Message received : ", EPC + " on ", message.topic, "Date And Time", create_at)
    print("Message received : ", EPC1 + " on ", message.topic, "Date And Time", create_at)
    # insert = '''INSERT INTO rfid(serialno) VALUES({})'''.format(data)
    # cursor.execute(insert)
    # conn.commit()


# while True:
#
#     try:
#         conn = psycopg2.connect(host='localhost', database='postgres', user='postgres',
#                                 password='Nissi123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfully")
#         break
#     except Exception as error:
#         print("connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)
#
# models.Base.metadata.create_all(bind=engine)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
        global connected
        connected = True
        print("Connected")
        print("..........")
    else:
        print("Unable To Connect")


connected = False
message_received = False
# broker_address = "15.207.254.109"
# broker_address = "192.168.1.53"
broker_address = "157.175.194.214"
print("creating new instance")
client = mqtt.Client('Test1')

client.on_message = on_message
client.on_connect = on_connect

client.username_pw_set(username="nissi", password="nissi")

print("connecting to broker")
client.connect(broker_address, port=1883)

client.loop_start()

# print("Subscribing to topic", "OG Exploration")
# client.subscribe("OG Exploration")

# print("Subscribing to topic", "OG Production")
# client.subscribe("OG Production")
#
# print("Subscribing to topic", "OG Storage")
# client.subscribe("OG Storage")

# print("Subscribing to topic", "Checkout")
# client.subscribe("Checkout")
#
# print("Subscribing to topic", "Reader/reader1")
# client.subscribe("Reader/reader1")

print("Subscribing to topic", "CheckIn")
client.subscribe("Checkin")

# print("Subscribing to topic", "CheckInElectric")
# client.subscribe("CheckInElectric")

while connected != True or message_received != True:
    time.sleep(0.2)

client.loop_forever()
