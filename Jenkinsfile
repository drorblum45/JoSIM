pipeline {
    agent any
    
    triggers {
        // Poll SCM every minute for changes
        pollSCM('* * * * *')
        // Alternative: Use webhook trigger (recommended)
        // githubPush()
    }
    
    stages {
        stage('Hello on Commit') {
            steps {
                script {
                    echo "Hello! New commit detected in JoSIM repository"
                    echo "Commit: ${env.GIT_COMMIT}"
                    echo "Branch: ${env.GIT_BRANCH}"
                    echo "Build Number: ${env.BUILD_NUMBER}"
                    echo "Timestamp: ${new Date()}"
                }
            }
        }
        
        stage('Optional: Build Info') {
            steps {
                script {
                    // Get commit message and author
                    def commitMessage = sh(
                        script: 'git log -1 --pretty=format:"%s"',
                        returnStdout: true
                    ).trim()
                    
                    def commitAuthor = sh(
                        script: 'git log -1 --pretty=format:"%an"',
                        returnStdout: true
                    ).trim()
                    
                    echo "Commit Message: ${commitMessage}"
                    echo "Author: ${commitAuthor}"
                }
            }
        }
    }
    
    post {
        always {
            echo "Pipeline completed for JoSIM repository"
        }
        success {
            echo "Hello pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed - but still saying hello!"
        }
    }
}