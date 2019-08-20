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
        bat(script: 'stdout = bat(returnStdout: true, script: \'git rev-parse HEAD\')         println("stdout ################ " + stdout + " ####################")', returnStdout: true, returnStatus: true, label: 'stdout')
        echo 'hello world New'
        echo '%stdout%'
        echo '%ERROR_LEVEL%'
        echo '%failures%'
      }
    }
  }
}