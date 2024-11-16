from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.app.middleware.globals import g
from src.app.schemas.request import UserRequestSchema
from src.app.schemas.response import UserResponseSchema
from src.app.services.form import UserForm

from src.preprocessing.utils import encode_labels


rec_sys_router = APIRouter()


@rec_sys_router.post(path='/recommend/', response_model=UserResponseSchema)
async def get_user_recommendation(request: UserRequestSchema) -> JSONResponse:
    ohe = g.ohe
    scaler = g.scaler
    model = g.model
    inputs = UserForm(user=request.user)
    inputs.fill()
    data = inputs.get()
    x = encode_labels(data)
    x = ohe.transform(x)
    x = scaler.transform(x)
    model.predict(x=x)
    recommendations: list[str] = model.recommend(top_n=request.top_n)
    return JSONResponse(
        content={
            'status': 'ok',
            'data': recommendations
        }
    )
