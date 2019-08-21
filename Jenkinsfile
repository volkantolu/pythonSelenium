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
        bat(script: 'UnitTest.py', returnStdout: true, returnStatus: true)
        echo 'hello world New'
        echo '%stdout%'
        echo '%ERROR_LEVEL%'
        echo '%failures%'
      }
    }
    stage('Unit Tests') {
      steps {
        bat(script: 'python -m unittest UnitTest.py', returnStdout: true, returnStatus: true)
        echo '%ERROR_LEVEL%'
      }
    }
  }
}