# John Wrightsman - Personal Portfolio Website

A responsive personal portfolio website showcasing my projects and skills.

## How to Run This Website

### Option 1: Local Development (Recommended)
1. **Download/Clone** this repository to your computer
2. **Navigate** to the project folder in your terminal/command prompt
3. **Open** `index.html` in your web browser
   - Simply double-click the file, or
   - Right-click → "Open with" → Choose your browser

### Option 2: Live Server (For Development)
If you have VS Code with Live Server extension:
1. **Open** the project folder in VS Code
2. **Right-click** on `index.html`
3. **Select** "Open with Live Server"
4. The website will open at `http://127.0.0.1:5500`

### Option 3: Python Simple Server
If you have Python installed:
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```
Then visit `http://localhost:8000` in your browser

### Option 4: Node.js Server
If you have Node.js installed:
```bash
# Install a simple server globally
npm install -g http-server

# Navigate to project folder and run
http-server

# Or use npx without installing
npx http-server
```

## Browser Compatibility
- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ✅ Mobile browsers

## Technologies Used
- **HTML5** - Semantic markup and form validation
- **CSS3** - Custom styling and responsive design
- **Bootstrap 5.3.2** - Responsive framework
- **Font Awesome 6.4.0** - Icons
- **JavaScript** - Form validation

## Project Structure
```
├── index.html          # Homepage
├── about.html          # About Me page
├── resume.html         # Resume page
├── projects.html       # Projects showcase
├── contact.html        # Contact form
├── thankyou.html       # Thank you page
├── styles.css          # Custom styles
└── images/             # Image assets
```
