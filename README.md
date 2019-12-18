# CS4BD-A3-Kafka

# 1) Complete. See python files above. 
    The `dockerCmds` file gives the docker containers that were used for this setup.

# 2) What is new/different about Kafka Streams? 
    Kafka Streams is an API providing the following features, similar to other stream processing frameworks:
    - Supports fault-tolerant local state, which enables very fast and efficient stateful operations like windowed joins and aggregations.
    - Supports exactly-once processing semantics to guarantee that each record will be processed once and only once even when there is a failure on either Streams clients or Kafka brokers in the middle of processing.
    - Employs one-record-at-a-time processing to achieve millisecond processing latency, and supports event-time based windowing operations with out-of-order arrival of records.
    - Offers necessary stream processing primitives, along with a high-level Streams DSL and a low-level Processor API.

    The difference with Kafka Streams is its seamless integration with Kafka.  The API is build directly on top of the Kafka producers and consumers, providing a simple interface to these lower level APIs.

# 3) Yes
