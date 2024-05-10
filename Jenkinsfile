pipeline {
  agent any

stages {
    stage('version') {
      steps {
        python --version
      }
    }
    stage('hello') {
      steps {
        python hello.py
      }
    }
  }
}
