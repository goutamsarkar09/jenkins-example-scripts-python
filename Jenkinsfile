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
        bat 'email_from_txt.py ./email_body.txt'
      }
    }
  }
}
