TARGETS = \
	Logger.class \
	OutputLogger.class \
	ProcessLogger.class \
	TestHarness.class \

CP = -classpath ".:javasysmon-0.3.5.1.jar"

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~
	rm    *~

deps:
	echo Download from https://jar-download.com/artifact-search/javasysmon and extract jar file here. Code expects the result to be named "javasysmon-0.3.5.1.jar".


Logger.class: Logger.java
	javac Logger.java

OutputLogger.class: OutputLogger.java
	javac OutputLogger.java

ProcessLogger.class: ProcessLogger.java
	javac ${CP} ProcessLogger.java

TestHarness.class: TestHarness.java
	javac ${CP} TestHarness.java

TestHarness: ${TARGETS}
	java ${CP} TestHarness run42 make -C pipeline/ MqttSignalGenerator

TestHarness.generator: ${TARGETS}
	java ${CP} TestHarness run1_gen make -C pipeline/ MqttSignalGenerator

TestHarness.mavg: ${TARGETS}
	java ${CP} TestHarness run1_mavg make -C pipeline/ MqttMovingAverage

TestHarness.func: ${TARGETS}
	java ${CP} TestHarness run1_func make -C pipeline/ MqttFunc

TestHarness.client: ${TARGETS}
	java ${CP} TestHarness run1_client make -C pipeline/ Mqtt_Client

TestHarness.mosquito_sub: ${TARGETS}
	java ${CP} TestHarness run1_client mosquitto_sub -v -t 'ahum/+/+'

