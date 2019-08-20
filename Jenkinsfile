pipeline {
  agent any
  stages {
    stage('wait') {
      steps {
        sleep 5
      }
    }
    stage('message') {
      steps {
        echo 'hello world'
      }
    }
    stage('shellScript') {
      steps {
        sh 'UnitTest.py'
      }
    }
  }
}