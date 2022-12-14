from fastapi import APIRouter, Body, Header, Depends, Request
from handlers.depends import refresh_token, access_token
from handlers.response import OK
from utils.jwt import create_access_token, create_refresh_token

auth = APIRouter()


@auth.post(
    "/signin",
    summary='SignIn',
    tags=['auth'],
)
async def login(request: Request):
    """
    Login API
    """
    form_data = await request.json()
    print(form_data)
    username = form_data['username']
    password = form_data['password']
    # form_data = await request.form()
    if username == "admin" and password == "admin":
        return OK({
            "message": "Login Success",
            "access_token": create_access_token(username),
            "refresh_token": create_refresh_token(username)
        })
    else:
        return OK({"message": "Login Failed"})


@auth.post(
    "/refresh",
    summary="Token Refresh",
    tags=['auth']
)
async def refresh(
    identity: str = Depends(refresh_token),
):
    """
    Refresh Token API
    """
    return OK({
        "message": "Refresh Success",
        "access_token": create_access_token(identity),
        "refresh_token": create_refresh_token(identity)
    })


@auth.get(
    "/me",
    summary="Get User Info",
    tags=['auth']
)
async def me(
    identity: str = Depends(access_token),
):
    """
    Get User Info API
    """
    return OK({
        "message": "Get User Info Success",
        "username": identity
    })