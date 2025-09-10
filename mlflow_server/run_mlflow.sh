export MLFLOW_S3_ENDPOINT_URL=https://storage.yandexcloud.net
export AWS_ACCESS_KEY_ID=YCAJE3Nlz8iDILW5VTYM1ihQB
export AWS_SECRET_ACCESS_KEY=YCPjvS7uwhvJpUj3bKm8X-IX4QAwBIVsvX61IL44


mlflow server \
  --backend-store-uri postgresql://mle_20250729_0060996a6e_freetrack:3c05f7b15a854e81907215f46d411f6d@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_mle_20250729_0060996a6e \
  --default-artifact-root s3://s3-student-mle-20250729-0060996a6e-freetrack \
  --registry-store-uri postgresql://mle_20250729_0060996a6e_freetrack:3c05f7b15a854e81907215f46d411f6d@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_mle_20250729_0060996a6e \
  --host 0.0.0.0 \
  --port 5000 \
  --no-serve-artifacts