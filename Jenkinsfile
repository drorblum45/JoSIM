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
        
        stage('Build Project') {
            steps {
                echo "=== BUILDING PROJECT ==="
                sh '''
                    mkdir -p build
                    cd build
                    cmake ..
                    cmake --build . --config Release
                '''
            }
        }
        
        stage('Run Simulation') {
            steps {
                echo "=== RUNNING SIMULATION ==="
                sh '''
                    cd build
                    ./josim-cli -o ./ex_jtl_basic.csv ../test/ex_jtl_basic.cir -V 1
                '''
            }
        }
        
        stage('Validate Output') {
            steps {
                echo "=== VALIDATING OUTPUT ==="
                sh 'python3 scripts/validate_csv.py build/ex_jtl_basic.csv'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'build/ex_jtl_basic.csv', allowEmptyArchive: true
        }
        success {
            echo "Build and simulation pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed - check logs for details"
        }
    }
}