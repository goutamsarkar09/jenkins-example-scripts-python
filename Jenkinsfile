pipeline {
  agent any
  tools {
        // Specify the name of the Python installation configured in Jenkins
        // This ensures that the required version of Python is available on the agent
        python
    }
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python hello.py'
      }
    }
  }
}
