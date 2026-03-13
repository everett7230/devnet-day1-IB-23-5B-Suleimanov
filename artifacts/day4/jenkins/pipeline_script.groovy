pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparing environment'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Results') {
            steps {
                echo 'Collecting results'
            }
        }
    }
}
