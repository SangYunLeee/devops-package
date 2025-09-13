# 개요
ansible을 이용하여 여러 서버에 대해 동일한 작업을 수행하는 방법을 기록합니다.

# 실행 방법
```bash
docker compose build
docker compose up -d
docker compose exec ansible bash
# 정상 동작 확인
cd infra-setup
ansible-playbook -i ./inventory/hosts.ini ./playbooks/ping.yml
```

# kubespray 를 통한 클러스터 구성
```bash
# 인벤토리 생성
cd kubespray
cp -rfp inventory/sample inventory/mycluster
declare -a IPS=(
    # 클러스터 노드 IP 작성
    10.10.1.3
    10.10.1.4
    10.10.1.5
)
CONFIG_FILE=inventory/mycluster/hosts.yaml python3 contrib/inventory_builder/inventory.py ${IPS[@]}

# 생성된 파일 확인
cat inventory/mycluster/group_vars/all/all.yml
cat inventory/mycluster/group_vars/k8s_cluster/k8s-cluster.yml
cat inventory/mycluster/hosts.yaml

# 클러스터 구성
ansible-playbook -i inventory/mycluster/hosts.yaml cluster.yml
```
