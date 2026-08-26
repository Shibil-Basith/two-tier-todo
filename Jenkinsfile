pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ShibilBasith11/todoapp'
        REGISTRY_CREDENTIALS = 'dockerhub-creds'
    }

    stages {

        stage('1. Checkout SCM') {
            steps {
                checkout scm

                sh 'echo "Building Workspace on commit: ${GIT_COMMIT}"'
            }
        }

        stage('2. Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .

                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('3. Registry Authentication & Push') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: "${REGISTRY_CREDENTIALS}",
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                        docker push ${IMAGE_NAME}:${BUILD_NUMBER}

                        docker push ${IMAGE_NAME}:latest
                    '''
                }
            }
        }

        stage('4. Continuous Deployment') {
            steps {
                sh '''
                    # Gracefully stop and remove obsolete running container
                    docker stop webpage_prod || true
                    docker rm webpage_prod || true

                    # Launch updated container mapped to host port 8080
                    docker run -d \
                        --name webpage_prod \
                        -p 8080:80 \
                        ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }

        success {
            echo "Pipeline build #${BUILD_NUMBER} completed successfully!"
        }

        failure {
            echo "Pipeline build #${BUILD_NUMBER} failed. Review console logs."
        }
    }
}
