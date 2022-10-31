# Fast API Demo
---

## Description:
FastAPI framework, high performance, easy to learn, fast to code, ready for production

## The key features are:

- **Fast** --> Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
Fast to code: Increase the speed to develop features by about 200% to 300%.
- **Fewer bugs** --> Reduce about 40% of human (developer) induced errors.
- **Intuitive** --> Great editor support. Completion everywhere. Less time debugging.
- **Easy** --> Designed to be easy to use and learn. Less time reading docs.
- **Short** --> Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- **Robust** --> Get production-ready code. With automatic interactive documentation.
- **Standards-based** --> Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

# Getting Started
1. clone repository
```
git clone <repo name>
```

2. install dependencies
```
cd fast_api && sudo pip install -r requirements.txt
```

3. run code (dev)
```
uvicorn main:app --reload
```

4. run code (prod)
```
uvicorn main:app --host localhost --port 3000
```
To keep a persistent connection, and to refesh during updates, add the ```--reload``` switch.

```
uvicorn main:app --host localhost --port 3000 --reload
```


4. test endpoints
* [/](http://localhost:3000)
* [/api/info](http://localhost:3000/api/info)
* [/api/release](http://localhost:3000/api/release)
* [/api/projects](http://localhost:3000/api/release)
* [/api/products](http://localhost:3000/api/release)

OR

* ```curl http://localhost:3000```
* ```curl http://localhost:3000/info```
* ```curl http://localhost:3000/release```
