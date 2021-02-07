# Guise Task
> You must upload some images before deleting and retrieving

> For all the below tasks, i created only one link `http://localhost:8000/api` and Just change the `method` of request (supported methods `GET`, `POST`, `DELETE`)

Tasks
---
- Image upload
- Delete
- Retieving images by their name

Pass the below parameters for appropriate tasks
---
> API link `http://localhost:8000/api` and pass below params
- Upload
  `image` - File input(image file)
- Delete
  `image` - Text input(image name)
- List images
  `q` - Search by name of images (`max-limit` is `5`)

This project also have a GUI version
---
> Just visit `http://localhost:8000`

To setup project on your machines
---
- Clone it
- Create virtualenv
`$ virtualenv -p python3 venv`
- Activate it
`$ source venv/bin/activate`
- Then do the following setup via cmds
`cd <repo-project>`
`pip install -r requirements.txt`
`./manage.py migrate`
`./manage.py runserver 0:8000`
- Now visit in browser with this link
`http://localhost:8000`