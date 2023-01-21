# Working With Kubernetes
For this session, you'll have to use docker hub to upload your image.
```bash
# build
docker build -t kube_example .
# Run minikub
minikube start
minikube status
# To see minikube dashboard
minikube dashboard
# push image
docker push d0lby360/kube_example
# create kubernetes object name kube_app and with our docker image
kubectl create deployment kube-app --image=d0lby360/kube_example
# list all deployments
kubectl get deployments
# expose port 8080 for deployment
kubectl expose deployment kube-app --type=LoadBalancer --port=8080
# see all services
kubectl get services
# get kube-app URL
minikube service kube-app
# Get status on all running pods (ready/restarts/...)
kubectl get pods
# run 3 replicas
kubectl scale deployment/kube-app --replicas=3
# shutdown all replicas 
kubectl --namespace default scale deployment kube-app --replicas 0
# delete deplyment
kubectl delete deployments kube-app
```

How to update kubernetes deployment
```bash
# Update docker image first
docker build -t d0lby360/kube_example:1 .
# Push 
docker push d0lby360/kube_example:1
# To update deplotment (in minikube dashboard under pods/containers)
kubectl set image deployment/kube-app kube-example-7hv6h=d0lby360/kube_example:1
```
