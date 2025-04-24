* Create a chart for app

A Chart is a Helm package
A Release is an instance of a chart running in a Kubernetes cluster

* Create a chart for app
```bash
helm create <chart-name>
helm show values . # display contents of values.yaml
helm push [chart] [remote] [flags]
helm install flask-app .  # because flask deployment name is linked to {{ .Release.Name }}
helm list
helm uninstall flask-app 
```
* Verify resources
```bash
kubectl get all -l app.kubernetes.io/managed-by=Helm
```