kubectl apply -f zookeeper.yaml
kubectl apply -f kafka-broker.yaml
kubectl apply -f test-consumer/consumer_deployment.yaml
kubectl apply -f santiago-greetings/santiago_greetings_deployment.yaml
echo "All Deployed!"