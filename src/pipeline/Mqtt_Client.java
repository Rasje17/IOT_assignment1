import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;
import org.json.*;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;
import java.lang.Math.*;

public class Mqtt_Client implements MqttCallback {
    static String broker = "tcp://localhost:1883";
    static int qos = 2;
    
    MqttClient client;
    Map<String, Double> temps;
    Map<String, Double> rhums;
    
    public Mqtt_Client (String broker, String topic) throws MqttException {
        MemoryPersistence persistence = new MemoryPersistence();
        client = new MqttClient(broker, "java/ahum", persistence);
        MqttConnectOptions connOpts = new MqttConnectOptions();
        connOpts.setCleanSession(true);
        client.setCallback(this);
        client.connect(connOpts);
        client.subscribe(topic, qos);
        
        temps = new HashMap<String, Double>();
        rhums = new HashMap<String, Double>();
    }
    
    public void deliveryComplete(IMqttDeliveryToken token) {}
    public void connectionLost(Throwable cause) {
        System.out.println("Connection lost. Cause: " + cause);
        System.out.println("Did you start up a client with the same ID?");
        System.exit(1);
    }
    
    public void messageArrived (String topic, MqttMessage message) throws MqttException {
        try {
                       
            JSONObject jo = new JSONObject(new String(message.getPayload()));
            int time  = jo.getInt("time");
            double value = jo.getDouble("value");

            System.out.println("IN,"+ topic + "," + time);

        } catch (JSONException e) {
            System.out.println("Received exception in messageArrived: "+e);
        }
    }
    
    public static void main(String[] args) throws MqttException, InterruptedException {
        Mqtt_Client ma = new Mqtt_Client(broker, "func/+/+");
        
        // stay alive
        while (true) {
            Thread.sleep(1000);
        }
    }
}
