import os
import re
import subprocess
import time
from hashlib import sha256
from fastapi import FastAPI, UploadFile, Query
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse, FileResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,  # 允许携带凭证（如 cookies）
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有 HTTP 头
)
# 定义文件存储路径
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # 确保目录存在

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SALT = "rosmontisMeow~"

@app.get("/rosmontis")
async def root():
    return {"message": "Meow~"}


@app.post("/uploads")
async def upload_file(file: UploadFile):
    # 检查文件类型
    if file.content_type not in ["text/plain", "application/octet-stream"]:
        return {
            "code": 400,
            "message": "File type not supported",
        }

    try:
        # 计算文件哈希值
        content = await file.read()
        file_hash_sha256 = sha256(content).hexdigest()

        # 获取安全的文件名
        file_name = os.path.basename(file.filename)

        # 生成任务 ID
        timestamp = int(time.time() * 1000)
        task_id = file_hash_sha256 + file_name + SALT + str(timestamp)
        task_id = sha256(task_id.encode("utf-8")).hexdigest()

        # 构造文件路径，添加时间戳避免冲突
        file_path = os.path.join(UPLOAD_DIR, f"{task_id}.txt")

        # 存储文件
        with open(file_path, "wb") as f:
            f.write(content)

        return {
            "code": 200,
            "message": "File uploaded successfully",
            "task_id": task_id,
        }

    except Exception as e:
        return {
            "code": 500,
            "message": f"Failed to process file: {str(e)}"
        }


@app.get("/start")
async def task_start(task_id: str = Query(...)):
    # 验证 task_id 的合法性
    if not re.match(r'^[a-f0-9]{64}$', task_id):
        return {
            "code": 400,
            "message": "Invalid task id",
        }

    def generator():
        try:
            # 使用 subprocess 启动子进程
            path = os.path.join("fmt", "kmeans3.py")
            process = subprocess.Popen(
                ["python", path, task_id],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # 持续读取子进程的输出流
            for line in iter(process.stdout.readline, ''):
                yield line

            # 等待进程结束
            process.wait()

            # 如果子进程返回非零退出码，读取 stderr 并返回错误信息
            if process.returncode != 0:
                error_output = process.stderr.read()
                yield f"ERROR: {error_output}\n"

        except Exception as e:
            yield f"ERROR: {str(e)}\n"

        # 明确流结束标志
        yield "END OF STREAM\n"

    return StreamingResponse(generator(), media_type="text/plain")



@app.get("/image")
async def task_image(task_id: str = Query(...)):
    # 验证 task_id 的合法性
    if not re.match(r'^[a-f0-9]{64}$', task_id):
        return {
            "code": 400,
            "message": "Invalid task id",
        }
    img_path = os.path.join(OUTPUT_DIR, f"{task_id}.png")
    if not os.path.exists(img_path):
        return {
            "code": 400,
            "message": "File not found",
        }
    return FileResponse(img_path, media_type="image/png")



@app.get("/path")
async def task_path(task_id: str = Query(...)):
    # 验证 task_id 的合法性
    if not re.match(r'^[a-f0-9]{64}$', task_id):
        return {
            "code": 400,
            "message": "Invalid task id",
        }
    data_path = os.path.join(OUTPUT_DIR, f"{task_id}.txt")
    if not os.path.exists(data_path):
        return {
            "code": 400,
            "message": "File not found",
        }
    return FileResponse(data_path, media_type="text/plain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)