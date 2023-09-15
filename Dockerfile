FROM python:3.11.5-bookworm as base

FROM base as build
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY .coveragerc /
COPY app.py /
# RUN coverage run -m unittest
# RUN coverage report
RUN mypy --strict app.py
RUN black --check app.py
RUN python -m compileall app.py

FROM base as release
COPY *.txt /
COPY --from=build app.py /
ENTRYPOINT ["python", "app.py"]
