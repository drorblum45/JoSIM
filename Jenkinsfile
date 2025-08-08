pipeline {
    agent any
    
    triggers {
        // Poll SCM every minute for changes.
        pollSCM('* * * * *')
    }
    
    stages {
        stage('Build Project') {
            steps {
                echo "Build Project"
                sh '''
                    # Set PATH to include common locations for Homebrew
                    export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
                    
                    mkdir -p build
                    cd build
                    cmake .. -DCMAKE_MESSAGE_LOG_LEVEL=ERROR
                    cmake --build . --config Release
                '''
            }
        }
        
        stage('Run Simulation') {
            steps {
                echo "Run Simulation"
                sh '''
                    cd build
                    ./josim-cli -o ./ex_jtl_basic.csv ../test/ex_jtl_basic.cir -V 1
                '''
            }
        }
        
        stage('Validate Output') {
            steps {
                echo "Validate Output"
                sh 'python3 scripts/validate_csv.py build/ex_jtl_basic.csv --expected-value 6.283185 --tolerance 0.1'
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