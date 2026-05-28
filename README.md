# Undergrad E-Portfolio Tutorial

A free, ready-to-use portfolio template for students. No coding experience needed. No installs. Just edit the files and put it live on the internet in minutes.

**Scan the QR code below to open this project on GitHub, then fork it to get your own copy.**

![QR code to this GitHub repo](qr-code.png)

---

## What is in this project?

| File | What it does |
|------|-------------|
| `index.html` | Your home page — the first thing people see |
| `projects.html` | A page to show your projects |
| `skills.html` | A page to list your skills |
| `resume.html` | A page with your education and work history |
| `contact.html` | A page with your email and social links |
| `css/style.css` | Controls the colours and layout on every page |
| `images/` | Put your photos and screenshots here |
| `resume.pdf` | Upload your CV here as a PDF |
| `templates/` | 6 pre-made designs — pick one if you want a different look |
| `AI_PROMPTS.md` | Prompts to help you edit with ChatGPT or Claude |
| `HOSTING_GUIDE.md` | Step-by-step instructions to get your site live |

---

## How to get started

1. **Fork this repo** — click the Fork button at the top right. This gives you your own copy.
2. **Turn on GitHub Pages** — go to Settings → Pages → Source → main branch → Save.
3. Your site goes live at `https://your-username.github.io/undergrad-eportfolio-tutorial/` within a minute.
4. **Edit the files** to replace the placeholder text with your real information.

For full step-by-step instructions (including how to add your photo and resume), read [`HOSTING_GUIDE.md`](HOSTING_GUIDE.md).

---

## The 6 themes

There are 6 pre-made designs for different fields. Open `templates/index.html` to see them all side by side.

| Template file | Best for |
|---------------|----------|
| `template-cs.html` | Computer Science / Software Engineering |
| `template-design.html` | Design / UX / Creative Arts |
| `template-data.html` | Data Science / Machine Learning |
| `template-bio.html` | Biology / Life Sciences / Pre-Med |
| `template-business.html` | Business / Finance / Consulting |
| `template-arch.html` | Architecture / Civil / Urban Design |

To use one, copy its contents into `index.html` and replace the placeholder text.

---

## Change the colour scheme

Open `css/style.css` and change these 4 lines at the top. Every button, link, and highlight on every page will update.

```css
:root {
  --accent:      #2563eb;   /* main colour */
  --accent-dark: #1d4ed8;   /* hover colour */
  --bg:          #f8fafc;   /* page background */
  --surface:     #ffffff;   /* card background */
}
```

---

## Checklist — things to update after you fork

- [ ] Replace `Your Name` in all 5 HTML files
- [ ] Add your photo — upload `profile.jpg` into the `images/` folder
- [ ] Add your real projects in `projects.html`
- [ ] Fix the skill percentages in `skills.html`
- [ ] Add your real education and work history in `resume.html`
- [ ] Update your email, GitHub, and LinkedIn links in `contact.html`
- [ ] Upload your CV as `resume.pdf`
- [ ] Pick a colour — change `--accent` in `css/style.css`

---

## Why no JavaScript?

Everything — the mobile menu, progress bar animations, hover effects — works with CSS only. This means no installs, no setup, and no broken dependencies. If you want to add JavaScript later, `AI_PROMPTS.md` has prompts to help you do that.
