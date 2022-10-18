## Endpoint Template:

<br>

- [x] We use the following template to describe each of our endpoints.
- [x] Everything between the guillemots (« and ») should be replaced to describe the endpoint.
- [x] Mandatory fields are:
  - Endpoint path
  - Endpoint method
  - Response
  - Response shape
- [x] Optional fields:
  - If the endpoint needs to know who the person is, then include the **_Headers/Authorization_** part.
  - If the endpoint is a POST, PUT, or PATCH, include the Request shape (JSON) part.

<br>

- Endpoint path: «path to use»
- Endpoint method: «HTTP method»
- Query parameters:
  - «name»: «purpose»
- Headers:
  - Authorization: Bearer token
- Request shape (JSON):
  ```json
  «JSON-looking thing that has the
  keys and types in it»
  ```
- Response: «Human-readable description
  of response»
- Response shape (JSON):
  ```json
  «JSON-looking thing that has the
  keys and types in it»
  ```

---

<br>

## API Design:

<br>

### 1. Log in:

- Endpoint path: /login
- Endpoint method: POST
- Request shape (form):
  - username: string
  - password: string
- Response: Account information
- Response shape (JSON):
  ```json
  {
    "account": {
        "username": string,
        "password": string,
    },
    "token": string
  }
  ```

<br>

### 2. Chats history:

- Endpoint path: /chats
- Endpoint method: GET
- Headers:
  - Authorization: Bearer token
- Response: chats history
- Response shape:
  ```json
  {
    "chats": [
      {
        "avatar_url": string,
        "contact_name": string,
        "msg_preview": string,
      }
    ]
  }
  ```

<br>

### 3. Contacts list:

- Endpoint path: /contacts
- Endpoint method: GET
- Headers:
  - Authorization: Bearer token
- Response: A list of contacts
- Response shape:
  ```json
  {
    "contacts": [
      {
        "avatar_url": string,
        "contact_name": string,
      }
    ]
  }
  ```

<br>

### 4. Chat:

- Endpoint path: /chat
- Endpoint method: POST
- Headers:
  - Authorization: Bearer token
- Request body:
  ```json
  {
    "posts": [
      {
        "contact_name": string,
        "post_text": string,
        "image_url": string,
        "video_url": string,
        "time_stamp": timestamp,
      }
    ]
  }
  ```
- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```

<br>

### 5. [stretch goal] Moments - list of posts:

- Endpoint path: /moments
- Endpoint method: GET
- Headers:
  - Authorization: Bearer token
- Response: A list of posts
- Response shape:
  ```json
  {
    "moments": [
      {
        "avatar_url": string,
        "contact_name": string,
        "post_text": string,
        "image_url": string,
        "video_url": string,
        "time_stamp": string,
        "likes": smallint,
      }
    ]
  }
  ```

<br>

### 6. Create a post:

- Endpoint path: /moments
- Endpoint method: POST
- Headers:
  - Authorization: Bearer token
- Request body:
  ```json
  {
    "post": {
      "avatar_url": string,  <!-- necessary ??????? -->
      "contact_name": string,  <!-- necessary ??????? -->
      "post_text": string,
      "image_url": string,
      "video_url": string,
      "time_stamp": timestamp,
    }
  }
  ```
- Response: An indication of success or failure
- Response shape:
  ```json
  {
    "success": boolean,
    "message": string
  }
  ```
  <br>

### 7. Profile page - create post & post history:

- Endpoint path: /user
- Endpoint method: GET
- Headers:
  - Authorization: Bearer token
- Response: the user detail
- Response shape:
  ```json
  {
    "user": {
      "username": string,
      "create_post": {
        "post_content": text,
        "image_url": string,
        "video_url": string,
        "time_stamp": timestamp,
      },
    },
    "posts_history": array,  <!-- ??????? -->
  }
  ```

<br>

### 8. Log out:

- Endpoint path: /logout
- Endpoint method: DELETE
- Headers:
  - Authorization: Bearer token
- Response: Always true
- Response shape (JSON):
  ```json
  true
  ```