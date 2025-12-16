# Commands used

- $ docker exec -it hands-on-kafka-kafka-1 kafka-topics   --bootstrap-server localhost:9092   --describe   --topic transactions

# Purpose: Create a Kafka topic.

- docker exec -it hands-on-kafka-kafka-1 kafka-console-producer   --bootstrap-server localhost:9092   --topic transactions
# Purpose: Allows messages to be published as a round-robin strategy within a partition.
- $ docker exec -it kafka kafka-console-consumer   --bootstrap-server localhost:9092   --topic transactions   --from-beginning   --property print.partition=true   --property print.offset=true
# Purpose: Reads messages from a given parition order; removing "--from beginning" leaves only the new messages.

- $  docker exec -it kafka kafka-console-consumer   --bootstrap-server localhost:9092   --topic transactions   --from-beginning   --property print.partition=true   --property print.offset=true

# Purpose: Creates a transaction group to help categorize messages.


# Result example:

Partition:2     Offset:3        {"id":2,"amount":75.0,"type":"refund"}
Partition:2     Offset:4        {"id":3,"amount":300.0,"type":purchase"}
Partition:0     Offset:0        {id:1,"amount":120.5,"type","purchase"}
Partition:0     Offset:1        {id:1,"amount":75.0,"type","refund"}
Partition:0     Offset:2
Partition:0     Offset:3        {"id":1,"amount":120.5,"type","purchase"}
Partition:0     Offset:4        {"id":1,"amount":120.5,"type":"purchase"}
Partition:0     Offset:5        {"id":2,"amount":75.0,"type":"refund"}
Partition:0     Offset:6        {"id":3,"amount":300.0,"type":purchase"}