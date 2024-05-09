pipeline {
  agent any
  tools {
        // Specify the name of the Python installation configured in Jenkins
        // This ensures that the required version of Python is available on the agent
        PythonInstallation 'python3'
    }
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 hello.py'
      }
    }
  }
}
