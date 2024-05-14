pipeline {
  agent any

stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('hello') {
      steps {
        script{
        // bat "python email_from_txt.py $workspace\\email_body.txt"
        def body2 = bat(script:"python email_from_txt.py $workspace\\email_body.txt", returnStdout: true)
        print body2
        }
      }
    }
  }
}
