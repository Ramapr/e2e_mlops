from fastapi import FastAPI


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    '''
    load model to runtime

    load_model_all()
    '''
    pass


@app.post('/predict')
async def predict():
    '''
    add schema , resp model

    logic
    '''
    pass
