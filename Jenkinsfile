
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Virendra-Balasaheb-Desai/ci-cd-pipeline.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m compileall -q app.py'
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
    }
}
