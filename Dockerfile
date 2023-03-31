FROM python:3.7 AS runtime

RUN apt-get update && \
    apt-get -y install libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir paddlepaddle==2.4.1 paddleocr==2.0.6 && \
    pip install --no-cache-dir -U opencv-python==4.6.0.66

RUN pip uninstall -y paddleocr Flask
#RUN pip uninstall -y Flask-Babel websockets aiofiles aiohttp aiosignal gradio


CMD ["/bin/bash"]


FROM runtime AS production

RUN git clone https://github.com/PantsuDango/DangoOCR.git /app

WORKDIR /app

ENTRYPOINT ["python", "app.py"]
