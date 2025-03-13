
* Images
https://hub.docker.com/r/jenkins/jenkins
https://hub.docker.com/r/jenkins/ssh-agent/tags?name=jdk17


* Generate a keypair ssh-keygen: `export pubkey=$(cat jenkinsagent.pub)`
* Create `.env` file: 
```bash
cat<<EOF>>.env
JENKINS_AGENT_SSH_PUBKEY=${pubkey}
EOF
```
* Verify `docker-compose -f docker-compose.yaml config`
* Start `docker-compose -f docker-compose.yaml up`
* Stop `docker-compose -f docker-compose.yaml down --remove-orphans && rm -rf jenkins_configuration/`
* Jenkins master initial password: `docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`


* Try a pipeline:
```json
pipeline {
    agent any  // Uses any available Jenkins agent
    stages {
        stage('first stage') {
            steps {
                sh 'ls -ltra'  // Executes the 'ls -la' command on the agent
            }
        }
        stage('second stage') {
            steps {
                sh 'java -version'
            }
        }
    }
}
```
