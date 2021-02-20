TARGETS = \
	TestHarness.class \

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~
	rm    *~


Logger.class: Logger.java
	javac Logger.java

OutputLogger.class: OutputLogger.java
	javac OutputLogger.java

TestHarness.class: TestHarness.java
	javac TestHarness.java

TestHarness: *.class
	java TestHarness run42 ls -l

