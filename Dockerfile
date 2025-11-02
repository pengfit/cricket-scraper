FROM mcr.microsoft.com/playwright/python:latest

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

ENV GOV_MODULE=""

# 使用绝对路径运行
CMD ["bash", "run_test.sh"]
