pipeline {
    agent any
    
    triggers {
        // Poll SCM every minute for changes.
        pollSCM('* * * * *')
    }
    
    stages {
        stage('Debug Branch Info') {
            steps {
                script {
                    echo "=== BRANCH DEBUG INFO ==="
                    echo "Current branch: ${env.GIT_BRANCH}"
                    echo "Git commit: ${env.GIT_COMMIT}"
                    echo "Build cause: ${currentBuild.getBuildCauses()}"
                    
                    // Show all branches
                    sh 'git branch -a'
                    sh 'git remote show origin'
                }
            }
        }
        
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
        
        stage('Build Info') {
            steps {
                script {
                    try {
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
                    } catch (Exception e) {
                        echo "Could not get git info: ${e.getMessage()}"
                    }
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