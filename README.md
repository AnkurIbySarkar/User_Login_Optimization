# User_Login_Optimization

This project benchmarks and tests different methods of validating user existence in a PostgreSQL database:

- Brute-force (in Python)
- Unindexed SQL
- Indexed SQL
- Batched check

## Run Locally

```bash
make install
docker-compose up -d
make run
