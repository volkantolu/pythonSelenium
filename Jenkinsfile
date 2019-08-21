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
        stdout = bat(returnStdout: true, script: 'UnitTest.py')    
        println("stdout ################ " + stdout + " ####################")
    }
  }
}
