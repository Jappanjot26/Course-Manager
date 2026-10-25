# Course Manager

## Run with Docker

The project is fully containerized. Docker is the only prerequisite; Python,
Django, and all application dependencies are installed inside the image.

1. Install and start [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Create an environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

3. Build and start the application:

   ```powershell
   docker compose up --build
   ```

Open <http://localhost:8000/admin/> after the container starts. Database
migrations run automatically on container startup.
SQLite data is persisted in the `course_manager_data` Docker volume.

To create an administrator:

```powershell
docker compose exec web python manage.py createsuperuser
```

Stop the application with:

```powershell
docker compose down
```

To remove the persisted database as well, run `docker compose down -v`.
