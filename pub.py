
import sys
sys.path.append('contrib/mosquitto')
sys.path.append('.')

import mosquitto

from config import Config

mqttc = mosquitto.Mosquitto()

try:
    mqttc.connect(config.MQTT_SERVER, 1883, 60)
    mqttc.publish("temperature/12/sensor/45", "{ 'test': '5434' }", 1 )

except:
    print "no connection"
