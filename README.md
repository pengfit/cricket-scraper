
# 🧭 Playwright Python Docker Test Runner

本项目用于在 **Docker 环境中运行 Playwright（Python 版）端到端测试**。
每个模块（如 `gov_xian`, `gov_beijing` 等）都可以 **单独运行并生成独立测试报告**。

---

## 📁 项目结构

```
/app/
├── src/
│   ├── gov_xian/
│   │   └── tests/
│   │       └── test_xian.py
│   ├── gov_beijing/
│   │   └── tests/
│   │       └── test_beijing.py
│   └── ...
├── reports/                 # pytest-html 报告输出
├── requirements.txt
├── pytest.ini
├── run_test.sh
├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ 环境说明

本项目基于官方 Playwright Python 镜像：

```
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy
```

该镜像自带：

* Python 3.x
* Playwright 及浏览器（Chromium、Firefox、WebKit）
* 所有系统依赖

---

## 📦 安装依赖

### requirements.txt

```
pytest
pytest-playwright
pytest-html
playwright
```

### pytest.ini

```
[pytest]
addopts = --self-contained-html
```

---

## 🧰 run_test.sh

脚本用于根据环境变量 `GOV_MODULE` 动态执行对应模块测试并生成报告。

```
#!/usr/bin/env bash
set -e

echo "🔹 Running tests for: ${GOV_MODULE}"

mkdir -p reports

pytest "src/${GOV_MODULE}" \
  --tracing=on \
  --html="reports/${GOV_MODULE}.html" \
  --self-contained-html

echo "✅ Report generated at reports/${GOV_MODULE}.html"
```

---

## 🐳 Dockerfile

```
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV GOV_MODULE=gov_xian

CMD ["bash", "run_test.sh"]
```

---

## 🧩 docker-compose.yml

```
version: "3.8"

services:
  gov_xian:
    build: .
    environment:
      - GOV_MODULE=gov_xian
    ipc: host
    volumes:
      - .:/app
  # 更多模块可依次添加
```

---

## 🚀 使用说明

### ▶️ 构建镜像

```
docker compose build
```

### ▶️ 运行单个模块

```
docker compose run --rm gov_xian
```

或手动运行：

```
docker build -t gov-tester .
docker run --rm --ipc=host -e GOV_MODULE=gov_xian -v $(pwd)/reports:/app/reports gov-tester
```

### ▶️ 同时运行多个模块

```
docker compose up --abort-on-container-exit
```

---

## 📊 测试报告

执行后会在本地生成：

```
reports/
├── gov_xian.html
├── gov_beijing.html
└── ...
```

每个模块的报告可直接在浏览器打开查看。

---

## 🧪 调试模式（可视化浏览器）

进入容器交互模式：

```
docker run -it --rm --ipc=host gov-tester bash
```

然后手动运行：

```
pytest --headed --slowmo 300 src/gov_xian/tests/test_xian.py
```

---

## 🧠 可选增强

* 支持并行执行：

  ```
  pip install pytest-xdist
  pytest -n auto
  ```
* 在 CI/CD 环境中，可将报告挂载或上传到云端（例如 GitHub Actions artifacts）。
* 若只使用 Chromium，可在 Dockerfile 中安装特定浏览器：

  ```
  RUN playwright install chromium --with-deps
  ```

---

## ✅ 总结

| 功能     | 实现方式                                                |
| ------ | --------------------------------------------------- |
| 单模块测试  | `docker compose run --rm gov_xian`                  |
| 多模块并行  | `docker compose up`                                 |
| 自动生成报告 | `reports/{gov_xxx}.html`                            |
| 可视化调试  | `pytest --headed --slowmo 300`                      |
| 依赖镜像   | `mcr.microsoft.com/playwright/python:v1.55.0-jammy` |

---