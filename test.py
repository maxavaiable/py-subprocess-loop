import subprocess_loop

def on_request(data):
    return data+1

subprocess_loop.Child.run(on_request)