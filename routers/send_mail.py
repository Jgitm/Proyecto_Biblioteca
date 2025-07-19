from fastapi import APIRouter, FastAPI, Body

from helpers.send_mail import EmailRequest, send_email

router = APIRouter(prefix="/send-email", tags=["send_mail"])

@router.post("/")
async def enviar_correo(request: EmailRequest = Body(...)):
    return send_email(request.to, request.subject, request.message)