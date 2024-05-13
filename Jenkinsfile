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
        bat script: "email_from_txt.py %ROOT_DIR%"
       '
      }
    }
  }
}
