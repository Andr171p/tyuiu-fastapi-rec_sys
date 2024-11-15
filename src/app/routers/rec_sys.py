from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.middleware.globals import g
from src.app.schemas.request import UserRequestSchema
from src.app.schemas.response import UserResponseSchema
from src.app.services.form import get_user_df


rec_sys_router = APIRouter()


@rec_sys_router.post(path='/recommend/', response_model=UserResponseSchema)
async def get_user_recommendation(request: UserRequestSchema) -> JSONResponse:
    scaler = g.scaler
    model = g.model
    top_n = request.top_n
    user = request.user
    data = get_user_df(user=user)
    x = scaler.standard(data=data)
    model.predict(x=x)
    recommendations: list[str] = model.recommend(top_n=top_n)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': recommendations
        }
    )
