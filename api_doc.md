# FastAPI 服务 API 文档

本文档描述了服务的所有可用 API。服务的主要功能包括文件上传、任务启动及结果文件和图片获取。

---

## **基础信息**
- **API 根路径**: `/`
- **数据格式**: JSON
- **错误响应**: 所有错误响应均返回状态码和错误信息。

---

## **1. 获取服务信息**

### **GET /rosmontis**
检查服务状态。

#### **请求示例**
```http
GET /rosmontis HTTP/1.1
Host: <服务器地址>
```

#### **响应示例**
- **成功**: 返回服务欢迎信息
```json
{
  "message": "Meow~"
}
```

---

## **2. 文件上传**

### **POST /uploads**
上传文件并生成任务 ID。

#### **请求参数**
- **文件**: 通过 `multipart/form-data` 上传文件，支持以下文件类型：
  - `text/plain`
  - `application/octet-stream`

#### **请求示例**
```http
POST /uploads HTTP/1.1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary

------WebKitFormBoundary
Content-Disposition: form-data; name="file"; filename="example.txt"
Content-Type: text/plain

<文件内容>
------WebKitFormBoundary--
```

#### **响应示例**
- **成功**: 返回任务 ID 和上传状态
```json
{
  "code": 200,
  "message": "File uploaded successfully",
  "task_id": "<task_id>"
}
```

- **失败**: 文件类型不支持
```json
{
  "code": 400,
  "message": "File type not supported"
}
```

---

## **3. 启动任务**

### **GET /start**
启动任务并实时返回任务执行的日志。

#### **请求参数**
- **task_id** (必需): 任务 ID，需为有效的 SHA256 哈希值格式。

#### **请求示例**
```http
GET /start?task_id=<task_id> HTTP/1.1
```

#### **响应示例**
- **成功**: 返回任务执行日志（流式响应）
```
<任务日志内容>
END OF STREAM
```

- **失败**: 任务 ID 无效
```json
{
  "code": 400,
  "message": "Invalid task id"
}
```

---

## **4. 获取任务生成的图片**

### **GET /image**
根据任务 ID 获取生成的图片文件。

#### **请求参数**
- **task_id** (必需): 任务 ID，需为有效的 SHA256 哈希值格式。

#### **请求示例**
```http
GET /image?task_id=<task_id> HTTP/1.1
```

#### **响应示例**
- **成功**: 返回图片文件（`image/png` 格式）
- **失败**: 图片文件未找到
```json
{
  "code": 400,
  "message": "File not found"
}
```

---

## **5. 获取任务生成的文本文件**

### **GET /path**
根据任务 ID 获取生成的文本文件。

#### **请求参数**
- **task_id** (必需): 任务 ID，需为有效的 SHA256 哈希值格式。

#### **请求示例**
```http
GET /path?task_id=<task_id> HTTP/1.1
```

#### **响应示例**
- **成功**: 返回文本文件（`text/plain` 格式）
- **失败**: 文本文件未找到
```json
{
  "code": 400,
  "message": "File not found"
}
```

---

## **错误码**
| 错误码 | 描述                       |
|--------|----------------------------|
| 200    | 请求成功                   |
| 400    | 请求参数无效或文件未找到   |
| 500    | 服务内部错误               |

---

## **附加说明**
1. **task_id** 的生成规则：
   - 基于文件内容的 SHA256 哈希值、文件名、时间戳和预定义的盐值组合生成。
   - task_id 长度固定为 64 个字符。
2. 服务中的文件存储路径：
   - 上传文件存储在 `uploads` 目录。
   - 任务输出文件存储在 `output` 目录。
