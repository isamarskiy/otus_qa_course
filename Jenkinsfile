pipeline{
    agent {
        docker { image 'eeacms/pep8'}
    }
    stages{
        stage('Code pull'){
            steps {
            checkout scm
            }
        }
        stage('Run peep8'){
            steps{
                sh 'pep8 *'
            }
        }
    }
}