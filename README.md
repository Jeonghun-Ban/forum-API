forum-API
===
![Python](https://img.shields.io/badge/Python-3.7.6-green.svg)
![Docker](https://img.shields.io/badge/Docker-19.03.8-skyblue.svg)
![Postgres](https://img.shields.io/badge/PostgreSQL-10.0-blue.svg)
![Redis](https://img.shields.io/badge/Redis-latest-red.svg)

flask-based bulletin board service API

API 구조
---

### User API

| URL | method | Usage |
|-----|--------|-------|
| /user/register | POST | 회원가입 |
| /user/login | POST | 로그인 |
| /user/logout | GET | 로그아웃 |

### Board API

| URL | method | Usage |
|-----|--------|-------|
| /board/ | GET | 게시판 목록 조회 |
| /board/ | POST | 게시판 생성 |
| /board/\<str:board_name\> | PUT | 게시판 이름 변경 |
| /board/\<str:board_name\> | DELETE | 게시판 제거 |

### BoardArticle API

| URL | method | Usage |
|-----|--------|-------|
| /board/\<str:board_name\> | GET | 글 목록 조회 |
| /board/\<str:board_name\> | POST | 글 생성 |
| /board/\<str:board_name\>/\<int:article_id> | GET | 글 내용 조회 |
| /board/\<str:board_name\>/\<int:article_id> | PUT | 글 제목 혹은 내용 수정 |
| /board/\<str:board_name\>/\<int:article_id> | DELETE | 글 제거 |

### Dashboard API

| URL | method | Usage |
|-----|--------|-------|
| /board/all | GET | 모든 게시판에서 최근 n개의 글의 제목 가져옴 |

실행 방법
---

```bash
docker-compose up
```

루트 디렉토리에서 위 명령어로 서버를 실행합니다.


- 이후 웹 브라우저에서 `127.0.0.1`로 접속해서 API call을 테스트하실 수 있습니다.
- `Swagger UI` 적용을 위해 `flask-restplus`를 사용했습니다.

### 주의할 점
- 콘솔에서 직접 API call을 테스트할 수 있습니다만, 사용자를 특정해야 하는 요청에는 `세션쿠키`를 전송해야만 합니다.
-  `세션쿠키`는 로그인 요청 시 HTTP 응답 헤더의 `Set-Cookie`에서 확인할 수 있습니다.

    <details><summary>콘솔 사용 예시</summary>
    
    로그인 시
    ```
    http 127.0.0.1/user/login 'email=<email>' 'password=<password>'  HTTP/1.0 200 OK
    Content-Length: 69
    Content-Type: application/json
    Date: Thu, 19 Mar 2020 18:46:19 GMT
    Server: Werkzeug/0.16.1 Python/3.7.6
    Set-Cookie: session=eyJzZXNzaW9uIjoiNzU4MDFiZGYtNTkyOC00YjYwLTljZmMtMWJkNDAwMmZmYzU3In0.XnO9-w.JoWYrJwfpgPzxmUj4SEfkUYYVo4; HttpOnly; Path=/
    Vary: Cookie

    {
        "message": "Successfully Logged in",
        "status": "success"
    }
    ```

    로그아웃 시
    ```bash
    # httpie로 요청 시
    http 127.0.0.1/user/logout 'Cookie:session=eyJzZXNzaW9uIjoiNzU4MDFiZGYtNTkyOC00YjYwLTljZmMtMWJkNDAwMmZmYzU3In0.XnO9-w.JoWYrJwfpgPzxmUj4SEfkUYYVo4'

    HTTP/1.0 200 OK
    Content-Length: 70
    Content-Type: application/json
    Date: Thu, 19 Mar 2020 18:59:22 GMT
    Server: Werkzeug/0.16.1 Python/3.7.6
    Set-Cookie: session=; Expires=Thu, 01-Jan-1970 00:00:00 GMT; Max-Age=0; Path=/    
    {
        "message": "Successfully Logged out",
        "status": "success"
    }
    ```

</details>


디렉터리 구조
---

        .
        ├── README.md
        ├── docker-compose.yml
        ├── flask
        │   ├── Dockerfile
        │   ├── __init__.py
        │   ├── requirements.txt
        │   ├── src
        │   │   ├── __init__.py
        │   │   ├── alembic.ini
        │   │   ├── app
        │   │   │   ├── __init__.py
        │   │   │   ├── config.py
        │   │   │   ├── models.py
        │   │   │   ├── controllers
        │   │   │   └── services
        │   │   ├── manage.py
        │   │   ├── migrations
        │   │   │   ├── README
        │   │   │   ├── __init__.py
        │   │   │   ├── env.py
        │   │   │   ├── script.py.mako
        │   │   │   └── versions
        │   │   └── utils
        │   │       ├── __init__.py
        │   │       ├── redis.py
        │   │       ├── restplus.py      
        │   │       └── sqlalchemy.py
        │   └── uwsgi.ini
        └── nginx
            ├── Dockerfile
            └── default.conf
