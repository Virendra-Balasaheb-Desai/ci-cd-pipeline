
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-app:latest'
        CONTAINER_NAME = 'devops-container'
    }

    stages {

        stage('Build & Test') {
            steps {
                echo 'Building test image and checking syntax...'
                sh 'docker build -t ${IMAGE_NAME} .'
                sh 'docker run --rm ${IMAGE_NAME} python -m compileall -q app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application container...'
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 5000:5000 \
                        ${IMAGE_NAME}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Checking running containers and application logs...'
                sh 'docker ps'
                sh 'docker logs ${CONTAINER_NAME}'
            }
        }
    }
}
