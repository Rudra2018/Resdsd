from fastapi import FastAPI
app=FastAPI(title='ZAP Runner (placeholder)')
@app.get('/health')
def h(): return {'ok':True}
