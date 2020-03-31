FROM evarga/jenkins-slave
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip

