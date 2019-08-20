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
    stage('windowsBatchScript') {
      steps {
        bat(script: 'UnitTest.py: echo %errorlevel%', returnStdout: true, returnStatus: true)
      }
    }
  }
}