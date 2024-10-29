#!/bin/bash

export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'

# Vault가 준비될 때까지 대기
until vault status; do
  echo "Waiting for Vault..."
  sleep 1
done

# 시크릿 경로에 데이터 저장 예제
vault kv put secret/myapp username="admin" password="supersecretpassword"
vault kv put secret/database db_name="mydb" db_password="dbpassword"
