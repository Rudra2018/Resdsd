from fastapi import FastAPI
app=FastAPI(title='3rd EAI Dispatcher (placeholder)')
@app.get('/health')
def h(): return {'ok':True}
