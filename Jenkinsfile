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
    stage('') {
      steps {
        sh 'python UnitTest.py'
      }
    }
  }
}