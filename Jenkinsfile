pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }
        stage('Find Changed Files') {
            steps {
                script {
                    // Find changed files
                    def changedFiles = sh(script: 'git diff --name-only HEAD~1', returnStdout: true).trim().split('\n')
                    
                    // Run the make target
                    sh 'make run_all'
                    // sh "python3 ./main.py ${changedFiles}"
                    // Loop through each changed file and call the Python script
                    // changedFiles.each { file ->
                    //     sh "python3 ./main.py ${file}"
                    // }
                }
            }
        }
    }
}
