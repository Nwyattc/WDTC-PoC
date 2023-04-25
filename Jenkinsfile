pipeline {
    agent any

    stages {
        stage('Generate Configuration using Jinja2') {
            steps {
		sh 'sudo python3 lab11-createTemp.py'
                sh 'sudo ansible-playbook /etc/ansible/site.yaml'
            }
        }
        stage('Configure OSPF') {
            steps {
                echo "Stage2"
		sh 'sudo python3 lab11-ospfConfig.py'
            }
        }
 	stage('Configuring BGP') {
            steps {
                echo "Stage 3"
		sh 'sudo python3 lab11-confBGP.py'
            }
        }
        stage('Generate CPU utilization graph using SNMP') {
            steps {
                echo "Stage 4"
		sh 'sudo python3 -m pip install easysnmp'
		sh 'sudo python3 -m pip install matplotlib'
		sh 'sudo python3 lab11-CPUgraph.py'
            }
        }
    }
}
