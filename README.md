# file-xplorer

This Django project offers a feature-rich file management system and real-time resource monitoring capabilities. It allows users to navigate, upload, download, edit, rename, and delete files in a directory structure, and it also provides real-time system resource monitoring.

## Features

### File Management

- **File Explorer**: Browse and navigate through directories.
- **File Upload**: Upload files to the server.
- **File Download**: Download files from the server.
- **File Editing**: Edit text files directly from the browser.
- **File Renaming**: Rename files and folders.
- **File Deletion**: Delete files and folders.
- **File Preview**: Preview files directly in the browser.

### Real-Time Resource Monitoring

- **System Information**: Provides system platform, release, and architecture.
- **RAM Usage**: Displays RAM usage as a percentage and in GB.
- **Disk Usage**: Shows disk usage as a percentage and in GB.
- **CPU Usage**: Displays CPU usage as a percentage and core/thread information.
- **Network Usage**: Shows network bytes sent and received.

### Command Line Interface

- **Terminal Access**: Allows to access CLI from the base of the folder.

## Prerequisites

Before running this project, make sure you have the following:

- Python 3.x
- Django (compatible with Django Channels)
- Psutil (for resource monitoring)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   cd file-explorer
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Migrate the database:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the application in your web browser at `http://localhost:8000/`.

## Usage

### File Management

- Browse directories by clicking on folder names.
- Use the provided forms to create new folders, upload files, delete files, rename files, and create new text files.
- Click on a text file to edit it directly in your browser.
- Click on a file to download it.

### Real-Time Resource Monitoring

- Open the resource monitor at `http://localhost:8000/resource/`.
- Real-time resource information will be displayed.

## Terminal

- A terminal is also available for running commands on the server.
- Opens the terminal at `http://localhost:8000/terminal/`.
- Use the terminal to navigate to directories using `cd`, and execute shell commands.

## Contributing

Contributions to this project are welcome! If you find issues, have suggestions, or want to add new features, please open an issue or submit a pull request.

## Acknowledgments

Special thanks to [Yasin Bakhtiar](https://github.com/yasinbakhtiar) for creating the [FileManager HTML project](https://github.com/yasinbakhtiar/FileManager) that served as the inspiration and foundation for the file management aspects of this Django project.
