pipeline {
    agent any
    environment {
        PYTHON_ENV = 'C:\\Python39\\python.exe' // Update with your Python path
    }
    stages {
        stage('Clone Repository') {
            steps {
git branch: 'main', url: 'https://github.com/<your-repo>.git'
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
                        ${PYTHON_ENV} -m pip show matplotlib || ${PYTHON_ENV} -m pip install matplotlib
                        ${PYTHON_ENV} -m pip show seaborn || ${PYTHON_ENV} -m pip install seaborn
                    """
                }
            }
        }
        stage('Train Model and Generate Plots') {
            steps {
                // Run the Python script that trains the model and generates plots
bat "${PYTHON_ENV} train_model.py"
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Archive the model and plots as Jenkins artifacts
                archiveArtifacts artifacts: 'iris_model.pkl, feature_pair_plot.png, decision_tree_structure.png, feature_importance_plot.png', fingerprint: true
            }
        }
    }
}
