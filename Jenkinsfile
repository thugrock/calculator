pipeline {
    agent any

    stages {
        stage('Clone git') {
            steps {
                git "https://github.com/thugrock/calculator.git"
            }
        }
        stage('Building Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testing Code') {
            steps {
                sh 'python3 test_app.py'
            }
            post {
                always {junit 'test-reports/*.xml'}
            }
        }
        stage('Building image'){
            agent any
            steps{
                sh 'docker-compose up -d --force-recreate --build --no-deps app'
            }
        }
        stage('Pushing image to Hub') {
            agent any
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                sh "docker tag calci thugrock/calculator"
                sh 'docker push thugrock/calculator'
                }
            }
        }
        stage('Clean the Clients'){
            agent any
            steps{
                catchError(buildResult: "SUCCESS", stageResult: "SUCCESS") {
                    sh "ansible-playbook clean_clients.yml -i hosts"
                }
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
