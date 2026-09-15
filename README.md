 # Atreyify

Atreyify is my interactive developer portfolio. It presents projects, experience, education, and technical interests in a music-player-inspired interface rather than as a conventional resume page.

The site is a single-page frontend built with plain HTML, CSS, and JavaScript. It has no frontend framework or package dependency. The dark layout, project tracklist, search, responsive navigation, audio controls, progress display, and contribution view are all implemented in the browser.

## What is included

- Search across the portfolio content from the header search field.
- Project and experience sections presented as an interactive tracklist.
- Browser audio controls powered by the Web Audio API.
- Animated playback state and equalizer details.
- Responsive sidebars and player controls for smaller screens.
- Project summaries covering VeriLogic, STP, CLARITI, and Manga-Sketcher-AI.

## Project structure

```text
index.html       The portfolio UI and client-side behavior
main.py          Small WSGI app used by the Vercel adapter
api/index.py     Vercel Python entry point
vercel.json      Routes requests to the Python entry point
```

## Run it locally

The frontend can be opened directly, but a local server is better for testing browser behavior:

```bash
git clone https://github.com/AtreyDev/Portfolio.git
cd Portfolio
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy with Vercel

This repository includes a small Python WSGI adapter so Vercel can serve the existing `index.html` through its Python runtime. From the project directory:

```bash
npm install -g vercel
vercel
```

For a production deployment, use `vercel --prod` after linking the project to your Vercel account.

## About me

I am Atrey Dev Pandey, a Computer Science Engineering student at Chandigarh University. My interests include artificial intelligence, machine learning, computer vision, and full-stack development.

- Portfolio: <https://atreydev.github.io/Resume/>
- GitHub: <https://github.com/AtreyDev>
- LinkedIn: <https://www.linkedin.com/in/atreydev-pandey>
- Email: <mailto:atreydevpandey@gmail.com>
