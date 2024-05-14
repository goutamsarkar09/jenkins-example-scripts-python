import groovy.json.*
def jsonData, jsonObject // For parsing the JSON property file.
pipeline {
	agent any

	stages {
		stage('Reading JSON property file') {
			steps {
				script 
				{
					// Read the JSON data from the file:
					jsonData = readFile("$workspace\\jenkins_properties.json").trim()

							// Parse the JSON data into a Groovy object: 
							jsonObject = readJSON text: jsonData
				}
			}
		}
		stage('version') {
			steps {
				bat 'python --version'
			}
		}
		stage('hello') {
			steps {
				script{
					print jsonObject
					// bat "python email_from_txt.py $workspace\\email_body.txt"
					def body2 = bat(script:"python email_from_txt.py $workspace\\$jsonObject.body_file_name", returnStdout: true)
					print "$jsonObject.body_file_name"
					print body2
				}
			}
		}
	}
}
