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
        bat(script: 'python -m unittest UnitTest.py', returnStdout: true, returnStatus: true)
      }
      
    }
  }
  
  post {
        always {
            echo "evrything is success"
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
  
}
