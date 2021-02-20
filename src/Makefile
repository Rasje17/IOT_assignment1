TARGETS = \
	TestHarness.class \

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}

mrproper: clean
	touch d~
	rm    *~


TestHarness.class: TestHarness.java
	javac TestHarness.java

TestHarness: TestHarness.class
	java TestHarness run42 ls -l

