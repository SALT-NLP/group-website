# Editting Group Website

To avoid conflict, please open PR to edit the website!

## Basic Edit

Making the specified changes to the group website is straightforward and you even don't need to set up a local development environment to do it. Check out [Developer Guide](#developer-guide) if you need more extensive modifications.

### Add/Modify/Delete a group member
To add a group member to the website, do the following steps:
1. Create a folder under `content/authors` using the member's name. The folder name shall only contain `a-zA-Z0-9` and `-`.
2. Add the member's photo to the folder. Rename the photo to `avatar.jpg`.
3. Create a file named `_index.md` in the folder. Add the following content:
    ```
    ---
    title: {Name of the Member}
    superuser: False
    role: {'Master' or 'Undergraduate'; otherwise, leave this field blank.}

    # Additional information (e.g., coadvise)
    additional_info: {If no additional information, leave this field blank.}

    # Order to show in compared to other authors
    weight: {Postdoc 1xx, PhD student 2xx, Master/Undergrad 3xx; check out the last person's weight in the corresponding group and add 1.}

    social:
      - icon: home
        icon_pack: fas
        link: {home page link; if None, comment out these three lines using `#`}
      - icon: twitter
        icon_pack: fab
        link: {twitter link; if None, comment out these three lines using `#`}

    user_groups:
      - Current Members
      - {"Postdocs" or "PhD Students" or "Master & Undergraduate Students"}

    ---
    ```

Modify content under the corresponding folder if you want to modify an existing group member.

To delete a group member from the website, delete the corresponding folder under `content/authors`.

### Add news
1. Open [content/home/news.md](content/home/news.md). 

2. Locate `<table class="no-hover-effect-or-stripes" style="border-collapse: collapse;">` and add the following code after it (start a new line).
    ```
    <tr class="news-item">
      <td style="border: none;">MM/YYY</td>
      <td style="border: none;">Content of the news.</td>
    </tr>
    ```

Currently, we show the first 10 news in `<table class="no-hover-effect-or-stripes" style="border-collapse: collapse;"> </table>`.


### Add/Modify a publication
To add a paper to the website, do the following steps:
1. Create a folder under `content/papers`. The folder name shall only contain `a-zA-Z0-9` and `-`.
2. Create a file named `index.md` in the folder. Add the following content:
    ```
    ---
    title: {paper title}
    authors: ['{author1}', '{author2}', ..., '{authorn}']
    categories: []
    date: "yyyy-mm-dd"
    preprint: {false/true}
    conference: {conference name if not preprint}
    paper: {paper link}
    code: {code link if available; otherwise, leave this field blank}
    webpage: {code link if available; otherwise, leave this field blank}
    award: {description of award if any; otherwise, leave this field blank}
    ---
    ```

Modify content under the corresponding folder if you want to modify an existing paper.

### Add/Modify a course
To add a course to the website, do the following steps:
1. Create a folder under `content/courses`. The folder name shall only contain `a-zA-Z0-9` and `-`.
2. Create a file named `index.md` in the folder. Add the following content:
    ```
    ---
    title: {course name}
    link: {link}
    location: "Stanford University"
    date: 'yyyy-mm-dd'
    times: ["{time1}", ...]
    ---
    ```

### Add/Remove Photos
1. Add the jpg file under `static/files`.
2. Locate `<div class="slider">` in [content/home/photo.md](content/home/photo.md) and change its content accordingly.

### Change other descriptions in `Home`
- The lab introduction can be modified in [content/authors/admin/_index.md](content/authors/admin/_index.md) after `---`.
- "Contact Us" can be modified in [content/home/contact.md](content/home/contact.md) after `+++`.
- "Funding" can be modified in [content/home/funding.md](content/home/funding.md) after `+++`.


## Developer Guide

This website is built with [Hugo Blox](https://docs.hugoblox.com/), a framework based on Go. Here are some useful documentations:
- Hugo Go language: https://gohugo.io/about/
- Archived template source (this website is not based on the latest version): https://github.com/HugoBlox/hugo-blox-builder/tree/main/modules/blox-bootstrap

### Set up local development environment
- Follow instructions on [this page](https://docs.hugoblox.com/getting-started/install-hugo/) to install hugo and dependencies
- Clone this repository and cd into the directory.
- Run `hugo server --disableFastRender`

### Codebase Overview
```
├── assets
│   ├── iamges
│   │   ├── icon.png # favicon
│   │   ├── logo.svg # logo on the navigation tab
│   ├── scss
│   │   ├── custom.scss # Add CSS rule here to override the template.
├── config/_default
│   ├── config.toml    # Usually no need to change.
│   ├── languages.toml # Usually no need to change.
│   ├── menus.toml     # Configurate the navigation bar.
│   ├── params.toml    # Usually no need to change.
├── content
│   ├── authors
│   │   ├── admin/ # lab introduction
│   │   ├── ...    # member information
│   ├── courses
│   │   ├── ...  # course information
│   ├── home  # widget_page, each widget on `Home` tab is maintained in a `.md` file.
│   │   ├── index.md   # Declare the widget page.
│   │   ├── about.md   # "about" widget, implemented in layouts/partials/widgets/about.html
│   │   ├── news.md    # Use a blank widget for custom content.
│   │   ├── photo.md   # Use a blank widget for custom content.
│   │   ├── news.md    # Use a blank widget for custom content.
│   │   ├── contact.md # Use a blank widget for custom content.
│   │   ├── funding.md # Use a blank widget for custom content.
│   ├── papers
│   │   ├── ...  # paper information
│   ├── people # widget_page, each widget on `People` tab is maintained in a `.md` file.
│   │   ├── index.md   # Declare the widget page.
│   │   ├── people.md  # "people" widget, implemented in layouts/partials/widgets/people.html
│   │   ├── alumni.md  # Use a blank widget for custom content.
│   ├── publication # widget_page, each widget on `Publications` tab is maintained in a `.md` file.
│   │   ├── index.md        # Declare the widget page.
│   │   ├── publication.md  # "publication" widget, implemented in layouts/partials/widgets/publication.html
│   ├── resources # widget_page, each widget on `Resources` tab is maintained in a `.md` file.
│   │   ├── index.md      # Declare the widget page.
│   │   ├── resources.md  # "resources" widget, implemented in layouts/partials/widgets/resources.html
├── data             # Part of the template, no need to change.
├── layouts/partials # Implementation of widgets.
├── static           # media files
├── ...              # Other files, no need to change.
```


## Deployment
The group website is currently deployed on a server provided by [Stanford Domains](https://domains.stanford.edu/) under the cpanel called `salt`. The corresponding domain name is  https://saltlab.stanford.edu/.

### Update the website on Stanford Domains server

Currently, Yijia Shao will update the website when there are new PRs. May figure out how to automate this process in the future :)

1. In the local development environment, run `hugo` and compress `./public` into `public.zip`.

2. Log in the server through https://domains.stanford.edu/dashboard/. Click "File Manager" under the "Files" menu to upload `public.zip`. Then click "Terminal" under the "Advanced" menu. In the terminal, run `bash update_website.sh`.
