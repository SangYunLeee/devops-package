# plane — Plane(프로젝트 관리) 셀프호스팅 docker compose

```bash
docker compose up -d      # http://localhost  (관리자: admin@plane.local / admin123 — 기본값, 띄운 뒤 바꾼다)
```

- `compose.yaml` — postgres·redis·minio·plane(api·worker·beat·web)·nginx
- `init-superuser.py` — migrate 뒤 관리자 계정과 인스턴스 설정을 만든다 (`ADMIN_EMAIL`·`ADMIN_PASSWORD`)
- `nginx.conf` — `/api/` 는 api, 나머지는 web 으로
- 비밀값은 전부 로컬 시험용 기본값이다. 밖에 띄울 땐 `SECRET_KEY`·DB·MinIO 값을 바꾼다.
- ⚠️ `minio/minio`·`minio/mc` 공식 이미지는 Docker Hub 에서 내려갔다(2025). 새로 받을 땐 다른 이미지로 바꿔야 한다.
