
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-app:latest'
        CONTAINER_NAME = 'devops-container'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'docker build -t devops-app:test .'
                sh 'docker run --rm devops-app:test python -m compileall -q app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f devops-container || true
                    docker run -d \
                        --name devops-container \
                        -p 5000:5000 \
                        devops-app:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
                sh 'docker logs devops-container'
            }
        }
    }
}
