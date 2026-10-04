# Editting Group Website

> **Note:** Automatic deployment is currently broken because the server blocks GitHub's IPs. After your PR is merged into `main`, someone with SSH access to the server must deploy it manually. See [Deployment](#deployment).

**To avoid conflict, please open PR to edit the website!** The `main` branch is protected from direct commits.

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
The group website is currently deployed on a server provided by [Stanford Domains](https://domains.stanford.edu/) under the cpanel called `salt` (server IP `146.190.148.141`). The corresponding domain name is https://saltlab.stanford.edu/.

The GitHub workflow ([.github/workflows/deploy.yml](.github/workflows/deploy.yml)) still builds the site on every commit to `main`, but it can no longer upload to the server because the server blocks GitHub's IPs. Until that's fixed, deploy manually with the script below.

### Deploy with `scripts/deploy.sh`
Requirements: [Hugo](https://docs.hugoblox.com/getting-started/install-hugo/) (extended, v0.121.2 to match CI) and SSH access to the server (your public key must be authorized for the `saltsudo` account, e.g. via cPanel → "SSH Access").

1. Check out the latest `main`:
    ```
    git checkout main && git pull
    ```
2. Run the deploy script from the repository root:
    ```
    scripts/deploy.sh
    ```
    It builds the site into `./public`, uploads it to the server with `scp`, and syncs it into the docroot (`~/saltlab.stanford.edu`), deleting stale files.
3. Open https://saltlab.stanford.edu/ to check the change is live.

You can override the defaults with environment variables, e.g.:
```
DEPLOY_USER=saltsudo DEPLOY_HOST=146.190.148.141 SSH_KEY=~/.ssh/id_ed25519 scripts/deploy.sh
```
Other options are `DEPLOY_PORT` (default `22`) and `DEPLOY_PATH` (default `saltlab.stanford.edu`, relative to the remote home directory).

### Fallback: upload through cPanel
If you don't have SSH access:

1. In the local development environment, run `hugo` and compress `./public` into `public.zip`.

2. Log in the server through https://domains.stanford.edu/dashboard/. Click "File Manager" under the "Files" menu to upload `public.zip`. Then click "Terminal" under the "Advanced" menu. In the terminal, run `bash update_website.sh`.
