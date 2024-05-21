# TenantTransit

TenantTransit is a tool to facilitate data migration between two Microsoft 365 tenants. It enables the migration of emails and other data related to Exchange Online and OneDrive for Business efficiently and securely.

## Key Features

- Discovers all users with mailboxes in the source tenant.
- Allows for user matching between source and target tenants.
- Executes email and data migration jobs asynchronously.
- Provides secure API endpoints for controlling and monitoring migration progress.

## Technology Stack

- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLAlchemy (with support for different backends like PostgreSQL, MySQL, SQLite)
- **Asynchronous Task Queue**: Celery
- **Authentication Tool**: OAuth2 with JWT
- **API Security**: Passport.js
- **Integration with Microsoft Graph**: HTTP Requests

## Installation and Usage

### Docker Deployment

1. Clone the repository:

```bash
git clone https://github.com/your_username/TenantTransit.git
cd TenantTransit
