pipeline {
    agent any
    
    triggers {
        // Poll SCM every minute for changes.
        pollSCM('* * * * *')
    }
    
    stages {
        
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
                    # Set PATH to include common locations for Homebrew
                    export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
                    
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