
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-app:latest'
        CONTAINER_NAME = 'devops-container'
    }

    stages {

        stage('Test') {
            steps {
                echo 'Testing application...'
                sh 'docker build -t devops-app:test .'
                sh 'docker run --rm devops-app:test python -m compileall -q app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t devops-app:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application container...'
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
                echo 'Checking running containers and application logs...'
                sh 'docker ps'
                sh 'docker logs devops-container'
            }
        }
    }
}
