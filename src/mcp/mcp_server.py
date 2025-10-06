from fastmcp import FastMCP
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from dotenv import load_dotenv

import uvicorn

import requests
import base64
import os
import json

load_dotenv()

mcp = FastMCP("APP-Assistant")

# Define custom middleware
custom_middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
]


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")


@mcp.custom_route("/diagnostic/status/heartbeat", methods=["GET"])
async def diagnostic_status_heartbeat(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")


http_app = mcp.http_app(middleware=custom_middleware)

@mcp.tool(description="Return the current communication preferences for a provided cafe id")
def get_subs_by_cafe_id(cafe_id: str) -> dict:
    """
    Return the current communication preferences for a provided cafe id

    Args:
        cafe_id: cafe id to look up

    Returns:
        Communication preferences as a dictionary

    Raises:
        ValueError: If the specified ID is not found
    """
    response = requests.get(
            f"http://localhost:9090/preferences/{cafe_id}",
            timeout=2,
        )
    return response.json()



@mcp.tool(description="Return the cafe id for a provided email address")
def get_cafe_id_for_email(email: str) -> list[dict]:
    """
    Return cafe id for a provided email address

    Args:
        email: email address to look up

    Returns:
        cafe id as a list of dictionaries

    Raises:
        ValueError: If the specified email is not found
    """
    response = requests.get(
        f"http://localhost:7070/user?email={email}",
        timeout=2,
    )
    return response.json()

@mcp.tool(description="Return the hotel user id for a provided email address")
def get_hotel_user_id_for_email(email: str) -> list[dict]:
    """
    Return id for a provided email address

    Args:
        email: email address to look up

    Returns:
        hotel user id as a list of dictionaries

    Raises:
        ValueError: If the specified email is not found
    """
    response = requests.get(
        f"http://localhost:8080/user?email={email}",
        timeout=2,
    )
    return response.json()




# @mcp.tool(
#     description="Try multiple tools to get user id by email, fallback if not found"
# )
# def get_id_for_email(email: str) -> dict:
#     # Try cafe ID first
#     try:
#         cafe_result = get_cafe_id_for_email(email)
#         if cafe_result and cafe_result != []:
#             return {"type": "cafe", "result": cafe_result}
#     except Exception as e:
#         pass
#     hotel_result = get_hotel_user_id_for_email(email)
#     # Check if hotel_result is a non-empty list and does not contain an error
#     if hotel_result:
#         return {"type": "hotel", "result": hotel_result}
#
#     return {"error": "No user id found for email"}

if __name__ == "__main__":
    print("Hello from app-assistant powered by FastMCP!")
    uvicorn.run(http_app, host="127.0.0.1", port=8000)
