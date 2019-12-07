import paho.mqtt.client as mqtt
import time
#define various MQTT callback functions-we'll only be using some of these
#but the others are defined to help with debugging should you need them
def on_connect(client,userdata,flags,rc):
    print("Connected! rc: ",rc)#rc return code
def on_message(client,userdata,message):
    if(str(message.topic)!=pubtop):
       print(str(message.topic),str(message.payload.decode("utf-8")))
def on_subscribe(client,userdata,mid,granted_qos):
       print("Subscribed:",str(mid),str(granted_qos))
def on_unsubscribe(client,userdatam,mid):
       print("Unsubscribed:",str(mid))
def on_publish(client,userdata,mid):#mid to track pusb req
       print("Publish:",client)
def on_log(client,userdata,level,buf):
       print("log:",buf)
def on_disconnect(client,userdata,rc):
        if rc!=0 :
            print("Unexpected disconnection.")
#set the address of your broker and your port.For a local broker,use the IP
#address.Otherwise,use the web address.
broker_address="iot.eclipse.org"
#broker_address=<insert your IP address here>
port=1883
#port=8883 #port for TLS/SSL
#create the MQTT client and set the callback functions you want to use
client=mqtt.Client()
client.on_subscribe=on_subscribe
client.on_unsubscribe=on_unsubscribe
client.on_connect=on_connect
client.on_message=on_message
time.sleep(1)#sleep for a beat to ensure things occur in order
#input username,password,and pub/sub topics in the terminal
user=input("Username:")
pw=input("Password:")
pubtop=input("Publish topic:")
subtop=input("Subscribe topic:")
#set user/pass,connect to the broker,start the loop,and subscribe
#-it is important to d0 this in order! Subscribing before connecting won't work
client.username_pw_set(user,pw)
client.connect(broker_address,port)
client.loop_start()
client.subscribe(subtop)
#chat loop
while True:
       chat=input()
       if chat=='QUIT' :
           break
       elif chat=='SUBSCRIBE' :
           new_substop=input('Subscribe to topic:')
           client.subscribe(new_subtop)
       elif chat=='UNSUBSCRIBE' :
            client.unsubscribe(unsubtop)
       elif chat=='PUBLISH' :
            pubtop=input('Publish to new topic:')
       else:
           client.publish(pubtop,chat)
#disconnect and stop the loop!
client.disconnect()
client.loop_stop()
