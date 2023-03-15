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
                sh 'docker-compose up -d --force-recreate --build --no-deps app'
            }
        }
        stage('Docker Push') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                sh "docker tag calci thugrock/calculator"
                sh 'docker push thugrock/calculator'
                }
            }
        }
        state('Clean the Clients'){
            agent any
            steps{
                sh "ansible-playbook clean_clients.yml -i hosts"
            }
        }
        stage('Deploy by Ansible'){
            agent any
            steps{
                sh "ansible-playbook calculator.yml -i hosts"
            }
        }
    }
}
