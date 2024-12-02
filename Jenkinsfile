pipeline {
    agent any
    environment {
        PYTHON_ENV = 'C:/Users/Administrator/AppData/Local/Programs/Python/Python313/python.exe' // Update with your Python path
    }
    stages {
        stage('Clone Repository') {
            steps {
                echo "---------------------cloning repo -----------------------"
                git branch: 'main', url: 'https://github.com/trilok-dev/model_build.git'
            }
        }
        stage('Check & Install Dependencies') {
            steps {
                script {
                    // Check and install Python dependencies using Windows commands
                    bat """
                        ${PYTHON_ENV} -m pip show pandas || ${PYTHON_ENV} -m pip install pandas
                        ${PYTHON_ENV} -m pip show scikit-learn || ${PYTHON_ENV} -m pip install scikit-learn
                        ${PYTHON_ENV} -m pip show joblib || ${PYTHON_ENV} -m pip install joblib
                    """
                }
            }
        }
        stage('Train Model') {
            steps {
                bat "${PYTHON_ENV} train_model.py"
            }
        }
        stage('Archive Model') {
            steps {
                archiveArtifacts artifacts: 'iris_model.pkl', fingerprint: true
            }
        }
    }
}
