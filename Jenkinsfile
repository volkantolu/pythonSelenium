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
      parallel {
        stage('shellScript') {
          steps {
            sh 'UnitTest.py'
          }
        }
        stage('') {
          steps {
            bat(script: 'python UnitTest.py', returnStdout: true, returnStatus: true)
          }
        }
      }
    }
  }
}