from os import access
from fastapi import APIRouter, Depends, routing, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2

router = APIRouter(
    prefix='/login',
    tags=['Authentification']
)

@router.post('/')#, response_model=schemas.Token)
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db)
    ):

    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
        ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid credentials')

    if not utils.verify(
        user_credentials.password,
        user.password
        ):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Invalid credentials'
            )
    
    access_token = oauth2.create_access_token(data={'user_id': user.id})
    
    return {'acess_token': access_token, 'token_type': 'bearer'}

