# Start flask server:

```bash
# start app on default port 5000
python app.py

# start app on port 5555
export FLASK_APP=main.py
export FLASK_RUN_PORT=5555
flask run

# Start flask server as standalone container (without redis)
docker build -t dejanualex/pythonredis:1.0 .
docker run -p 5555:5000 dejanualex/pythonredis:1.0
```
# Test app:

```bash
# lint
pylint $(git ls-files '*.py')

# unittest
./test_app.py
```

# Compose flask-app and redis

* Start/stop stack:
```bash
docker-compose -f docker-compose.yaml config
docker-compose -f docker-compose.yaml up -d --build
docker-compose ps

docker-compose down --rmi all --volumes --remove-orphans
```

# Kubernetes flask-app and redis

* What k8s objects do we need for our stack?

```bash
kubectl apply -f k8s_deploy_stack

# dummy create secret
kubectl create secret generic python-hello-app-secret --from-literal=testsecret=dummyvalue
# check the secret value
kubectl get secrets python-hello-app-secret -ojsonpath={.data.testsecret} | base64 -d

# check counter
kubectl expose deploy flask-app --name=flask-svc --type="LoadBalancer" --port=5555 --target-port=5000
```

# Helm chart

```bash
cd helm_chart
helm create pythonhello

helm template flaskhello pythonhello
helm install flaskhello pythonhello 

helm uninstall flaskhello  

kubectl expose deploy flaskhello-pythonhello --name=flask-svc --type="LoadBalancer" --port=5555 --target-port=5000
```

### ToDos

* Explore Dockerfile (explore [hadoling](https://github.com/hadolint/hadolint) linter: `docker run --rm -i hadolint/hadolint < Dockerfile`)
* Build and push the image to [docker registry](https://hub.docker.com/) (explore a scanner like [trivy](https://github.com/aquasecurity/trivy))