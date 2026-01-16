# Django Todo App

A simple and elegant todo application built with Django.

## Features

- ✅ Create, read, update, and delete todos
- ✅ Mark todos as complete/incomplete
- ✅ Add descriptions and due dates to todos
- ✅ View todo details
- ✅ Admin interface for managing todos
- ✅ Beautiful, responsive UI with gradient background

## Project Structure

```
todos/
├── models.py          # Todo model definition
├── views.py           # View functions
├── urls.py            # URL routing
├── admin.py           # Django admin configuration
├── apps.py            # App configuration
├── migrations/        # Database migrations
└── templates/
    └── todos/
        ├── base.html         # Base template with styling
        ├── todo_list.html    # List all todos
        ├── todo_detail.html  # View single todo
        └── todo_form.html    # Create/edit todo form
```

## Getting Started

### 1. Install Dependencies

Make sure you have the virtual environment activated and install Django if not already installed:

```bash
pip install django
```

### 2. Apply Migrations

Migrations have already been created and applied. The database tables are ready to use.

### 3. Create a Superuser (Optional - for Admin Access)

```bash
python manage.py createsuperuser
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

The app will be available at:
- **Todo App**: http://localhost:8000/
- **Todo Admin**: http://localhost:8000/admin/

## URLs

- `/` - List all todos (home page)
- `/create/` - Create a new todo
- `/todo/<id>/` - View todo details
- `/todo/<id>/update/` - Edit a todo
- `/todo/<id>/toggle/` - Toggle completion status
- `/todo/<id>/delete/` - Delete a todo
- `/admin/` - Django admin interface

## Todo Model Fields

- **title** (CharField) - Todo title (required, max 200 chars)
- **description** (TextField) - Detailed description (optional)
- **completed** (BooleanField) - Completion status (default: False)
- **due_date** (DateTimeField) - Due date and time (optional)
- **created_at** (DateTimeField) - Creation timestamp (auto)
- **updated_at** (DateTimeField) - Last update timestamp (auto)

## Features Breakdown

### Todo List View
- Displays all todos with status indicators
- Shows completion progress (e.g., "2/5 completed")
- Quick actions to toggle, edit, or delete todos
- Empty state message when no todos exist

### Todo Detail View
- Shows full todo information
- Displays creation and update timestamps
- Shows due date if set
- Buttons to edit, mark complete/incomplete, or delete

### Todo Form
- Supports creating new todos
- Allows editing existing todos
- Optional description field
- Optional due date picker with datetime support
- Form validation

## Styling

The app features a modern, responsive design with:
- Gradient purple background
- Smooth animations and hover effects
- Card-based layout
- Touch-friendly buttons
- Responsive grid that adapts to mobile screens

## Database

The app uses SQLite (default Django database) stored at `db.sqlite3`.

To reset the database:
```bash
# Delete db.sqlite3
# Then run migrations again
python manage.py migrate
```

## Admin Interface

The Django admin interface includes:
- List view of all todos with filters
- Search functionality for title and description
- Bulk edit options
- Filter by completion status and creation date
- Readonly timestamp fields

## Future Enhancements

Potential improvements:
- User authentication and per-user todos
- Categories/tags for todos
- Priority levels
- Recurring todos
- Notifications for due dates
- Drag-and-drop reordering
- Dark mode toggle
