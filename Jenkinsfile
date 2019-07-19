pipeline{
    agent {
        docker { image 'eeacms/pylint'}
    }
    stages{
        stage('Code pull'){
            steps {
            checkout scm
            }
        }
        stage('Run pylint'){
            steps{
                sh 'pylint *'
            }
        }
    }
}