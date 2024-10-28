# 개요
ansible을 이용하여 여러 서버에 대해 동일한 작업을 수행하는 방법을 기록합니다.

# 실행 방법
```bash
docker compose build
docker compose up -d
docker compose exec ansible bash
# 실행
ansible-playbook -i ./inventory/hosts.ini ./playbooks/ping.yml
```
