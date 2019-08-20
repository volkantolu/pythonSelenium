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
        echo 'hello world2'
        bat(script: 'UnitTest.py', returnStdout: true, returnStatus: true, label: 'batchOutput')
        echo 'hello world3'
        echo '%errorlevel%'
        echo '%failures%'
        echo '%batchOutput%'
        unstable '%batchOutput%'
        unstable 'batchOutput'
      }
    }
  }
}