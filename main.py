# import uvicorn
# from fastapi import FastAPI, Form, Depends, Request
# from fastapi_sqlalchemy import DBSessionMiddleware, db
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware

# from schema import Kit as SchemaKit
# from schema import Cirurgia as SchemaCirurgia

# from schema import Kit
# from schema import Cirurgia

# from models import Kit as ModelKit
# from models import Cirurgia as ModelCirurgia

# import os
# from dotenv import load_dotenv

# load_dotenv('.env')


# app = FastAPI()



# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get("/")
# async def root():
#     return {"message": "hello world"}

# # @app.post('/enviar_kit/', response_model=SchemaKit)
# # async def kit(kit: SchemaKit):
# #     db_kit = ModelKit(nome_instrumento = kit.nome_instrumento)
# #     db.session.add(db_kit)
# #     db.session.commit()
# #     return db_kit

# @app.post('/enviar_kit/', response_model=SchemaKit)
# def create_kit(kit: SchemaKit, db: Session):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get('/verificar_kit/')
# async def verificar_kit():
#     kit = db.session.query(ModelKit).all()
#     return kit

# # @app.get('/book/')
# # async def book():
# #     book = db.session.query(ModelBook).all()
# #     return book

# # @app.post('/author/', response_model=SchemaAuthor)
# # async def author(author:SchemaAuthor):
# #     db_author = ModelAuthor(name=author.name, age=author.age)
# #     db.session.add(db_author)
# #     db.session.commit()
# #     return db_author

# # @app.get('/author/')
# # async def author():
# #     author = db.session.query(ModelAuthor).all()
# #     return author

# @app.exception_handler(ValueError)
# async def value_error_exception_handler(request: Request, exc: ValueError):
#     return JSONResponse(
#         status_code=400,
#         content={"message": str(exc)},
#     )

# # To run locally
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)




from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/")
async def root():
    return {"message": "hello world"}

@app.post("/add_kit/", response_model=schemas.Kit)
def create_kit(kit: schemas.KitCreate, db: Session = Depends(get_db)):
    return crud.create_kit(db=db, kit=kit)




@app.get("/kit/", response_model=list[schemas.Kit])
def read_kit(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_kit(db, skip=skip, limit=limit)


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
