pipeline {
    agent any

    stages {
        stage('Clone git') {
            steps {
                git "https://github.com/thugrock/calculator.git"
            }
        }
        stage('Build Code') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Build docker image'){
            agent any
            steps{
                sh 'sudo docker-compose up -d --force-recreate --build --no-deps app'
            }
        }
        stage('Docker Push') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                sh "sudo docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                sh "sudo docker tag calci thugrock/calculator"
                sh 'sudo docker push thugrock/calculator'
                }
            }
        }
    }
}
