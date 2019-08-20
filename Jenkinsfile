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
        bat(script: 'UnitTest.py', returnStdout: true, returnStatus: true, label: 'batchOutput')
        echo 'hello world New'
        echo '%batchOutput%'
        echo '%ERROR_LEVEL%'
        echo '%failures%'
      }
    }
  }
}