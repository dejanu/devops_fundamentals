# Start flask server:
```bash
# start app on default port 5000
python app.py

# start app on port 5555
export FLASK_APP=main.py
export FLASK_RUN_PORT=5555
flask run
```

Start flask server as standalone container (without redis), image available [here](https://hub.docker.com/repository/docker/dejanualex/pythonhello/tags)

```bash
docker run -p 5555:5000 dejanualex/pythonhello:1.0
```
# Test app:

```bash
# lint
pylint $(git ls-files '*.py')

# unittest
./test_app.py
```
# Build flask app:

```bash
docker build -t dejanualex/pythonhello:1.0 .
```

# Compose flask-app and redis

* Start:
```bash
docker-compose -f docker-compose.yaml up -d --build
```
* Stop:
```bash
docker-compose down --rmi all --volumes --remove-orphans
```

# Kubernetes flask-app and redis

```bash
kubectl apply -f k8s_deploy_stack
kubectl expose deploy flask-app --name=flask-svc --type="LoadBalancer" --port=5555 --target-port=5000
```

# Helm chart

* [here](https://github.com/dejanu/course_materials/blob/main/python_hello_app/helm_chart/readme.md)

### ToDos

* Explore Dockerfile (explore [hadoling](https://github.com/hadolint/hadolint) linter: `docker run --rm -i hadolint/hadolint < Dockerfile`)
* Build and push the image to [docker registry](https://hub.docker.com/) (explore a scanner like [trivy](https://github.com/aquasecurity/trivy))