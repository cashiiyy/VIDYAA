from livekit import api
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# Your LiveKit Cloud API credentials
API_KEY = "APIW4Amd77Nxo2H"
API_SECRET = "FHjftKuo52psNn7tZg0kVek5qtfgJ7ujpFD1f27WZ4RC"

app = FastAPI()

@app.get("/get-token")
def get_token(identity: str = "android-user-123"):
    # Create an access token
    token = (
        api.AccessToken(API_KEY, API_SECRET)
        .with_identity(identity)
        .to_jwt()
    )
    return JSONResponse({"token": token})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)