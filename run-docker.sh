docker system prune -f

docker build --no-cache -t rampup-knn .
docker run --name rampup-knn rampup-knn
docker run  --name rampup-knn-container rampup-knn
docker cp rampup-knn-container:/app/csv/output.csv .
docker container stop rampup-knn-container
