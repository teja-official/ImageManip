# Image manipulator
> You must upload some images before deleting and retrieving

**One link multi functional**

> For all the below tasks, i created only one link `http://imagemanip.herokuapp.com/api`, it will serves for all requests and Just change the `method` of request (supported methods `GET`, `POST`, `DELETE`)

Tasks
---
- Image upload
- Delete
- Retrieve all images
- Retieving images by their name

Pass the below parameters for appropriate tasks
---
> API link `http://imagemanip.herokuapp.com/api` and pass below params
- Upload `[POST]`
  `image` - File input(image file)
  ```json
    {"image": "an-image.png"}
  ```
- Delete `[DELETE]`
  `image` - Text input(image id)
  ```json
    {"image": 21}
  ```
- List all images `[GET]`
  `all` - Checkbox input
  ```json
    {"all": true}
  ```
- List images `[GET]`
  `q` - Search by name of images (`max-limit` is `5`)
  ```json
    {"q": "an-image"}
  ```


This project also have a GUI version
---
> Just visit `http://imagemanip.herokuapp.com`

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


Visit my LinkedIn profile
---
[![N|Solid](https://www.seoclerk.com/pics/want59614-1T309j1520843586.png)](https://www.linkedin.com/in/dharma-teja-547572132/)
