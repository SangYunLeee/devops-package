#Dockerfile

FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

#---- docker-ce-cli
RUN apt-get update && apt-get install -y docker-ce-cli

#---- sshpass
RUN apt-get -y install sshpass

#---- locale
RUN apt-get install -y locales git \
    && localedef -f UTF-8 -i ko_KR ko_KR.UTF-8

#---- yq
RUN curl -fsSL https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/local/bin/yq \
    && chmod +x /usr/local/bin/yq

#---- argocd
RUN curl -fsSL -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64 \
    && chmod +x /usr/local/bin/argocd

ENV LC_ALL ko_KR.UTF-8

USER jenkins
