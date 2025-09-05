from fastapi import FastAPI
app=FastAPI(title='3rd EAI Worker (placeholder)')
@app.get('/health')
def h(): return {'ok':True,'note':'Run Docker heavy images for full functionality.'}
