pipeline {
  agent {
    docker {
      image 'python:3.7.4'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      post {
        always {
          junit 'test-reports/*.xml'

        }

      }
      steps {
        sh 'python UnitTest.py'
      }
    }
  }
}