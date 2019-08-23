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
        script {
          sonuc = bat(script: 'python -m unittest UnitTest.py', returnStdout: true, returnStatus: true)
          echo "${sonuc}"
          if("${sonuc}" == "1")
          currentBuild.result = 'FAILURE'
        }

      }
    }
  }
  post {
    always {
      echo 'always show this message'

    }

    success {
      echo 'Show this message when success'

    }

    failure {
      echo 'Show this message when failed'

    }

  }
}