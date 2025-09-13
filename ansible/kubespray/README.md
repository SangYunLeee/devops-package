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
ansible-playbook -i inventory/sample/inventory.ini cluster.yml -b -v
```

## K8S 제거
```bash
ansible-playbook -i inventory/sample/inventory.ini reset.yml -b -v
```
