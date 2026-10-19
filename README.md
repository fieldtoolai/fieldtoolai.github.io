# Field Tool AI

Static directory of real AI tools for small businesses, organized by trade. Plain HTML/CSS/JS, no build step needed to serve. Live preview on GitHub Pages at https://fieldtoolai.github.io/ (served from the `main` branch root). Also Vercel-ready (deploy the folder as-is).

- `build/data.py` holds all tool listings; `build/gen.py` regenerates every page plus sitemap.xml, robots.txt and llms.txt. Run `python3 build/gen.py` after editing.
- `DOMAIN` in `build/gen.py` is `https://fieldtoolai.github.io` and `EMAIL` is `leonisas2026@gmail.com`. If the custom domain fieldtoolai.com is registered later, change them there, then regenerate.
- Newsletter form is a placeholder (no backend). Sponsor slots are placeholders. Affiliate links: Fireflies.ai (FirstPromoter, `?fpr=john-f49468`). Add markers to `AFFILIATE_MARKERS` in gen.py so new referral links get rel="sponsored".
- Tool URLs and AI feature claims were checked against official sites on 2026-10-15. No pricing is listed.
