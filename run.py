import uvicorn

# # Package # #

def run():
    """Run the API using Uvicorn"""
    uvicorn.run(
        'app:app',
        port=5000,
        host='localhost',
        reload=True,
    )
if __name__=='__main__':
    run()