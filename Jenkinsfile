pipeline {
    agent any
    
    environment {
        TEST_NAME = 'ex_jtl_basic'
        VALUE_NAME = 'B01'
        EXPECTED_VALUE = '6.283185'
        TOLERANCE = '5.0'
    }
    
    triggers {
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
                    ./josim-cli -o ./${TEST_NAME}.csv ../test/${TEST_NAME}.cir -V 1
                '''
            }
        }
        
        stage('Validate Output') {
            steps {
                echo "Validate Output"
                sh 'python3 scripts/validate_csv.py build/${TEST_NAME}.csv --arg-name ${VALUE_NAME} --expected-value ${EXPECTED_VALUE} --tolerance ${TOLERANCE}'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'build/${TEST_NAME}.csv', allowEmptyArchive: true
        }
        success {
            echo "Build and simulation pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed - check logs for details"
        }
    }
}