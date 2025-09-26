from fastapi import FastAPI, HTTPException, status
from .schemas import User, UserUpdate

app = FastAPI()
users: list[User] = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def add_user(user: User):
    if any(u.user_id == user.user_id for u in users):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
    users.append(user)
    return user

#Allow users to update user
@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    for u in users:
        if u.user_id == user_id:
            if user.user_id:
                #Check if user_id already exist
                if any(v.user_id==user.user_id for v in users):
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="user_id already exists")
                u.user_id = user.user_id
            if user.name:
                u.name = user.name
            if user.email:
                #Check if email already exist
                if any(v.email==user.email for v in users):
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already exists")
                u.email = user.email
            if user.age:
                u.age = user.age
            if user.student_id:
                #Check if student_id already exist
                if any(v.student_id==user.student_id for v in users):
                    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="student_id already exists")
                u.student_id = user.student_id
            return u
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

#Allow users to delete user
@app.delete("/api/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    for u in users:
        if u.user_id == user_id:
            users.remove(u)
            return True
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.get("/health")
def get_health():
    return {"status": "ok"}