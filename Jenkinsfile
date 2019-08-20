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
        outputValue = bat(script: 'UnitTest.py', returnStdout: true, returnStatus: true, label: 'stdout')
        println("outputValue ## " + outputValue + " ##")
        echo 'hello world New'
        echo '%stdout%'
        echo '%ERROR_LEVEL%'
        echo '%failures%'
      }      
    }
  }
}
