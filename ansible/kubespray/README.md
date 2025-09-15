# Ansible 과 kubespray 를 통한 k8s 설치/삭제 방법 

1. kubespray 환경 구성
```bash
# 1. kubespray Image 실행
docker compose up -d
docker compose exec kubespray bash
```
2. 노드 IP 환경 구성
아래 파일 수정
- inventory/inventory.ini

## K8S 설치
```bash
ansible-playbook -b -v -i inventory/mycluster/inventory.ini cluster.yml 
ansible-playbook -b -v -i  inventory/mycluster/inventory.ini custom_playbooks/install_zsh.yml
```

## K8S 제거
```bash
ansible-playbook  -b -v -i inventory/mycluster/inventory.ini reset.yml
```


참고 사이트:
- https://hokka1179.tistory.com/22
- https://readthedocs.vinczejanos.info/Blog/2023/04/21/install-kube-tailscale/#install-kubernetes-cluster-behind-tailscale-vpn
- https://kubespray.io/#/
- https://github.com/kubernetes-sigs/kubespray/tree/release-2.28
