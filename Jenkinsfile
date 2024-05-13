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
        def result = bat script: "python email_from_txt.py D:\\JPX\\TASK_DAY_WISE\\2024\\email_body.txt", returnStdout: true
      }
    }
  }
}
