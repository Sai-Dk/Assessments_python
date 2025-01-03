from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get("/gold-rate", response_class=HTMLResponse)
async def get_gold_rate():
    api_key = "be796c63d2d30bc2672f03b334186145"  # Replace with your actual API key
    url = "https://api.metalpriceapi.com/v1/latest"
    params = {
        "api_key": api_key,
        "base": "USD",
        "currencies": "INR"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code == 200:
        gold_data = response.json()
        print("API Response:", gold_data)

        try:
            inr_rate = gold_data["rates"]["INR"]
            usd_inr_rate = gold_data["rates"]["USDINR"]
        except KeyError:
            raise HTTPException(status_code=404, detail="Gold rate data not found in the response")

        html_content = f"""
        <html>
            <head>
                <title>Gold Rate</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                    }}
                    .rate-container {{
                        max-width: 600px;
                        margin: 40px auto;
                        padding: 20px;
                        border: 1px solid #ddd;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                </style>
            </head>
            <body>
                <div class="rate-container">
                    <h1>Current Gold Rate</h1>
                    <p>Gold Rate in INR: {inr_rate} INR</p>
                    <p>Conversion Rate (USD to INR): {usd_inr_rate} INR per USD</p>
                </div>
            </body>
        </html>
        """
        return HTMLResponse(content=html_content)
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", "API request failed"))

