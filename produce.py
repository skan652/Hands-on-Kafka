#!/usr/bin/env python3
import csv
import json
import subprocess
import os

csv_file = os.path.join(os.path.dirname(__file__), 'transactions.csv')

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        message = {
            "transaction_id": int(row['transaction_id']),
            "user_id": int(row['user_id']),
            "amount": float(row['amount']),
            "timestamp": row['timestamp']
        }
        json_msg = json.dumps(message)
        cmd = ['docker', 'exec', '-i', 'hands-on-kafka-kafka-1', 'kafka-console-producer', 
               '--bootstrap-server', 'localhost:9092', '--topic', 'transactions']
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate(input=json_msg.encode())
        count += 1
        if count % 50 == 0:
            print(f"Produced {count} messages...")

print(f"Successfully produced {count} messages to Kafka!")
