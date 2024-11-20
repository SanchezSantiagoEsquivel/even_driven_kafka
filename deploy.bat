kubectl apply -f zookeeper.yaml
kubectl apply -f kafka-broker.yaml
kubectl apply -f test-consumer/consumer_deployment.yaml
kubectl apply -f santiago-greetings/santiago_greetings_deployment.yaml
kubectl apply -f luis-greetings/luis_greetings_deployment.yaml
kubectl apply -f eyder-fruits/eyder_greetings_deployment.yaml
kubectl apply -f lenin-mensaje/lenin_greetings_deployment.yaml
kubectl apply -f juleipssy-greetings/juleipssy_greetings_deployment.yaml
echo "All Deployed!"