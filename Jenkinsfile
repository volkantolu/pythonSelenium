pipeline {
  agent any
  stages {
    stage('Source Code - Git') {
      steps {
        sleep 5
      }
    }
    stage('Alert') {
      steps {
        echo 'hello world'
      }
    }
    stage('Run Tests') {
      steps {
        script {
          sonuc = bat(script: 'python -m unittest UnitTest.py', returnStdout: true, returnStatus: true)
          //sonuc = bat(script: 'python -m unittest UnitTest.py', returnStdout: true)
          //sonuc = bat(script: 'python -m unittest UnitTest.py', returnStatus: true)
          //sonuc = bat(script: 'python -m unittest UnitTest.py')
          //echo "{sonuc}"
          echo sonuc.toString()
          if (sonuc == 1){
            bat(script: 'exit 1')
            currentBuild.result = 'FAILRUE'
            //return
          }
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