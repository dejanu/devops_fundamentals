.DEFAULT_GOAL := documentation

documentation:
	@echo "docker_up"
	@echo "docker_down"
	@echo "k8s_service"
	@echo "helm_install"
	@echo "repo"

docker_up:
	@printf 'docker-compose -f docker-compose.yaml up -d --build \n'

docker_down:
	@printf 'docker-compose down --rmi all --volumes --remove-orphans \n'

k8s_service:
	@printf 'kubectl expose deployment flask-app --name flask --type="LoadBalancer" --port=5555 --target-port=5000 \n'

helm_install:
	@printf 'helm install flask-app helm_chart/demochart/ \n'

repo:
	@printf 'https://github.com/dejanu/cautious-idp.git \n'
