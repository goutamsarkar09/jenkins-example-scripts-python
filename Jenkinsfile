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
        bat "python email_from_txt.py $workspace\\email_body.txt"
        bat 'dir'
      }
    }
  }
}
